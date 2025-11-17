from dataclasses import dataclass, fields, MISSING
from contextlib import contextmanager
from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException, NotFound, Forbidden
from markupsafe import escape
import mysql.connector
import datetime
import logging
import json
from typing import Dict, Optional, cast, Any
from dotenv import load_dotenv
from werkzeug.wrappers.response import Response
import os

load_dotenv()

TYPE_CONVERSIONS = {
    int: int,
    float: float,
    bool: lambda v: str(v).lower() in ("1", "true", "yes"),
    str: lambda v: v,
}


@dataclass
class Airport:
    ident: str
    name: str
    municipality: str


class Database:
    logger = logging.getLogger(__name__)

    def __init__(self, config) -> None:
        self.config = config

    @contextmanager
    def get_conn_cur(self, commit_on_exit: bool = False):
        conn = None
        cur = None
        try:
            conn = mysql.connector.connect(**self.config)
            cur = conn.cursor(dictionary=True)
            yield cur
            if commit_on_exit:
                conn.commit()
        except mysql.connector.Error as e:
            Database.logger.error(
                "DB error: %s Errno:%s State:%s",
                e.msg,
                getattr(e, "errno", None),
                getattr(e, "sqlstate", None),
            )
            raise
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def _row_to_airport(self, row) -> Airport:
        expected_fields = {}
        for field in fields(Airport):
            if field.name in row:
                value = row[field.name]
                converter = TYPE_CONVERSIONS.get(field.type, lambda v: v)
                value = converter(value)
                expected_fields[field.name] = value
            elif field.default is not MISSING:
                expected_fields[field.name] = field.default
            elif field.default_factory is not MISSING:
                expected_fields[field.name] = field.default_factory()
            else:
                raise KeyError(f"Missing required field: {field.name}")

        return Airport(**expected_fields)

    def get_by_icao(self, params: tuple = ()) -> Optional[Airport]:
        sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
        with self.get_conn_cur() as cur:
            cur.execute(sql, params)
            row = cast(Optional[Dict[str, Any]], cur.fetchone())
            return self._row_to_airport(row) if row else None


class Server(Flask):
    version = "0.2.0"

    def __init__(
        self,
        import_name: str,
        *,
        debug: bool = False,
        host: str = "localhost",
        port: int = 5000,
        db_config: dict,
        **kwargs,
    ):
        self.server_host = host
        self.server_port = port
        self.server_debug = debug
        self.server_start_time = datetime.datetime.now()
        self.server_db = Database(db_config)

        super().__init__(
            import_name,
            **kwargs,
        )

    def register_routes(self):
        @self.route("/favicon.ico")
        def favicon():
            return "", 204

        @self.route("/status", methods=["GET"])
        def status():
            if self.server_debug:
                return self.getStatus()
            raise Forbidden("Restricted access.")

        @self.route("/kenttä/<icao>", methods=["GET"])
        def get_airport_by_icao(icao):
            airport = self.server_db.get_by_icao((icao.upper(),))
            if airport:
                return self.getPayload(
                    message="Airport found",
                    data=airport.__dict__,
                    success=True,
                    code=200,
                )
            raise NotFound(f"Airport not found with ICAO: {escape(icao)}")

    def _uptime(self):
        uptime = datetime.datetime.now() - self.server_start_time
        delta = uptime.total_seconds()
        hours, remainder = divmod(delta, 3600)
        minutes, seconds = divmod(remainder, 60)
        return "".join(
            (
                f"Days: {uptime.days} Hours: {int(hours):d} ",
                f"Minutes: {int(minutes):d} ",
                f"seconds: {int(seconds):d}",
            )
        )

    def getStatus(self):
        return self.getPayload(
            message="Server healthy",
            data={
                "server_status": {
                    "host": self.server_host,
                    "port": self.server_port,
                    "debug": self.server_debug,
                    "start_time": self.server_start_time.strftime("%c"),
                    "alive": self._uptime(),
                }
            },
            success=True,
            code=200,
        )

    def getPayload(
        self,
        message: Optional[str] = None,
        data: Optional[Any] = None,
        *,
        success: bool = True,
        code: int = 200,
        error: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> Response:
        payload = {"success": success, "code": code}
        if message:
            payload["message"] = message
        if data is not None:
            payload["data"] = data
        if error is not None:
            payload["error"] = error

        payload.update(kwargs)
        if self.server_debug:
            print("[DEBUG] Payload:", json.dumps(payload, indent=2))

        response = jsonify(payload)
        response.status_code = code
        return response

    def json_error(
        self,
        error: Optional[Exception] = None,
        message: Optional[str] = None,
        code: int = 500,
    ) -> Response:
        if isinstance(error, HTTPException):
            return self.getPayload(
                success=False,
                code=error.code or code,
                error={"type": error.__class__.__name__, "message": error.description},
            )

        if isinstance(error, mysql.connector.Error):
            return self.getPayload(
                success=False,
                code=500,
                error={
                    "type": "DatabaseError",
                    "errno": error.errno,
                    "sqlstate": error.sqlstate,
                    "message": error.msg,
                },
            )
        self.logger.error("Unhandled exception", exc_info=error)
        return self.getPayload(
            success=False,
            code=code,
            error={
                "type": error.__class__.__name__ if error else "UnknownError",
                "message": str(error) if error else (message or "Something went wrong"),
            },
        )

    def listen(self):
        def _max_msg_len(messages: list[str]) -> int:
            return max(len(line) for line in messages)

        def _render_with_borders(messages):
            def _render_line(message, max_length):
                content_width = max_length - 4
                total_pad = content_width - len(message)
                left_pad = total_pad // 2
                right_pad = total_pad - left_pad

                return f"|{' ' * left_pad}{message}{' ' * right_pad}|"

            raw_length = _max_msg_len(messages)
            max_length = raw_length + 6
            if raw_length % 2 != 0:
                max_length += 1

            formatted_messages = [
                _render_line(message, max_length) for message in messages
            ]

            inner_border_width = max_length // 4 - 1
            border = ">~" + "~<>~" * inner_border_width + "~<"

            return "\n".join(
                [
                    border,
                ]
                + [formatted_messages[0], border, _render_line("", max_length)]
                + [
                    item
                    for message in formatted_messages[1:-1]
                    for item in (message, _render_line("", max_length))
                ]
                + [
                    border,
                    _render_line("", max_length),
                    formatted_messages[-1],
                    _render_line("", max_length),
                ]
                + [border],
            )

        try:
            listen_messages = [
                f"<< Server: {__name__} | ~<>~ | v.{Server.version} >>",
                f"Mode: {'DEBUG' if self.server_debug else 'PROD'}",
                f"{datetime.datetime.now().strftime('%c')}",
                f"Healthy: {True}",
                f"> Listening: http://{self.server_host}:{self.server_port} <",
            ]
            result_msg = _render_with_borders(listen_messages)
            print(result_msg)
            self.register_routes()
            super().run(
                host=self.server_host,
                port=self.server_port,
                debug=self.server_debug,
            )

        except Exception as e:
            error_messages = [
                f"Server: {__name__}",
                f"Healthy: {False}",
                f"Error: {type(e).__name__}: {str(e)}",
            ]
            error_msg = _render_with_borders(error_messages)
            print(error_msg)


server = Server(
    __name__,
    host="127.0.0.1",
    port=5005,
    debug=True,  # switch False for "fake prod mode"
    db_config={
        "user": os.getenv("DB_USER", "devuser"),
        "password": os.getenv("DB_PASSWORD", "devpw"),
        "host": os.getenv("DB_HOST", "127.0.0.1"),
        "port": os.getenv("DB_PORT", 3306),
        "database": os.getenv("DB_NAME", "flight_game"),
    },
)


@server.errorhandler(Exception)
def handle_general_error(e):
    return server.json_error(e)


if __name__ == "__main__":
    try:
        server.listen()
    finally:
        if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            print()
            print(
                "\n".join(
                    (
                        "--- Total server runtime ---",
                        f"From: {server.server_start_time.strftime('%c')}",
                        f"Till: {datetime.datetime.now().strftime('%c')}",
                        f"{server._uptime()}",
                    )
                )
            )
            print("\nShutting down...")

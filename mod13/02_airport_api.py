from dataclasses import dataclass, fields, MISSING
from contextlib import contextmanager
from flask import Flask, jsonify
from markupsafe import escape
import mysql.connector
import datetime
from typing import Dict, Optional, Union, cast, Any
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass
class Airport:
    ident: str
    name: str
    municipality: str


DB_CONFIG = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "port": os.getenv("DB_PORT", 3306),
    "database": os.getenv("DB_NAME", "flight_game"),
}


TYPE_CONVERSIONS = {
    int: int,
    float: float,
    bool: lambda v: str(v).lower() in ("1", "true", "yes"),
    str: lambda v: v,
}


class Database:
    def __init__(self, config) -> None:
        self.config = config

    @contextmanager
    def get_conn(self, commit_on_exit: bool = True):
        conn = mysql.connector.connect(**self.config)
        cur = conn.cursor(dictionary=True)
        try:
            yield cur
            if commit_on_exit:
                conn.commit()
        finally:
            cur.close()
            conn.close()

    def _row_to_airport(self, row) -> Airport:
        kwargs = {}

        for field in fields(Airport):
            if field.name in row:
                value = row[field.name]
                converter = TYPE_CONVERSIONS.get(field.type, lambda v: v)
                value = converter(value)
                kwargs[field.name] = value
            elif field.default is not MISSING:
                kwargs[field.name] = field.default
            elif field.default_factory is not MISSING:
                kwargs[field.name] = field.default_factory()
            else:
                raise KeyError(f"Missing required field: {field.name}")

        return Airport(**kwargs)

    def get_by_icao(self, params: tuple = ()) -> Optional[Airport]:
        sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
        with self.get_conn(commit_on_exit=False) as cur:
            cur.execute(sql, params)
            row = cast(Optional[Dict[str, Any]], cur.fetchone())
            return self._row_to_airport(row) if row else None


class Server(Flask):
    version = "0.1.0"

    def __init__(
        self,
        import_name: str,
        *,
        host: str = "127.0.0.1",
        port: int = 5000,
        debug: bool = False,
        static_url_path: Optional[str] = None,
        static_folder: Union[str, os.PathLike[str], None] = "static",
        static_host: Union[str, None] = None,
        host_matching: bool = False,
        subdomain_matching: bool = False,
        template_folder: Union[str, os.PathLike[str], None] = "templates",
        instance_path: Union[str, None] = None,
        instance_relative_config: bool = False,
        root_path: Union[str, None] = None,
        **kwargs,
    ):
        self.server_host = host
        self.server_port = port
        self.server_debug = debug

        super().__init__(
            import_name,
            static_url_path,
            static_folder,
            static_host,
            host_matching,
            subdomain_matching,
            template_folder,
            instance_path,
            instance_relative_config,
            root_path,
            **kwargs,
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
            if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
                print(result_msg)

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
            print("\n".join(error_msg))


serverSettings = {"host": "127.0.0.1", "port": 5001, "debug": True}
server = Server(__name__, **serverSettings)
db = Database(DB_CONFIG)


@server.route("/favicon.ico", methods=["GET"])
def favicon():
    return "", 204


@server.route("/kenttä/<icao>", methods=["GET"])
def airport_by_icao(icao):
    airport = db.get_by_icao((icao.upper(),))
    if airport:
        return jsonify(airport.__dict__), 200
    else:
        return jsonify(
            {
                "error": "Not Found",
                "message": f"Airport not found with ICAO: {escape(icao)}",
            }
        ), 404


@server.errorhandler(Exception)
def handle_general_error(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500


if __name__ == "__main__":
    server.listen()

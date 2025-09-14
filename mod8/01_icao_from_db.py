import mysql.connector


def fetch_airport_by_icao(icao_str: str) -> tuple[str, str]:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        database="flight_game",
        user="smol",
        password="2122",
        autocommit=True,
    )
    cur = conn.cursor()
    sql = "SELECT `name`, `municipality` FROM `airport` WHERE `ident` = %s"
    cur.execute(sql, (icao_str,))
    row = cur.fetchone()
    return (row[0], row[1])  # type: ignore


user_input = "EFKK"
airport_info = fetch_airport_by_icao(user_input)
print(airport_info)

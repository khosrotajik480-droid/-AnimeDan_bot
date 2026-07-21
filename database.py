import sqlite3

DATABASE_NAME = "anime_bot.db"


def connect():

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    return conn, cursor


def create_database():

    conn, cursor = connect()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        telegram_id INTEGER UNIQUE,

        first_name TEXT,

        username TEXT,

        joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )

    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS animes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE

    )

    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS seasons(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        anime_id INTEGER,

        season_number INTEGER,

        FOREIGN KEY(anime_id)

        REFERENCES animes(id)

    )

    """)

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS episodes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        season_id INTEGER,

        episode_number INTEGER,

        file_id TEXT,

        caption TEXT,

        FOREIGN KEY(season_id)

        REFERENCES seasons(id)

    )

    """)

    conn.commit()

    conn.close()
    def add_user(

    telegram_id,

    first_name,

    username

):

    conn, cursor = connect()

    cursor.execute(

        """

        INSERT OR IGNORE INTO users(

            telegram_id,

            first_name,

            username

        )

        VALUES(?,?,?)

        """,

        (

            telegram_id,

            first_name,

            username

        )

    )

    conn.commit()

    conn.close()


def get_user(

    telegram_id

):

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT *

        FROM users

        WHERE telegram_id=?

        """,

        (

            telegram_id,

        )

    )

    data = cursor.fetchone()

    conn.close()

    return data


def get_users():

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT *

        FROM users

        ORDER BY id DESC

        """

    )

    data = cursor.fetchall()

    conn.close()

    return data


def users_count():

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT COUNT(*)

        FROM users

        """

    )

    count = cursor.fetchone()[0]

    conn.close()

    return countdef add_anime(

    name

):

    conn, cursor = connect()

    cursor.execute(

        """

        INSERT INTO animes(

            name

        )

        VALUES(?)

        """,

        (

            name,

        )

    )

    conn.commit()

    conn.close()


def get_animes():

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT *

        FROM animes

        ORDER BY id ASC

        """

    )

    data = cursor.fetchall()

    conn.close()

    return data


def get_anime(

    anime_id

):

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT *

        FROM animes

        WHERE id=?

        """,

        (

            anime_id,

        )

    )

    data = cursor.fetchone()

    conn.close()

    return data


def delete_anime(

    anime_id

):

    conn, cursor = connect()

    cursor.execute(

        """

        DELETE FROM animes

        WHERE id=?

        """,

        (

            anime_id,

        )

    )

    conn.commit()

    conn.close()
    def add_season(

    anime_id,

    season_number

):

    conn, cursor = connect()

    cursor.execute(

        """

        INSERT INTO seasons(

            anime_id,

            season_number

        )

        VALUES(?,?)

        """,

        (

            anime_id,

            season_number

        )

    )

    conn.commit()

    conn.close()


def get_seasons(

    anime_id

):

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT *

        FROM seasons

        WHERE anime_id=?

        ORDER BY season_number ASC

        """,

        (

            anime_id,

        )

    )

    data = cursor.fetchall()

    conn.close()

    return data


def get_season(

    season_id

):

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT *

        FROM seasons

        WHERE id=?

        """,

        (

            season_id,

        )

    )

    data = cursor.fetchone()

    conn.close()

    return data


def delete_season(

    season_id

):

    conn, cursor = connect()

    cursor.execute(

        """

        DELETE FROM seasons

        WHERE id=?

        """,

        (

            season_id,

        )

    )

    conn.commit()

    conn.close()

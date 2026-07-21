import sqlite3

DATABASE_NAME = "database.db"
def connect():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    return conn, cursor
  def create_users():

    conn, cursor = connect()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        telegram_id INTEGER UNIQUE,

        first_name TEXT,

        username TEXT,

        join_date TEXT

    )

    """)

    conn.commit()

    conn.close()
    def create_animes():

    conn, cursor = connect()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS animes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT UNIQUE

    )

    """)

    conn.commit()

    conn.close()
    def create_seasons():

    conn, cursor = connect()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS seasons(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        anime_id INTEGER,

        season_number INTEGER

    )

    """)

    conn.commit()

    conn.close()
    def create_episodes():

    conn, cursor = connect()

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS episodes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        season_id INTEGER,

        episode_number INTEGER,

        chat_id INTEGER,

        message_id INTEGER

    )

    """)

    conn.commit()

    conn.close()
    def create_database():

    create_users()

    create_animes()

    create_seasons()

    create_episodes()
    from datetime import datetime


def add_user(telegram_id, first_name, username):

    conn, cursor = connect()

    cursor.execute("""

    INSERT OR IGNORE INTO users(

        telegram_id,

        first_name,

        username,

        join_date

    )

    VALUES(?,?,?,?)

    """,

    (

        telegram_id,

        first_name,

        username,

        datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    )

    )

    conn.commit()

    conn.close()
  def users_count():

    conn, cursor = connect()

    cursor.execute(

        "SELECT COUNT(*) FROM users"

    )

    count = cursor.fetchone()[0]

    conn.close()

    return count
    def add_anime(name):

    conn, cursor = connect()

    cursor.execute(

        "INSERT INTO animes(name) VALUES(?)",

        (name,)

    )

    conn.commit()

    conn.close()
    def get_animes():

    conn, cursor = connect()

    cursor.execute(

        "SELECT * FROM animes"

    )

    data = cursor.fetchall()

    conn.close()

    return data
    def get_anime_id(name):

    conn, cursor = connect()

    cursor.execute(

        "SELECT id FROM animes WHERE name=?",

        (name,)

    )

    data = cursor.fetchone()

    conn.close()

    if data:

        return data[0]

    return None
    def add_season(anime_id, season):

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

            season

        )

    )

    conn.commit()

    conn.close()
    def get_seasons(anime_id):

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT season_number

        FROM seasons

        WHERE anime_id=?

        ORDER BY season_number

        """,

        (anime_id,)

    )

    data = cursor.fetchall()

    conn.close()

    return data
    def add_episode(
    season_id,
    episode_number,
    chat_id,
    message_id
):

    conn, cursor = connect()

    cursor.execute(

        """

        INSERT INTO episodes(

            season_id,

            episode_number,

            chat_id,

            message_id

        )

        VALUES(?,?,?,?)

        """,

        (

            season_id,

            episode_number,

            chat_id,

            message_id

        )

    )

    conn.commit()

    conn.close()
    def get_episodes(season_id):

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT

        episode_number,

        chat_id,

        message_id

        FROM episodes

        WHERE season_id=?

        ORDER BY episode_number

        """,

        (season_id,)

    )

    data = cursor.fetchall()

    conn.close()

    return data
    def get_episode(season_id, episode_number):

    conn, cursor = connect()

    cursor.execute(

        """

        SELECT

        chat_id,

        message_id

        FROM episodes

        WHERE season_id=?

        AND episode_number=?

        """,

        (

            season_id,

            episode_number

        )

    )

    data = cursor.fetchone()

    conn.close()

    return data
    def delete_episode(season_id, episode_number):

    conn, cursor = connect()

    cursor.execute(

        """

        DELETE FROM episodes

        WHERE season_id=?

        AND episode_number=?

        """,

        (

            season_id,

            episode_number

        )

    )

    conn.commit()

    conn.close()
    def delete_season(season_id):

    conn, cursor = connect()

    cursor.execute(

        "DELETE FROM episodes WHERE season_id=?",

        (season_id,)

    )

    cursor.execute(

        "DELETE FROM seasons WHERE id=?",

        (season_id,)

    )

    conn.commit()

    conn.close()
    def delete_anime(anime_id):

    conn, cursor = connect()

    cursor.execute(

        "SELECT id FROM seasons WHERE anime_id=?",

        (anime_id,)

    )

    seasons = cursor.fetchall()

    for season in seasons:

        cursor.execute(

            "DELETE FROM episodes WHERE season_id=?",

            (season[0],)

        )

    cursor.execute(

        "DELETE FROM seasons WHERE anime_id=?",

        (anime_id,)

    )

    cursor.execute(

        "DELETE FROM animes WHERE id=?",

        (anime_id,)

    )

    conn.commit()

    conn.close()
    def update_episode(

    season_id,

    episode_number,

    chat_id,

    message_id

):

    conn, cursor = connect()

    cursor.execute(

        """

        UPDATE episodes

        SET

        chat_id=?,

        message_id=?

        WHERE

        season_id=?

        AND

        episode_number=?

        """,

        (

            chat_id,

            message_id,

            season_id,

            episode_number

        )

    )

    conn.commit()

    conn.close()
    

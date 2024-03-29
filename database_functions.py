import sqlite3


def tables_setup():
    conn_players = sqlite3.connect("tables/players.db")
    conn_scores = sqlite3.connect("tables/scores.db")

    c_players = conn_players.cursor()
    c_scores = conn_scores.cursor()

    c_players.execute("""CREATE TABLE if not exists players
                    (username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL)""")
    conn_players.commit()

    c_scores.execute("""CREATE TABLE if not exists scores
                        (score INTEGER NOT NULL,
                        time REAL NOT NULL,
                        username TEXT NOT NULL)""")
    conn_scores.commit()

    conn_players.close()
    conn_scores.close()


def add_new_player(username, password):
    try:
        conn = sqlite3.connect("tables/players.db")
        c_players = conn.cursor()
        c_players.execute(f"INSERT INTO players VALUES ('{username}', '{password}')")
        conn.commit()
        conn.close()
        return True
    except sqlite3.DatabaseError:
        return False


def login_player(username, password):
    conn = sqlite3.connect("tables/players.db")
    c_players = conn.cursor()
    c_players.execute(f"SELECT * FROM players WHERE username = '{username}'")
    user_details = c_players.fetchone()
    if user_details and user_details[1] == password:
        return True
    else:
        return False


def add_player_score(username, score, time):
    conn = sqlite3.connect("tables/scores.db")
    c_scores = conn.cursor()
    c_scores.execute(f"INSERT INTO scores VALUES ('{score}', '{time}', '{username}')")
    conn.commit()
    conn.close()


def retrieve_top_scores():
    conn = sqlite3.connect("tables/scores.db")
    c_scores = conn.cursor()
    c_scores.execute(f"SELECT * FROM scores ORDER BY score DESC, time DESC LIMIT 5")
    top_scores = c_scores.fetchall()
    conn.commit()
    conn.close()
    return top_scores

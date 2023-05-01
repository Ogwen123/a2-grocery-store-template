import sqlite3

def connect():
    from main import CONFIG
    global conn
    # DO ***NOT*** USE ABSOLUTE FILE PATHS, THEY MUST BE RELATIVE. WJEC WILL NOT BE ABLE TO MARK YOUR PROJECT OTHERWISE
    conn = sqlite3.connect(CONFIG["DB_PATH"], check_same_thread=False)
    global c
    c = conn.cursor()
    setup()

def setup():
    c.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, quantity INTEGER, availability TEXT, date TEXT)")

def fetch(query):
    c.execute(query)
    return c.fetchall()

def fetch_one(query):
    c.execute(query)
    return c.fetchone()

# TODO more methods and experiment with sqlite3 to make sure it works as a substitute
import sqlite3

# Create a database connection
def sqlite_init():
    try:
        sqlite = sqlite3.connect('src/database.db', timeout=20)
        return sqlite
    except sqlite3.Error as error:
        return exit()
sqlite = sqlite_init()

# Create a cursor
cursor = sqlite.cursor()

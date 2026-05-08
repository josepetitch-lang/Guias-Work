import sqlite3

namedb = "pornito.db"

def getconnection():
    try:
        connection = sqlite3.connect(namedb)
        return connection
    except sqlite3.error as e: 
        print(f"Oye", (e), "PARA NOJODA, MAMAGUEVO, NOJODA ")
        return None
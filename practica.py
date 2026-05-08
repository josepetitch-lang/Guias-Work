import sqlite3

connection = sqlite3.connect("eusoubrazucaymegustanlasgarotas.db")
cursor = connection.cursor()

cursor.execute ("""CREATE TABLE IF NOT EXISTS consolas (
                   id INTEGER PRIMARY KEY,
                   name TEXT, 
                   company TEXT,
                   games TEXT,
                   year_sold INTEGER) 
                """)
               

cursor.execute ("INSERT INTO consolas (id,name,company,games,year_sold) VALUES (1, 'PS2', 'SONY', 'NO GAMES', 2006)")

connection.commit()
connection.close()

print("ESOOOOOO NOJODAJJKSJKSJSKJSK")


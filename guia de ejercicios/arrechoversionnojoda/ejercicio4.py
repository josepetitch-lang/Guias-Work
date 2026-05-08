#4. Explorador de Tablas (Nivel Hacker)
#Investiga cómo listar todas las tablas disponibles en tu base de datos desde Python usando sqlite3 y muestra sus nombres por consola. 
#(Pista: busca información sobre la tabla interna sqlite_master).:-

import sqlite3

connection = sqlite3.connect(r"C:\Users\vikto\OneDrive\Documentos\SQLITE\northwind.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
tablas = cursor.fetchall()
print("Tablas disponibles:")
for t in tablas:
    print(f"- {t[0]}")
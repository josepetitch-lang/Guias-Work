import sqlite3

connection = sqlite3.connect("northwind.db")
cursor = connection.cursor()

cursor.execute("SELECT ProductName, UnitPrice FROM Products ORDER BY UnitPrice DESC LIMIT 1;")

producto_caro = cursor.fetchone()

print(f"El producto más caro es: {producto_caro[0]} con un precio de ${producto_caro[1]}")

connection.close() #xd


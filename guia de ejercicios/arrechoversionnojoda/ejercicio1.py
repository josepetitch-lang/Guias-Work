#1. Analista de datos con Python: 
#Escribe un script en Python que pida al usuario el ID de una categoría (CategoryID)
#Muestre en la consola el valor total en dinero del inventario de esa categoría (es decir, la suma de UnitPrice * UnitsInStock de todos los productos de esa categoría).

import sqlite3

connection = sqlite3.connect("northwind.db")
cursor = connection.cursor()

c_id = input("Necesito el ID de una Categoría:")

cursor.execute("""SELECT SUM(UnitPrice * UnitsInStock) FROM Products ID WHERE CategoryID = ?""", (c_id))
total = cursor.fetchone()[0]
print(f"El valor total del inventario para la categoría {c_id} es: ${total:.2f}")
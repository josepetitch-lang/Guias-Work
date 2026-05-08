#3. Productos en Peligro: 
#Usando Python y SQL, crea un script que encuentre los productos que tienen UnitsInStock igual a 0 pero que NO están descontinuados (Discontinued = 0).
#Imprime una lista de "Alerta de Reabastecimiento" en la consola.

import sqlite3 

connection = sqlite3.connect("northwind.db")
cursor = connection.cursor()

cursor.execute("SELECT ProductName FROM Products WHERE UnitsInStock = 0")
productos = cursor.fetchall()
print("Alerta de Reabastecimiento (que tenía que ver jolines tio)")
if productos:
    for p in productos:
        print(f"el producto {p[0]} está agotado")
else:
    print("Todo en orden, no hay productos agotados")

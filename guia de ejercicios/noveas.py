import sqlite3
import time

connection = sqlite3.connect("northwind.db")
cursor = connection.cursor()

query = """
SELECT ProductName, UnitsInStock 
FROM Products 
WHERE UnitsInStock > 0
ORDER bY UnitsInStock ASC
LIMIT 10;
"""

cursor.execute(query)

productos = cursor.fetchall()

print("Stock del Objeto (Objetos)")

for product in productos:
    print(f"Objeto: {product[0]}, Stock: {product[1]}")
    time.sleep(10) # jajajajaja

connection.close()

#Asegúrate de que sqlite3.connect("northwind.db") apunte al archivo real PORFAVOR
#(puede que necesites poner ../northwind.db dependiendo desde dónde ejecutes el script)
#PD: pongan raw si es necesario xdxdxd

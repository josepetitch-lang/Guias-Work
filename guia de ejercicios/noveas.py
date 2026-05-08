import sqlite3
import time

connection = sqlite3.connect(r"C:\Users\vikto\OneDrive\Documentos\SQLITE\northwind.db")
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

print("TOP 10 MOMOS QUE A NADIE LE DA RISA")

for product in productos:
    print(f"Objeto: {product[0]}, Stock: {product[1]}")
    time.sleep(10)

connection.close()

#Asegúrate de que sqlite3.connect("northwind.db") apunte al archivo real (puede que necesites poner ../northwind.db dependiendo desde dónde ejecutes el script)
#PD: pongan raw si es necesario xdxdxd

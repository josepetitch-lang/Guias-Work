#2. Reporte de Ciudades Estrella:
#Escribe una consulta SQL que devuelva las 3 ciudades (City de la tabla Customers) que tienen la mayor cantidad de clientes registrados.#

import sqlite3

connection = sqlite3.connect("northwind.db")
cursor = connection.cursor()

cursor.execute("""SELECT City, COUNT(CustomerID) as ClientesTotal FROM Customers GROUP BY City ORDER BY TotalClientes DESC LIMIT 3""")
ciudades = cursor.fetchall()
for ciudad in ciudades:
    print(f"Ciudad: {ciudad[0] ! Clientes : {ciudad[1]}}")
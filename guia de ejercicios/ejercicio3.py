import sqlite3

pais = input("Ingresa el país a buscar:")

connection = sqlite3.connect(r"C:\Users\vikto\OneDrive\Documentos\SQLITE\northwind.db")
cursor = connection.cursor()

query = """SELECT COUNT(*) FROM Customers WHERE COUNTRY = ?"""
cursor.execute(query, (pais,))

resultado = cursor.fetchone()
cantidad = resultado[0]

print(f"Hay {cantidad} en el país de: {resultado}")
print("Si te tocó Venezuela, perdoname mucho, te estafaron xd")

connection.close()


# r = raw (crudo en inglés) dice = "No interpretes una mierda nojoda, me teneis el huevo flaco nojoda nojoda nojoda nojoda"

# \n = salto de línea
# \t = tabulación
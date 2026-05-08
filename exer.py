import sqlite3

connection = sqlite3.connect(r"C:\Users\vikto\OneDrive\Documentos\SQLITE\northwind.db")
 
cursor = connection.cursor()

cursor.execute("""SELECT * FROM Orders ORDER BY OrderID DESC LIMIT 5;""" )

products= cursor.fetchall()
print(len(products))
print(products)

print(isinstance(products, str))
print(isinstance(products, list))

connection.close()

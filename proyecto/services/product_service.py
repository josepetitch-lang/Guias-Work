import sqlite3
from data.database import getconnection
from models.products import Products


class ProductService:
    def get_all_products():     
        connection = getconnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * From products")
        products = cursor.fetchall()
        connection.close()
        return products

    def create_products():
        connection = getconnection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO products (name, price, category, stock) VALUES (?.?,?,?')", (Products.name, Products.price, Products.category, Products.stock))
        connection.commit()
        connection.close()

    def update_products():
        connection = getconnection()
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET name = ?, price = ?, category = ?. stock = ? WHERE id = ?", (Products.id))
        connection.commit()
        connection.close()

    def delete_products():
        connection = getconnection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (Products.id))
        connection.commit()
        connection.close()

    


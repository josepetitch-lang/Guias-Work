from models.products import Products
from services.product_service import ProductService

nombre = input("Precio:")
precio = input("Precio:")
categoría = input("Precio:")
stock = input ("Stock:")

product = Products(nombre,precio,categoría, stock)

print(product)


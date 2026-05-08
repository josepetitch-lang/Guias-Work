class Products:
    def __init__(self,id,name,price,category,stock):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Category: {self.category}, StocK: {self.stock}"
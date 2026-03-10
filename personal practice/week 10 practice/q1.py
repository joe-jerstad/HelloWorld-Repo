class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def set_name(self, new_name):
        self.name = new_name
    
    def set_price(self, new_price):
        self.price = new_price

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

prod1 = Product('Trombone', 300, 50)
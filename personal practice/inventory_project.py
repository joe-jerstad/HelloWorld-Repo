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
    
    def change_name(self, new_name):
        self.name = new_name

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, new_quant):
        self.quantity = new_quant

    def total_value(self):
        return self.quantity * self.price
    
    def reduce_stock(self, amount):
        self.quantity -= amount

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = {}

    def get_cart(self):
        cart_string = ''
        
        for product in self.cart:
            cart_string += f'Product: {product.name} Quantity: {self.cart[product]}\n'
        
        return cart_string
        
        
            
    def add_to_cart(self, product, amount):
        self.cart[product] = amount
    
    def remove_from_cart(self, product):
        del self.cart[product]

    def empty_cart(self):
        self.cart = self.cart.clear()

    def calculate_total(self):
        total = 0

        for product in self.cart:
            total += self.cart[product] * product.get_price()

        return total
    
class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = {}
    
    def add_product(self, product):
        self.inventory[product] = product.get_quantity()
    
    def sell_product(self, product_name, quantity):
        self.inventory[product_name] -= quantity
        product_name.reduce_stock(quantity)

    def inventory_value(self):
        total = 0

        for product in self.inventory:
            total += self.inventory[product] * product.get_price()

        return total
    
prod1 = Product('Shirt', 50, 100)
prod2 = Product('Pants', 70, 20)
prod3 = Product('Socks', 10, 200)
prod4 = Product('Shorts', 30, 70)

cust1 = Customer('Joe', 'joe@gmail.com')

store1 = Store('The Store')

cust1.add_to_cart(prod1, 3)
cust1.add_to_cart(prod3, 2)
    
print(cust1.get_cart())







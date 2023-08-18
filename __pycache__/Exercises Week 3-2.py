class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display(self):
        print("\n***** PRODUCT *****")
        print("Product:", self.name)
        print("Price: $", self.price)
        print("Quantity:", self.quantity)
        print("total:", self.calculate_total())
    
    def calculate_total(self):
        return self.price * self.quantity


class Electronics(Product):
    def __init__(self, name, price, quantity, brand):
        super().__init__(name, price, quantity)
        self.brand = brand
    
    def display(self):
        super().display()
        print(f"Brand: {self.brand}")


class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size
    
    def display(self):
        super().display()
        print(f"Size: {self.size}")


class Books(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author
    
    def display(self):
        super().display()
        print(f"Author: {self.author}")


electronics = Electronics("Laptop", 999.99, 2, "HP")
electronics.display()

clothing = Clothing("T-shirt", 19.99, 5, "M")
clothing.display()

book = Books("The Great Help", 9.99, 10, "Kare45n Dela Rosa")
book.display()

# electronics.display()
# print(f"Total cost: ${electronics.calculate_total():.2f}\n")

# clothing.display()
# print(f"Total cost: ${clothing.calculate_total():.2f}\n")

# book.display()
# print(f"Total cost: ${book.calculate_total():.2f}")


# p1 = Product("Milk", 2.99, 12)
# p1.display()
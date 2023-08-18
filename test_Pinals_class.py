class Book:
    def __init__(self, title, quantity, price, author, publisher_name):
        self.title = title
        self.quantity = quantity
        self.price = price
        self.author = author
        self.publisher_name = publisher_name

    def displaydata(self):
        print("Book Title:", self.title)
        print("Quantity:", self.quantity)
        print("Price:", self.price)
        print("Author:", self.author)
        print("Publisher Name:", self.publisher_name)

my_book = Book("Sample Book", 1, "$20", "John Author", "Nick Publisher")
my_book.displaydata()

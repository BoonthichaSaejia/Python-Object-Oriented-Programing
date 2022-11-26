# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author= author
        self.pages = pages
        self.price = price
        # TODO: add properties
        self.__secret = "This is a secret attribute"
    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price * (1-self._discount)
        else:
            return self.price
    
    def setDiscount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstor", 1200, 400.00)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 127.00)

# TODO: print the price of book1
print("Book1's price is",b1.getPrice())

# TODO: try setting the discount
print("Book2's price is",b2.getPrice())
b2.setDiscount(0.25)
print("Book2's price is",b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
#print(b2.__secret) #uncomment to try
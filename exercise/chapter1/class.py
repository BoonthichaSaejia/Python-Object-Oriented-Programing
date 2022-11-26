class Book:
    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")
    __booklist = None
    def setTitle(self, newTitle):
        self.title = newTitle
    
    @classmethod
    def getBooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getBooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    def __init__(self,title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype

print("Book type:", Book.getBooktypes())

b1 = Book("Title 1","HARDCOVER")
# b2 = Book("Title 2","COMIC") #uncomment to see error
b3 = Book("Title 3","PAPERBACK")

thebooks = Book.getBooklist()
thebooks.append(b1)
thebooks.append(b3)
print(thebooks)
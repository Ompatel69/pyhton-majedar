#library management
class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []
    def addbook(self, book):
        self.books.append(book)
        self.nobooks = len(self.books)
    def showinfo(self):
        print(f"There are {self.nobooks} books in the library and they are : ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addbook("hunda punda")
l1.addbook("secrets of the magician")
l1.addbook("hunda punda part two")
l1.showinfo()
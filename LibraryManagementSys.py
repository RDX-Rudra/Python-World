class Library:
    def __init__(self) -> None:
        self.noBooks = 0
        self.books = []
        
    def addbook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)
        
    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are")
        for book in self.books:
            print(book)
            
l1 = Library()
l1.addbook("Higher Math")
l1.addbook("Higher phy")
l1.addbook("Higher chem")
l1.showInfo()
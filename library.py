class Library:
    def _init_(self, name, address):
        self.name = name
        self.address = address
        self.books = []


    def add_book(self, book):
        self.books.append(book)
        print(book.title, 'was added')
    
    def remove_book(self, book):
        self.books.remove(book)
        print(book.title, "was removed")
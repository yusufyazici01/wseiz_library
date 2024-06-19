class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Book {book.title} added to the library.')

    def remove_book(self, book):
        self.books.remove(book)
        print(f'Book {book.title} removed from the library.')

    def add_patron(self, patron):
        self.patrons.append(patron)
        print(f'Patron {patron.name} added to the library.')

    def remove_patron(self, patron):
        self.patrons.remove(patron)
        print(f'Patron {patron.name} removed from the library.')

    def list_books(self):
        print(f'Books in {self.name}:')
        for book in self.books:
            print(f'  {book}')

    def list_patrons(self):
        print(f'Patrons in {self.name}:')
        for patron in self.patrons:
            print(f'  {patron}')
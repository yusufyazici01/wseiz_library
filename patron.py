class Patron(Person):
    def __init__(self, name, patron_id):
        super().__init__(name, patron_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f'{self.name} borrowed {book.title}.')
        else:
            print(f'{book.title} is not available.')

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f'{self.name} returned {book.title}.')
        else:
            print(f'{self.name} does not have {book.title}.')

    def __str__(self):
        borrowed_books_titles = [book.title for book in self.borrowed_books]
        return f'{super().__str__()}, Borrowed Books: {", ".join(borrowed_books_titles) if borrowed_books_titles else "None"}'
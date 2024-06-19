from library import Library
from book import Book
from patron import Patron

our_library = Library('Wseiz Library', 'Rejtana 17, Warsaw')
our_book = Book('Robinson Cruzeo', 300, 'adventure', 'J.J Rowling', '3423-kdsjflkdsjfkl')

print("The name: ", our_library.name)
print("Number of pages:", our_book.pages)
print("The adress is", our_library.address)

our_library.add_book(our_book) 
our_library.remove_book(our_book)
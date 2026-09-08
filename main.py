from library import Book, EBook, Library, is_valid_isbn

my_library = Library()

book1 = Book("FastAPI", "Bill Lubanovic", "1111111111111")
book2 = Book("Python Crash Course", "Eric Matthes", "2222222222222")
book3 = EBook("Designing Data-Intensive Applications", "Martin Kleppmann", "3333333333333", 12.99)
book4 = EBook("Software Architecture: The Hard Parts", "Neal Ford Mark Richards Pramod Sadalage Zhamak Dehghani", "4444444444444", 20.0)
book5 = Book("Clean Code", "Robert C. Martin", "5555555555555")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)
my_library.add_book(book4)
my_library.add_book(book5)

my_library.checkout_book("1111111111111")
my_library.checkout_book("2222222222222")
my_library.return_book("1111111111111")

available_books = my_library.list_available_books()
print("Available books:")
for book in available_books:
    book.describe()

all_books = [book1, book2, book3, book4, book5]
sorted_books = sorted(all_books, key=lambda book: book.title)
print("\nSorted by title:")
for book in sorted_books:
    book.describe()

titles = list(map(lambda book: book.title, all_books))
print("\nTitles only:", titles)

print("\nISBN check:")
print(is_valid_isbn("1111111111111"))  
print(is_valid_isbn("abc"))             
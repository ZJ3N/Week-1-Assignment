class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def describe(self):
        print(f"{self.title} by {self.author} (ISBN: {self.isbn})")


class EBook(Book):
    def __init__(self, title, author, isbn, file_size_mb, is_available=True):
        super().__init__(title, author, isbn, is_available)
        self.file_size_mb = file_size_mb

    def describe(self):
        print(f"{self.title} by {self.author} (E-Book, {self.file_size_mb}MB)")


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def find_book(self, isbn):
        for book in self.__books:
            if book.isbn == isbn:
                return book
        return None

    def remove_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.__books.remove(book)
            return True
        return False

    def checkout_book(self, isbn):
        book = self.find_book(isbn)
        if book is None:
            print("Book not found.")
            return False
        elif not book.is_available:
            print("Book is already checked out.")
            return False
        else:
            book.is_available = False
            print("Book checked out successfully.")
            return True

    def return_book(self, isbn):
        book = self.find_book(isbn)
        if book and not book.is_available:
            book.is_available = True
            print("Book returned successfully.")
            return True
        elif book and book.is_available:
            print("Book was not checked out.")
            return False
        else:
            print("Book not found.")
        return False

    def list_available_books(self):
        return list(filter(lambda book: book.is_available, self.__books))


def is_valid_isbn(isbn):
    return isbn.isdigit() and len(isbn) == 13
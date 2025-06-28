# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_description(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_description(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_description(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book or its subclasses can be added.")

    def list_books(self):
        for book in self.books:
            print(book.get_description())


# ✅ TEST CASES FOR IMPLEMENTATION AND OUTPUT
if __name__ == "__main__":
    print("=== Initialization and Inheritance Checks ===")

    # Base Book
    b = Book("1984", "George Orwell")
    assert b.title == "1984"
    assert b.author == "George Orwell"
    assert b.get_description() == "Book: 1984 by George Orwell"
    print("✅ Book class passed.")

    # EBook
    eb = EBook("Digital Fortress", "Dan Brown", 1200)
    assert isinstance(eb, Book)
    assert eb.title == "Digital Fortress"
    assert eb.author == "Dan Brown"
    assert eb.file_size == 1200
    assert eb.get_description() == "EBook: Digital Fortress by Dan Brown, File Size: 1200KB"
    print("✅ EBook class passed.")

    # PrintBook
    pb = PrintBook("Brave New World", "Aldous Huxley", 268)
    assert isinstance(pb, Book)
    assert pb.title == "Brave New World"
    assert pb.author == "Aldous Huxley"
    assert pb.page_count == 268
    assert pb.get_description() == "PrintBook: Brave New World by Aldous Huxley, Page Count: 268"
    print("✅ PrintBook class passed.")

    # Library
    print("\n=== Library Composition Checks ===")
    lib = Library()
    lib.add_book(b)
    lib.add_book(eb)
    lib.add_book(pb)
    assert len(lib.books) == 3
    assert all(isinstance(book, Book) for book in lib.books)
    print("✅ Library add_book() passed.")

    # Capture and test output of list_books
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output

    lib.list_books()

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip().split('\n')

    expected_output = [
        "Book: 1984 by George Orwell",
        "EBook: Digital Fortress by Dan Brown, File Size: 1200KB",
        "PrintBook: Brave New World by Aldous Huxley, Page Count: 268"
    ]

    assert output == expected_output, f"Expected:\n{expected_output}\nGot:\n{output}"
    print("✅ Library list_books() output correct.\n")

    print("🎉 All checks passed successfully.")

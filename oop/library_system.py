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


# ✅ Initialization Checks
if __name__ == "__main__":
    print("--- Running Initialization Checks ---")

    # Base Book
    b = Book("1984", "George Orwell")
    print(f"Book initialized with: {b.title}, {b.author}")
    assert b.title == "1984"
    assert b.author == "George Orwell"

    # EBook
    eb = EBook("Digital Fortress", "Dan Brown", 1200)
    print(f"EBook initialized with: {eb.title}, {eb.author}, {eb.file_size}KB")
    assert eb.title == "Digital Fortress"
    assert eb.author == "Dan Brown"
    assert eb.file_size == 1200

    # PrintBook
    pb = PrintBook("Brave New World", "Aldous Huxley", 268)
    print(f"PrintBook initialized with: {pb.title}, {pb.author}, {pb.page_count} pages")
    assert pb.title == "Brave New World"
    assert pb.author == "Aldous Huxley"
    assert pb.page_count == 268

    print("✅ All class initializations passed.\n")

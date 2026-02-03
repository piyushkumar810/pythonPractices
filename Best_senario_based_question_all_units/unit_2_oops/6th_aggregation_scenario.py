# ✅ Solution: Aggregation – Library Management System
# 🔹 Independent Class: Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book(self):
        print(f"Title: {self.title}, Author: {self.author}")

# 🔹 Aggregating Class: Library
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []  # holds references to Book objects

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to {self.library_name}")

    def show_books(self):
        print(f"\nBooks in {self.library_name}:")
        for b in self.books:
            b.display_book()

# 🔹 Object Creation & Usage
# Create Book objects independently
b1 = Book("Clean Code", "Robert C. Martin")
b2 = Book("The Pragmatic Programmer", "Andrew Hunt")

# Create Library
lib = Library("City Central Library")

# Aggregate books into library
lib.add_book(b1)
lib.add_book(b2)

# Show books in library
lib.show_books()

# Prove independence of Book objects
print("\nBook objects still work independently:")
b1.display_book()
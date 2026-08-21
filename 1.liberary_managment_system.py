#Design a Library Management System using object-oriented programming
#principles in Python. This system should manage books and patrons (library
#users), allowing for basic operations such as adding new books, registering
#patrons, borrowing books, and returning books.
class Book:
    def __init__(self, book_id, name, author):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.available = True


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        book_id = input("Enter book ID: ")

        # Check for duplicate book ID
        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        name = input("Enter book name: ")
        author = input("Enter author name: ")

        book = Book(book_id, name, author)
        self.books.append(book)

        print("Book added successfully!")

    def register_patron(self):
        patron_id = input("Enter patron ID: ")

        # Check for duplicate patron ID
        for patron in self.patrons:
            if patron.patron_id == patron_id:
                print("Patron ID already exists!")
                return

        name = input("Enter patron name: ")

        patron = Patron(patron_id, name)
        self.patrons.append(patron)

        print("Patron registered successfully!")

    def borrow_book(self):
        patron_id = input("Enter patron ID: ")
        book_id = input("Enter book ID: ")

        patron = None
        book = None

        # Find patron
        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if patron is None:
            print("Patron not found!")
            return

        # Find book
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if book is None:
            print("Book not found!")
            return

        # Check availability
        if not book.available:
            print("Book is already borrowed!")
            return

        book.available = False
        patron.borrowed_books.append(book)

        print("Book borrowed successfully!")

    def return_book(self):
        patron_id = input("Enter patron ID: ")
        book_id = input("Enter book ID: ")

        patron = None

        # Find patron
        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if patron is None:
            print("Patron not found!")
            return

        # Find borrowed book
        for book in patron.borrowed_books:
            if book.book_id == book_id:
                book.available = True
                patron.borrowed_books.remove(book)

                print("Book returned successfully!")
                return

        print("This book was not borrowed by this patron!")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n--- BOOKS ---")

        for book in self.books:
            status = "Available" if book.available else "Borrowed"

            print("Book ID:", book.book_id)
            print("Book Name:", book.name)
            print("Author:", book.author)
            print("Status:", status)
            print("--------------------")

    def display_patrons(self):
        if not self.patrons:
            print("No patrons registered.")
            return

        print("\n--- PATRONS ---")

        for patron in self.patrons:
            print("Patron ID:", patron.patron_id)
            print("Patron Name:", patron.name)

            if patron.borrowed_books:
                print("Borrowed Books:")

                for book in patron.borrowed_books:
                    print(" -", book.name, "(ID:", book.book_id + ")")
            else:
                print("Borrowed Books: None")

            print("--------------------")


# Create library object
library = Library()


# Main menu
while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.register_patron()

    elif choice == "3":
        library.borrow_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 7.")

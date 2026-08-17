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
        name = input("Enter book name: ")
        author = input("Enter author name: ")

        book = Book(book_id, name, author)
        self.books.append(book)

        print("Book added successfully!")

    def register_patron(self):
        patron_id = input("Enter patron ID: ")
        name = input("Enter patron name: ")

        patron = Patron(patron_id, name)
        self.patrons.append(patron)

        print("Patron registered successfully!")

    def borrow_book(self):
        patron_id = input("Enter patron ID: ")
        book_id = input("Enter book ID: ")

        for patron in self.patrons:
            if patron.patron_id == patron_id:

                for book in self.books:
                    if book.book_id == book_id:

                        if book.available:
                            book.available = False
                            patron.borrowed_books.append(book)
                            print("Book borrowed successfully!")
                        else:
                            print("Book is already borrowed!")

                        return

                print("Book not found!")
                return

        print("Patron not found!")

    def return_book(self):
        patron_id = input("Enter patron ID: ")
        book_id = input("Enter book ID: ")

        for patron in self.patrons:
            if patron.patron_id == patron_id:

                for book in patron.borrowed_books:
                    if book.book_id == book_id:
                        book.available = True
                        patron.borrowed_books.remove(book)

                        print("Book returned successfully!")
                        return

                print("This book was not borrowed by this patron!")
                return

        print("Patron not found!")


library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

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
        print("Thank you!")
        break

    else:
        print("Invalid choice!")


   
                       
               

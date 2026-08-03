#Design a Library Management System using object-oriented programming
#principles in Python. This system should manage books and patrons (library
#users), allowing for basic operations such as adding new books, registering
#patrons, borrowing books, and returning books.

class book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title = title
        self.author= author
        self.available = True

class patron:
    def __init__(self,name,patron_id):
        self.name=name
        self.patron_id=patron_id

class Liberary:
    def __init__(self):
        self.book=[]
        self.patron=[]

    def add_book(self,book):
        self.book.append(book)
        print("added sucessfully")

    def register(self,patron):
        self.patron.append(patron)
        print( "registered sucessfully")

    def borrow(self,patron_id,book_id):
        for p in self.patron:
            if p.patron_id==patron_id:
                for b in self.book:
                    if b.book_id==book_id:

                        if book.available == False:
                            print("borrowed ")
                        else:
                            print("not borrowed")

                            return("not available")
                            
    def ret(self,book_id):
        for b in self.book:
            if b.book_id==book_id:
                book.available=True
                print("book returned sucessfully")
            else:
                print("book not returned")

                return("not availale")


Liberary = Liberary ()  
b1 = book(111,"python","alberteinstine") 
b2 = book(112,"maths","aryabhatta")

Liberary.add_book(b1)
Liberary.add_book(b2)

p1 = patron("Aarya","ABC")

Liberary.register(p1)

Liberary.borrow(111,"ABC")
Liberary.ret("ABC")

        
        


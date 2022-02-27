class Library:

    def __init__(self, books, library_name) -> None:
        self.books = books
        self.library_name = library_name
        
    def displaybook(self, books):
        return books
    
    def addbook(self, books, newbook):
        books.append(newbook)

    def lendbook(self, book, lender_name):
        books.remove(book)
        self.lendername = lender_name
        
    def returnbook(self, book):
        books.append(book)
        
lends = []
lenders = []
books = ["Harry Potter", "The Alchemist", "Pschycology of Money", "Mnemonics"]
ParasLibrary = Library(books, "ParasLibrary")

while True:
    do = input("What you want to do displaybook(d) or addbook(a) or lendbook(l)  or returnbook(r) or Quit(q)? ")

    if do=="d":
        print(ParasLibrary.displaybook(books))

    elif do=="a":
        newbook = input("Which book you want to add? ")
        ParasLibrary.addbook(books, newbook)

    elif do=="l":
        whichbook = input("Which book you want? ")
        lendername = input( "What is your name? ")

        if whichbook in books:
            ParasLibrary.lendbook(whichbook, lendername)
            lends = [whichbook]
            lenders = [lendername]

        elif whichbook not in books:
            print(f"{whichbook} is not available in our library.")

    elif do=="r":
        whichbook = input("Which book you want to return? ")
        returnername = input("What is your name? ")

        if whichbook in lends and returnername in lenders:
            ParasLibrary.returnbook(whichbook)
            
        elif whichbook not in lends:
            print(f"This book was not lended by anyone. Lended books are {lends}.")
        elif returnername not in lenders:
            print(f"You have not lended any book from our lirary. Lenders are {lenders}")

    elif do=="q":
        break


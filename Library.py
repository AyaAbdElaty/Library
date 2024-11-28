class library:
    
    def __init__(self):
        self.booklist = [] #for the book list
        self.M_booklist = [] #for the book list after lowercase the letters
        self.name_of_library = ""   # for the name of the library
        self.lended_books = {}    # a dictionary to store the name of the user and the borrowed books
        self.book = ""           # the book name entered by the user
        self.Abook = ""          # for the book added by th user 
        self.name = ""           # for the user name
        
        
        
        
    def available_Books(self):          # for showcasing the available books
        self.M_booklist = [each.lower() for each in self.booklist]
        print(self.M_booklist)
    
    def books_lending(self):              # for showcasing all lended books with their user
        self.available_Books()
        self.book = input("please enter the book you want to borrow ")
        if self.book.lower() in self.M_booklist:
            self.name = input("please enter your name: ")
            
            if self.name.lower() in self.lended_books.keys():
                self.lended_books[self.name].append(self.book)
                
            
            else:  
                self.lended_books[self.name] = [self.book]
            self.z = self.M_booklist.index(self.book)
            self.booklist.pop(self.z)
            self.M_booklist.remove(self.book)
            print("your book is availble")
            print(self.lended_books)
            
                
        else:
            print("sorry your book isn't in our library")

    def add_book(self):        # to let the user add any book to the library
        self.available_Books()
        self.Abook = input("Enter the name of the book you want to add: ")
        if self.Abook.lower() in self.M_booklist:
            print("This book is already in the library")
        else:
            self.M_booklist.append(self.Abook)
            self.booklist.append(self.Abook)
            return self.M_booklist
    def borrowed_Book(self):          # To let the user return the borrowed book to the library
        self.newdic_lend = {}
        self.re_Books = input("Enter your Book name ")
        list_dicBook = self.lended_books.values()
        for each in list_dicBook:
            if self.re_Books in each:
                each.remove(self.re_Books)
            else: 
                print("sorry this book isn't in our borrowed list")
                
        print(list_dicBook)
        return (self.lended_books)
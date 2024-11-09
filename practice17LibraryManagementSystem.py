class library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]

    def countbooks(self, book):
        self.books.append(book)
        self.no_of_books=len(self.books)

    def showdetails(self):
        print(f"the total no of books in our library is {self.no_of_books}")
        print("\n")
        print("------------------------displaying all the books---------------------")
        
        
    
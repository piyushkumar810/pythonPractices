# --------------------------------------library management system------------------------------
# write a library class with no of books and books as two instance variable. write a program to create a library
# from the library class and show how you can print all the books add a boook and get the number of books 
# using different method. show that your program does not presist the book after the program is stopped.


class library:
    def __init__(self):
        self.noBooks=0
        self.Books=[]

    def addBook(self, book):
        self.Books.append(book)
        self.noBooks=len(self.Books)

    def showinfo(self):
        print(f"The library has total {self.noBooks} Books. and The books are : ")

        for i in self.Books:
            print(i)

l1=library()


l1.addBook("Ramayan")
l1.addBook("Mahabharat")
l1.addBook("Bhagavad gita")
l1.addBook("upanishad")
l1.addBook("Rigveda")
l1.addBook("samaveda")
l1.addBook("yajurveda")
l1.addBook("atharveda")


l1.showinfo()
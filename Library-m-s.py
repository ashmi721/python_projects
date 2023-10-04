''' write a library class with no_of_books and books as two instance variables. Write a program to create a library from this 
 class and show how you can print all books, add a book and get the number of books using different methods, show that your program doesn't persist the 
 books after the program is stopped!
'''
class library:
    def __init__(self):
        self.no_of_books = 0
        self.books=[]
    
    def add_book(self,book):
        self.books.append(book)
        self.no_of_books = len(self.books)


    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book) 
            self.no_of_books = len(self.books)

    def show_info(self):
        print(f"Number of books in the library are {self.no_of_books} :")
        for book in self.books:
            print(book)

l1 = library()
l1.add_book("Harry Potter")
l1.show_info()

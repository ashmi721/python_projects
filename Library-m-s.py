''' write a library class with no_of_books and books as two instance variables. Write a program to create a library from this 
 class and show how you can print all books, add a book and get the number of books using different methods, show that your program doesn't persist the 
 books after the program is stopped!
'''
class library:
    books = []

def __init__(self):
        self.no_of_books = len(self.books)

def print_all_books(self):
        for book in self.books:
            print(book)
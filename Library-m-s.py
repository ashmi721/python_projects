''' write a library class with no_of_books and books as two instance variables. Write a program to create a library from this 
 class and show how you can print all books, add a book and get the number of books using different methods, show that your program doesn't persist the 
 books after the program is stopped!
'''
class Library:
    def __init__(self):
        self.no_of_books = 0 # Initialize the number of books to 0
        self.books = {}       # Initialize the dictionary of books

    def add_book(self, book, category): # create add book funtion with two parameter
        self.books[book] = category  # add book with category in dectinary of books
        self.no_of_books += 1 # increment after the add the each book

    def remove_book(self, book): # create remove book funtion with one parameter
        if book in self.books: # cheek if remove book are available
            del self.books[book] # del required book
            self.no_of_books -= 1 # decrement after the remove the book

    def print_books(self): 
        print("Available books in the library are:",self.no_of_books) # display the no of books with name
        for book, category in self.books.items():
            print(f"{book} - {category}")

    def get_no_of_books(self):
        return self.no_of_books # it return the no of books

l1 = Library() # create an instance of the class
l1.add_book("Harry Potter", "Fantasy") # call the funtion with argument
print(f"Number of Initial books: {l1.get_no_of_books()}")

# enter the user requrement such as add, remove and quit
while True:
    print("Enter a book name (Enter 'a' to add, 'q' to quit, 'r' to remove get the total info):")
    choice = input()
    if choice == 'q':
        break
    elif choice == 'a':
        print("Enter a book name:")
        book = input()
        print("Enter the category of the book:")
        category = input()
        l1.add_book(book, category)
    elif choice == 'r':
        print("Enter the name of the book to remove:")
        book_to_remove = input()
        l1.remove_book(book_to_remove)

# diaplay the all books
l1.print_books()

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
        self.no_of_books += 1

    def remove_book(self, book):
        if book in self.books:
            del self.books[book]
            self.no_of_books -= 1

    def print_books(self):
        print("Available books in the library are:",self.no_of_books)
        for book, category in self.books.items():
            print(f"{book} - {category}")

    def get_no_of_books(self):
        return self.no_of_books

l1 = Library()
l1.add_book("Harry Potter", "Fantasy")
print(f"Number of Initial books: {l1.get_no_of_books()}")

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

l1.print_books()

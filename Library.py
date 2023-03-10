class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title.title()  # string with capitalised first letter
        self.author = author  # string
        self.dewey = dewey  # string
        self.isbn = isbn  # string
        self.available = True
        self.borrower = None
        book_list.append(self)  # Holds book objects as created - main routine

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.available)
        print(self.borrower)
        print(border)


class User:
    def __init__(self, name, address):
        self.name = name  # string
        self.address = address  # string
        self.fees = 0.0  # float
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print(f"Fees: ${self.fees:.2f}")
        print(border)


# Print list of books
def print_info():
    for book in book_list:
        book.book_details()


# Print list of users
def print_user():
    for user in user_list:
        user.user_details()


# Add a new library user
def add_user():
    name = input("Enter the new user's name: ").title()
    address = input("Enter the new user's address: ")
    User(name, address)
    print(name, address, "has been added to the user list")


# Add a new book
def add_book():
    title = input("Enter the new book's title: ").title()
    author = input("Enter the new book's author: ").title()
    dewey = input("Enter the new book's dewey code: ").upper()
    isbn = input("Enter the new book's ISBN: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")


# Find a user
def find_user():
    user_to_find = input("Enter the name of the user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")

# Main routine
book_list = []
user_list = []
border = "-" * 20

# Create objects - Books
Book("Lord of the Rings", "J.R.R.Tolkien", "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale Of Two Cities", "Charles Dickens", "DIC", "9781853262647")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

# Create objects - Users
User("John", "12 Example St")
User("Susan", "1011 Binary Rd")
User("Paul", "25 Appletree Dr")
User("Mary", "8 Moon Cres")


add_book()
print(border)
print_info()
# add_user()
# print_user()



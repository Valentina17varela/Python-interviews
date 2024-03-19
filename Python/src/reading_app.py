"""
Online Cloud Reading Application
(Like Kindle)

- Users have a library of books that they can add to or remove from
- Users can set a book from their library as active
- The reading app should keep track of the current page the user is on
- The reading app only displays 1 page at a time in the active book
"""


class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages


class User:
    def __init__(self, username):
        self.username = username
        self.library = []
        self.active_book = None  # Reference to the active book
        self.current_page = 1  # Current page the user is on

    def add_book_to_library(self, book):
        self.library.append(book)

    def remove_book_from_library(self, book):
        if book in self.library:
            self.library.remove(book)

    def set_active_book(self, book):
        if book in self.library:
            self.active_book = book
            self.current_page = 1  # Set current page to the first page


class ReadingApp:
    def __init__(self):
        self.users = {}

    def register_user(self, username):
        if username not in self.users:
            self.users[username] = User(username)
        else:
            print("User already registered.")

    def display_page(self, username):
        user = self.users.get(username)
        if user:
            if user.active_book:
                print(
                    f"Page {user.current_page} of {user.active_book.title} by {user.active_book.author}"
                )
            else:
                print("No active book set.")
        else:
            print("User not found.")

    def turn_page(self, username):
        user = self.users.get(username)
        if user:
            if user.active_book:
                if user.current_page < user.active_book.total_pages:
                    user.current_page += 1
                    print(f"Turned to page {user.current_page}")
                else:
                    print("You've reached the end of the book.")
            else:
                print("No active book set.")
        else:
            print("User not found.")


app = ReadingApp()
app.register_user("valentina17varela")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)

user1 = app.users["valentina17varela"]
user1.add_book_to_library(book1)
user1.add_book_to_library(book2)

user1.set_active_book(book1)
app.display_page(
    "valentina17varela"
)  # Output: Page 1 of The Great Gatsby by F. Scott Fitzgerald

app.turn_page("valentina17varela")  # Output: Turned to page 2
app.display_page(
    "valentina17varela"
)  # Output: Page 2 of The Great Gatsby by F. Scott Fitzgerald

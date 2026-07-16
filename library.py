import json

FILE_NAME = "books.json"


# ----------------------------
# Load Books
# ----------------------------
def load_books():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# ----------------------------
# Save Books
# ----------------------------
def save_books(books):
    with open(FILE_NAME, "w") as file:
        json.dump(books, file, indent=4)


# ----------------------------
# Add Book
# ----------------------------
def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")

    # Check duplicate ID
    for book in books:
        if book["id"] == book_id:
            print("\nBook ID already exists.\n")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(new_book)

    save_books(books)

    print("\nBook added successfully.\n")


# ----------------------------
# View Books
# ----------------------------
def view_books():

    books = load_books()

    if len(books) == 0:
        print("\nNo books found.\n")
        return

    print("\n========== BOOK LIST ==========\n")

    for book in books:

        status = "Available" if book["available"] else "Borrowed"

        print(f"""
Book ID    : {book['id']}
Title      : {book['title']}
Author     : {book['author']}
Status     : {status}
----------------------------------------
""")


# ----------------------------
# Search Book
# ----------------------------
def search_book():

    books = load_books()

    keyword = input("Enter Book Title: ").lower()

    found = False

    for book in books:

        if keyword in book["title"].lower():

            status = "Available" if book["available"] else "Borrowed"

            print(f"""
Book Found

Book ID : {book['id']}
Title   : {book['title']}
Author  : {book['author']}
Status  : {status}
""")

            found = True

    if not found:
        print("\nBook not found.\n")


# ----------------------------
# Borrow Book
# ----------------------------
def borrow_book():

    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            if book["available"]:

                book["available"] = False

                save_books(books)

                print("\nBook borrowed successfully.\n")

            else:

                print("\nBook is already borrowed.\n")

            return

    print("\nBook not found.\n")


# ----------------------------
# Return Book
# ----------------------------
def return_book():

    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            if not book["available"]:

                book["available"] = True

                save_books(books)

                print("\nBook returned successfully.\n")

            else:

                print("\nThis book was not borrowed.\n")

            return

    print("\nBook not found.\n")


# ----------------------------
# Delete Book
# ----------------------------
def delete_book():

    books = load_books()

    book_id = input("Enter Book ID: ")

    for book in books:

        if book["id"] == book_id:

            books.remove(book)

            save_books(books)

            print("\nBook deleted successfully.\n")

            return

    print("\nBook not found.\n")
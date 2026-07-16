from library import (
    add_book,
    view_books,
    search_book,
    borrow_book,
    return_book,
    delete_book
)


def display_menu():
    print("\n" + "=" * 40)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
    print("=" * 40)


def main():
    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            borrow_book()

        elif choice == "5":
            return_book()

        elif choice == "6":
            delete_book()

        elif choice == "7":
            print("\nThank you for using the Library Management System.")
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()
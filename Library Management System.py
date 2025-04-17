# Simple Library Management System

# A list to hold the books in the library
library_books = []

# Function to add a new book to the library
def add_book():
    book_title = input("Enter the title of the book: ")
    book_author = input("Enter the author of the book: ")
    library_books.append({'title': book_title, 'author': book_author})
    print(f'Book "{book_title}" by {book_author} added to the library.')

# Function to search for a book by title
def search_book():
    search_title = input("Enter the title of the book you want to search for: ")
    found_books = [book for book in library_books if search_title.lower() in book['title'].lower()]
    if found_books:
        print(f"Found books matching '{search_title}':")
        for book in found_books:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print(f"No books found with the title '{search_title}'.")

# Function to display the list of all books
def display_books():
    if library_books:
        print("Here is the list of books in the library:")
        for book in library_books:
            print(f"Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books available in the library.")

# Main function to run the system
def main():
    username = input("Enter your Under 25 App username: ")
    print(f"Hello {username}, welcome to your Library!")

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a new book")
        print("2. Search for a book")
        print("3. Display the list of books")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            display_books()
        elif choice == '4':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

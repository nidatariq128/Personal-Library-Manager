import json
import os

data_file = 'library.txt'

def load_library():
    """Load the library from a file."""
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    """Save the library to a file."""
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Add a new book to the library."""
    print("\nAdd a Book")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = input("Enter the publication year: ")
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == 'yes'
    
    new_book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    
    library.append(new_book)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    """Remove a book from the library."""
    print("\nRemove a Book")
    title_to_remove = input("Enter the title of the book to remove: ")
    initial_len = len(library)
    library[:] = [book for book in library if book['title'].lower() != title_to_remove.lower()]
    
    if len(library) < initial_len:
        print(f"Book '{title_to_remove}' removed successfully!")
    else:
        print(f"Book '{title_to_remove}' not found.")

def search_books(library):
    """Search for a book by title or author."""
    print("\nSearch for a Book")
    search_by = input("Search by (title/author): ").lower()
    search_term = input(f"Enter the {search_by}: ").lower()

    results = [book for book in library if search_term in book[search_by].lower()]
    if results:
        print(f"Matching Books:")
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")

def display_all_books(library):
    """Display all books in the library."""
    print("\nYour Library:")
    for index, book in enumerate(library, 1):
        status = "Read" if book['read'] else "Unread"
        print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_statistics(library):
    """Display library statistics."""
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"\nTotal books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    """Main program loop."""
    print("Welcome to your Personal Library Manager!")

    library = load_library()

    while True:
        print("\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


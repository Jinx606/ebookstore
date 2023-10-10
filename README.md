# Ebookstore Database Management

This Python script is designed to manage an ebookstore database using SQLite. It allows a clerk to perform various operations such as entering new books, updating book details, deleting books, and searching for books within the database.

## Prerequisites

Before running this script, ensure you have the following:

- Python installed on your system.
- The SQLite library for Python, which is typically included with Python installations.

## Getting Started

1. Clone the repository or download the script to your local machine.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Run the script using the following command:

   python ebookstore.py

Follow the on-screen menu prompts to perform various database management operations.

### Usage

## Menu Options

Enter Book (Option 1): Allows you to add a new book to the database by providing the book's ID, title, author, and quantity in stock.

Update Book (Option 2): Enables you to update the details of an existing book in the database. You can modify the book's title, author, and quantity.

Delete Book (Option 3): Allows you to remove a book from the database based on its ID.

Search Books (Option 4): Lets you search for a specific book in the database by providing its ID. It displays book details if found.

Exit (Option 0): Terminates the program.

## Notes

The database file is named ebookstore_db and is created in the same directory as the script.

The script uses SQLite to manage the database, and the database schema includes a book table with columns for ID, title, author, and quantity.

The script includes error handling to handle invalid input and database errors gracefully.

## Author

Jinx606

## Acknowledgments

Thanks to SQLite for providing a lightweight and efficient database engine.

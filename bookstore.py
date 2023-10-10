# Importing necessary library
import sqlite3

# Establishing a connection to the database I will be creating
db = sqlite3.connect('ebookstore_db')

# Creating a cursor object
cursor = db.cursor()

# Creating a table 'book' with the necessary columns and their attributes. Using ID as the Primary Key.
cursor.execute(''' CREATE TABLE IF NOT EXISTS book (
                   id INTEGER PRIMARY KEY NOT NULL,
                   title TEXT NOT NULL,
                   author TEXT NOT NULL,
                   qty INTEGER NOT NULL
)''')

# Saving the changes
db.commit()

# Populating the table with the given records and ignoring if they already exist
cursor.execute('''INSERT OR IGNORE INTO book (id, title, author, qty)
                  VALUES (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
                         (3002, "Harry Potter and the Philospher's Stone", 'J.K. Rowling', 40),
                         (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
                         (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
                         (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)''')

#Saving the changes made and closing the connection
db.commit()
db.close()


# Defining functions for the different menu options. Starting with a validation for integers where they are needed using .isdigit
def get_valid_integer(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        print("Invalid input. Please use a number as your input.")
        

# Defining enter_book. General error exceptions are made
def enter_book(id, title, author, qty):
    try:
        db = sqlite3.connect('ebookstore_db')
        cursor = db.cursor()
        cursor.execute(''' INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)''', (id, title, author, qty))
        print(f"{title}, by {author}, with a quantity of {qty} in stock. Successfully added.\n")
        db.commit()
    except Exception as e:
        print(print("An error has occurred while entering this book. Please ensure all details are correct."))    
        db.rollback()
        raise e
    finally:
        if db:
            db.close()
 

# Defining update book and adding error exceptions
def update_book(id, title, author, qty):
    try:
        db = sqlite3.connect('ebookstore_db')
        cursor = db.cursor()
        cursor.execute(''' UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?''',(title, author, qty, id))
        print(f"{title}, by {author} with ID {id} and a quantity of {qty} in stock. Successfully updated.\n")
        db.commit()
    except Exception as e:
        print("An Error has occurred while attempting the update. Please ensure all details are correct", e)
        db.rollback()
        raise e
    finally:
        if db:
            db.close()


# Defining delete book and adding a general error exception
def delete_book(id, title, author):
    try:
        db = sqlite3.connect('ebookstore_db')
        cursor = db.cursor()
        cursor.execute(''' DELETE FROM book WHERE id = ?''',(id,))
        print(f"{title}, by {author} and ID of {id} successfully deleted.\n")
        db.commit()
    except Exception as e:
        print("An error has occurred during deletion of this book. Please ensure all details are correct.")
        db.rollback()
        raise e
    finally:
        if db:
            db.close()


# Defining Search books adding the ability to display all books
def search_books(id):
    try:
        db = sqlite3.connect('ebookstore_db')
        cursor = db.cursor()
        cursor.execute(''' SELECT * FROM book WHERE id = ?''',(id,))
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
        if not books:
            print("Book Not Found")        
    except Exception as e:
        print("An error has occurred.", e)
    finally:
        if db:
            db.close()

# Defining a function ro display books to make the search, update and delete options more user friendly and error exceptions are made
def display_books():
    try:
        db = sqlite3.connect('ebookstore_db')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM book''')
        books = cursor.fetchall()
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
        db.close()
    except Exception as e:
        print("An Error has occured displaying all books:", e)
        
                
# Welcoming the clerk to the program and presenting them with a menu to choose from.
print("Welcome to your ebookstore database. Let's get started on what you would like to do.")


# Setting the valid range for menu integers
valid_range = [0, 1, 2, 3, 4]

# Defining a menu for the clerk to choose from and receiving their input. The 'isdigit' prevents letters used instead of integers in the menu
def clerk_menu():
    print('''\nMain menu\n1. Enter Book
2. Update Book
3. Delete Book
4. Search Books
0. Exit''')
    choice = get_valid_integer("\nPlease enter your choice from 1 to 4 or press 0 to Exit the program.\n")
    while choice not in valid_range:
        print("Invalid menu choice. Please select a valid option from the menu.")
        choice = get_valid_integer("\nPlease enter your choice from 1 to 4 or press 0 to Exit the program.\n")

    return choice

# Starting a While loop to iterate through the menu choices
while True:
    choice = clerk_menu()
    
    # If user chooses to enter a book, adding exceptions for if the ID or QTY are letters instead of integers
    if choice == 1:
        id = get_valid_integer("Please enter the book ID:\n")
        title = input("Please enter the book title:\n")
        author = input("Please enter the author of the book:\n")
        qty = get_valid_integer("Please enter the quantity of the book in stock:\n")
        enter_book(id, title, author, qty)
        
    # If user chooses to update a book, this will display all books first for the user to make the correct choice in which book to update
    elif choice == 2:
        print("The books you have in stock are:\n")
        display_books()
        id = get_valid_integer("\nPlease enter the ID of the book you would like to update:\n")
        title = input("Please enter the new title of the book or rewrite the current title if there is no change:\n")
        author = input("Please enter the new author's name or rewrite the author's name if there is no change:\n")
        qty = get_valid_integer("Please enter the quantity of the book in stock:\n")
        update_book(id, title, author, qty)
        
    # If user chooses to delete a book, this will display all the books first in order for the user to make the correct choice
    elif choice == 3:
        print("The books you have in stock are:\n")
        display_books()
        id = get_valid_integer("\nPlease enter the ID of the book you would like to delete:\n")
        delete_book(id, title, author)
        
    # If the user chooses to search for a book, adding exceptions for titles not found as well as the general error of a book not being found.
    elif choice == 4:
        print("The books you have in stock are:\n")
        display_books()
        id = get_valid_integer("\nPlease enter the ID of the book you would like to search for:\n")
        search_books(id)
        
    # If the user chooses to exit the program it ends with a message and with break.
    elif choice == 0:
        print("You are now exiting the program. Have a nice day!")
        break
import booksSDK
from book import Book

def print_menu():
    print("""Choose an option whit num:
    1. print all books
    2. add a book
    3. update a book
    4. delete a book
    5. deleted a book seperately (by rowid although you dont know row id)
    6. check existence of book
    7. count of books
    8. borrow a book
    9. return a book
    10. take sorted list of books (by title)
    """)

def print_seperately_menu():
    print("""what do you know about book?
    1- Row id
    2- title
    3- author
    4- nothing  
    """)

while True:
    print()
    print_menu()
    resp = input()
    response = int(resp) if resp.isdigit() else None

    if response == 1:
        print("Printing all books")
        for rowid, book in booksSDK.get_books():
            print(f"{rowid} : {book}")

    elif response == 2:
        print("What is the name of book?")
        title = input()

        print("Who is the author of the book?")
        author = input()

        print("Is it available? (True/False)")
        available = input()
        book = Book(title, author, available)

        booksSDK.add_book(book)
        print("book added")

    elif response == 3:
        print("what is the current title?")
        old_book_title = input()

        print("what is the current author of book?")
        old_book_author = input()

        print("what is the current available of book? (True/False)")
        old_book_available = input()

        old_book = Book(old_book_title, old_book_author, old_book_available)

        print("what is the new title?")
        new_book_title = input()

        print("what is the new author of book?")
        new_book_author = input()

        print("what is the new available of book? (True/False)")
        new_book_available = input()

        new_book = Book(new_book_title, new_book_author, new_book_available)

        
        print(booksSDK.update_book(new_book, old_book))
    

    elif response == 4:
        print("what is the name of book?")
        title = input()
        print("what is the author of book?")
        author= input()
        print("what is the available of book?")
        available = input()
        book = Book(title, author, available)
        print(booksSDK.delete_book(book))

    elif response == 5:
        print_seperately_menu()
        resp2 = input()
        response2 = int(resp2) if resp2.isdigit() else None
        
        if response2 == 1: #G
            print("what is the id?")
            rowid = int(input())
            print(booksSDK.delete_book_by_rowid(rowid))

        elif response2 == 2:
            print("What is the title?")
            title = input()
            rowid = booksSDK.taking_rowid_by_title(title)
            print(booksSDK.delete_book_by_rowid(rowid))

        elif response2 == 3:
            print("What is the author?")
            author = input()
            rowid = booksSDK.taking_rowid_by_author(author)
            print(booksSDK.delete_book_by_rowid(rowid))

        elif response2 == 4:
            print("Please go to hell :)")
        else:
            print("we cant understand please again")
        
    elif response == 6:
        print("what is the name of book?")
        title = input()
        print("what is the author of book?")
        author= input()
        
        book = Book(title, author, None)
        if booksSDK.is_book_exist(book):
            print("Book exists")
        else:
            print("Book does not exist")
    
    elif response == 7:
        print("Total number of books:", booksSDK.count_books())

    elif response == 8:
        print("what is the name of book?")
        title = input()
        print("What is the author of book?")
        author= input()
        book = Book(title, author, None)
        print(booksSDK.borrow_book(book))

    elif response == 9:
        print("what is the name of book?")
        title = input()
        print("What is the author of book?")
        author= input()
        book = Book(title, author, None)
        print(booksSDK.return_book(book))
      
    elif response == 10:
        print("Taking sorted list of books by title")
        for rowid, book in booksSDK.sorted_books_by_title():
            print(f"{rowid} : {book}")


    else:
        print("Thanks for using our app")
        break
    
    
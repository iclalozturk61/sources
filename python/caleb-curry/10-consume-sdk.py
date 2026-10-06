#84 - Creating a Library Console App & 85 - Updating and Deleting Books through Console App**************** 85 ile güncellencek
import booksSDK
from book import Book

def print_menu():
    print("""Choose an option whit num:
    1. print all books
    2. add a book
    3. update a book
    4. delete a book
    5. deleted a book seperately (by rowid although yo dont know row id)
    """)

def print_seperately_menu():
    print("""what do you know about book?
    1- Row id
    2- title
    3- pages
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

        print("How many pages is the book?")
        pages = int(input())

        book = Book(title, pages)

        booksSDK.add_book(book)
        print("book added")

    elif response == 3:
        print("what is the current title?")
        old_book_title = input()

        print("what is the current number of pages?")
        old_book_pages = input()

        old_book = Book(old_book_title, old_book_pages)

        print("what is the new title?")
        new_book_title = input()

        print("what is the new number of pages?")
        new_book_pages = input()

        new_book = Book(new_book_title, new_book_pages)

        print("books were updated")
        print(booksSDK.update_book(new_book, old_book))
    

    elif response == 4:
        print("what is the name of book?")
        title = input()
        print("what is the number of pages?")
        pages= input()
        book = Book(title, pages)
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
            print("What is the pages?")
            pages = input()
            rowid = booksSDK.taking_rowid_by_pages(pages)
            print(booksSDK.delete_book_by_rowid(rowid))

        elif response2 == 4:
            print("Please go to hell :)")
        else:
            print("we cant understand please again")
        
        


    else:
        print("Thanks for using our app")
        break
import sqlite3
from book import Book

#bookSDK.py ile her işimiz bittiğinde cursor bağlantısını kapatacak fonksyon: ŞÜPHELİ
def cursor():
    return sqlite3.connect('books.db').cursor()

c = cursor()
c.execute('CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, available BOOLEAN)')
c.connection.close()

def add_book(book): #book nesnesi alacak parametre olarak
    c = cursor()
    
    with c.connection:
        c.execute('INSERT INTO books VALUES (?, ?, ?)', (book.title, book.author, book.available))
    c.connection.close()

    return c.lastrowid

def get_books():
    c = cursor()
    books = []

    with c.connection:
        for book in c.execute('SELECT rowid, title, author, available FROM books'): #book her seferinde bir satırı alacak kendine ve book[0]=rowid book[1]=title book[2]=author book[3]=available
            books.append((book[0], Book(book[1], book[2], book[3]))) #title ı ve pages i Book sınıfına veriyor ordan nesne üretiyor. Nesneleri de books listesinde topluyor
    c.connection.close()
    return books

def get_books_by_title(title):
    c = cursor()

    with c.connection:
        c.execute('SELECT * FROM books WHERE title=?', (title,)) #değişkenleri böyle veriyoruz syntax böyle
    data = c.fetchone() #titleın olduğu satırı tuple dönecek, eşleşme olmazsa bulamazda None atar
    c.connection.close()
    
    if not data: #tuple lar boşsa False döner
        return None
    
    return(Book(data[0], data[1], data[2])) #title, author, available

def delete_book(book):
    c = cursor()
    
    with c.connection:
        c.execute('DELETE FROM books WHERE title=? AND author=? AND available=?', (book.title, book.author, book.available))
    deleted_count = c.rowcount
    c.connection.close()
    
    if deleted_count == 0:
        return "book not found"
    
    return f"The Number of deleted books: {c.rowcount}"

def delete_book_by_rowid(rowid):
    c = cursor()

    with c.connection:
        c.execute('DELETE FROM books WHERE rowid=?', (rowid,))
    
    c.connection.close()

    return "Silme işlemi tamamlandı" #c.lastrowid olsaydı burda: silme ve updata işlemlerinden sonra rowid 0 gelir kullanmak pek mantıklı değil hep 0 döner

def update_book(new_book, old_book):
    c = cursor()

    with c.connection:
        c.execute('UPDATE books SET title=?, author=?, available=? WHERE title=? AND author=? AND available=?', 
                 (new_book.title, new_book.author, new_book.available,  old_book.title, old_book.author, old_book.available))
        num_of_updated = c.rowcount
    c.connection.close()

    if num_of_updated == 0:
        return "Book not found"

    return "new book updated"

def taking_rowid_by_title(title):
    c = cursor()

    with c.connection:
        c.execute('SELECT rowid FROM books WHERE title=?', (title,))
        rowid = c.fetchall()

        if len(rowid) == 1:
            rowid = rowid[0][0]
        else:
            c.execute('SELECT rowid, title FROM books WHERE title=?', (title,))
            result = c.fetchall()
            print("Which one is yours please give me a row id?") 
            for row in result:
              print("rowid:", row[0], "title:", row[1])
            rowid = int(input())
    c.connection.close()

    return int(rowid)  

def taking_rowid_by_author(author):
    c = cursor()

    with c.connection:
        c.execute('SELECT rowid, author FROM books WHERE author=?', (author,))
        rowid = c.fetchall()

        if len(rowid) == 1:
            return rowid[0][0]
        else:
            c.execute('SELECT rowid, author FROM books WHERE author=?', (author,)) 
            result = c.fetchall()
            print("Which one is yours please give me a row id?")
            for row in result:
                print("rowid:", row[0], "author:", row[1])
            rowid = int(input())
    c.connection.close()

    return int(rowid)    


def is_book_exist(book):
    c = cursor()

    with c.connection:
        c.execute('SELECT available FROM books WHERE title=? AND author=?', (book.title, book.author))
        data = c.fetchone()
    c.connection.close()

    if data:
        return True
    else:
        return False
    
def count_books():
    c = cursor()
    with c.connection:
        c.execute('SELECT COUNT(*) FROM books')
        count = c.fetchone()[0]
    c.connection.close()
    return count

def borrow_book(book):
    c = cursor()

    with c.connection:
        c.execute('UPDATE books SET available=? WHERE title=? AND author=?', (False, book.title, book.author))
        num_of_updated = c.rowcount
    c.connection.close()

    if num_of_updated == 0:
        return "Book not found or not available"

    return "Book borrowed successfully"

def return_book(book):
    c = cursor()

    with c.connection:
        c.execute('UPDATE books SET available=? WHERE title=? AND author=? AND available=?', (True, book.title, book.author, False))
        num_of_updated = c.rowcount
    c.connection.close()

    if num_of_updated == 0:
        return "Book not found or not borrowed"

    return "Book returned successfully"

def sorted_books_by_title():
    c = cursor()
    books = []

    with c.connection:
        for book in c.execute('SELECT rowid, title, author, available FROM books ORDER BY title ASC'):
            books.append((book[0], Book(book[1], book[2], book[3])))
    c.connection.close()
    return books
# 76 - Intro to SQLite and Creating a Database
"""
Veritabanı (Database)
Tanım: Verilerin düzenli bir şekilde saklandığı ve yönetildiği sistem.

Avantajları:
    -Veriler güvenli tutulur.
    -Hızlı erişim ve sorgulama yapılır.
    -Aynı anda birçok kişi kullanabilir.

Türleri:
İlişkisel Veritabanı (RDBMS): Tablolar ve satır-sütun yapısı vardır (ör. SQL Server, MySQL, SQLite, PostgreSQL).
NoSQL Veritabanı: Daha esnek, genelde JSON benzeri yapı kullanır (ör. MongoDB, Firebase).

SQL ve SQLite Farkları
Özellik                     	SQL	                                                                                                SQLite
Ne olduğu	        Bir dil (Structured Query Language)	                                                                Bir veritabanı yönetim sistemi (RDBMS)
Görev	            Veritabanında veri tanımlama, ekleme, silme, sorgulama için kullanılan standart dil	                Verileri saklayan, yöneten ve SQL diliyle kullanılan bir yazılım
Kullanım alanı	    SQL dili MySQL, PostgreSQL, SQL Server, Oracle, SQLite vb. tüm RDBMS’lerde geçerli	                Mobil uygulamalar, küçük projeler, gömülü sistemler (tek dosya üzerinde çalışır)
Kurulum	            SQL tek başına kurulmaz, sadece dildir	                                                            SQLite kurulumsuz, tek dosya ile çalışır
Dosya yapısı	    SQL sadece komut kümesi olduğu için dosya oluşturmaz	                                            Veritabanını .db uzantılı tek bir dosyada tutar
Ölçeklenebilirlik	Büyük veritabanlarında güçlüdür (örn. SQL Server, MySQL)	                                        Küçük-orta boyutlu projeler için uygundur, çok büyük sistemlerde yetersiz kalır

Database i nerede tutarız?
    -SQL Server, MySQL gibi sistemler sunucuda (server) çalışır.
    -SQLite ise tek bir dosyada (.db) veritabanını tutar.

Disk tabanlı veritabanı (kalıcı)
    Veriler dosyalara veya özel formatlara yazılır.
    Örn: MySQL, SQL Server(sunucuda tutalar ama o da disk tabanlı sonuçta), PostgreSQL, SQLite (normal kullanımda .db dosyasında saklar). 

Memory tabanlı veritabanı (geçici)
    Veriler RAM’de tutulur. Sistem kapanınca gider.
    Örn: SQLite’ın :memory: modu, Redis, Memcached.

-- Bellekte veritabanı oluşturma
sqlite3 :memory:
-- Normal dosyada veritabanı oluşturma
sqlite3 mydata.db
"""

import sqlite3

conn = sqlite3.connect(":memory:") #conn = Veritabanı bağlantısı.
#conn = sqlite3.connect("example.db") eğer böyle yazsaydık dosyada veritabanımızı oluşturmuk olurduk verileri kalıcı hala getirirdik
# python terminal hangi klasör içindeyse oraya koyar db dosyasını, py dosyasının nerede olduğunun bir önemmi yok

#cursor() = O bağlantı üzerinden SQL sorgusu çalıştırmak ve sonuçları almak için kullanılan nesne.
c = conn.cursor()

#77 - Create a SQLite Table in SQLite
"""
c.execute(...)
    c, bir cursor nesnesidir. Yani veritabanına SQL komutları gönderen aracı.
    .execute(...) metodu, SQL komutunu çalıştırır.

EĞER DAHA ÖNCEDEN ÜRETİLMEMİŞSE TABLO ÜRET, tablonun adı books olsun, title adında bir sutun olsun İÇİNDEKİ VERİ TİPİ DE TEXT OLSUN, pages adında bir sutun olsun İÇİNDEKİ VERİ TİPİ DE INTEGER OLSUN.

+-------------------------+--------+
| title                  | pages  |
+-------------------------+--------+
|                         |        |
|                         |        |
|                         |        |
+-------------------------+--------+
"""
import sqlite3

conn = sqlite3.connect(":memory:")

c.execute('''CREATE TABLE IF NOT EXISTS books 
          (title TEXT, pages INTEGER) ''')  

#78 - Insert Data to Database in Python

import sqlite3

conn = sqlite3.connect(":memory:")

c.execute('''CREATE TABLE IF NOT EXISTS books 
          (title TEXT, pages INTEGER) ''')  

c.execute('INSERT INTO books(title) VALUES ("Beyoğlu\'nun en güzel abisi")') #books tablosunun title sutununa "Beyoğlu'nun en güzel abisi" verisini EKLE
conn.commit()

c.execute('INSERT INTO books VALUES ("Beyoğlu\'nun en güzel abisi", 456)') #title belirtmeden de veri verebiliriz
#c.execute(...) ile tabloya yeni satır eklendi ama bu işlem henüz veritabanına kalıcı olarak yazılmadı, sadece geçici bellekte (transaction içinde) tutuluyor.
#conn.commit() çalıştırıldığında bu değişiklikler kalıcı hale geliyor, yani veritabanına gerçekten kaydediliyor.

# 79 - Retrieve Database Data in Python
import sqlite3

conn = sqlite3.connect(":memory:")

c.execute('''CREATE TABLE IF NOT EXISTS books 
          (title TEXT, pages INTEGER) ''')  

c.execute('INSERT INTO books VALUES ("Beyoğlu\'nun en güzel abisi", 456)') 
conn.commit()


c.execute('SELECT title FROM books')
data = c.fetchone()
print("79-2- ", data)  #fethcone en yukardan başlar sırayla bir alt satırdaki veriyi verir

data = c.fetchone()
print("79-2- ", data)

data = c.fetchone()
print("79-2- ", data)

data = c.fetchone()
print("79-2- ", data) #veriler biterse boş satıra gelirse None döner

data = c.fetchone()
print("79-2- ", data)

c.execute('SELECT * FROM books') #HER ŞEYİ (* ile) AL books kütüphanesinden: * yapınca her şeyi seçmiş olursun
data = c.fetchone()
print("79-3- ", data)

books = { #tuple türünde(parantez içinde, birden fazla veri içeren değişmez) veriler tutan bir set
    ("Kavim", 400),
    ("Agatha\'nın anahtarı", 152),
    ("Korkuyu Beklerken", 202)
}
c.executemany('INSERT INTO books VALUES (?, ?)', books)
conn.commit()

c.execute('SELECT * FROM books ') 
print("79-3- ", data)

c.execute('SELECT * FROM books WHERE title="Agatha\'nın anahtarı"') #WHERE: sadece title sütunu "Agatha'nın anahtarı" olan satırları seçer.
data = c.fetchall()

print("79-3- ", data)
print(type(books))

"""
1. fetchone()
    Bir sonraki satırı getirir. Her çağrıldığında bir satır döner, yoksa None döner. Genellikle döngüyle kullanılır.

2. fetchmany(size)
    Belirttiğin size kadar satırı liste olarak getirir. Eğer o kadar satır yoksa, kalan kadar döner. Bellek dostudur, büyük veri setlerinde idealdir.

3. fetchall()
    Tüm kalan satırları getirir. Sonuçları bir liste içinde döner. Küçük veri setlerinde hızlı ve pratiktir.    


Metod	            Dönen veri tipi	                Açıklama
fetchone()	    Tek tuple	                    Sadece ilk satırı döner
fetchmany(n)	Liste içinde n adet tuple	    İlk n satırı döner
fetchall()	    Liste içinde tüm tuple’lar	    Tüm satırları döner
"""

#80 - Delete Database Data in Python
import sqlite3

conn = sqlite3.connect(":memory:")

c.execute('''CREATE TABLE IF NOT EXISTS books 
          (title TEXT, pages INTEGER) ''')  

c.execute('INSERT INTO books VALUES ("Beyoğlu\'nun en güzel abisi", 456)') 
conn.commit()

books = { 
    ("Beyoğlu\'nun en güzel abisi", 456),
    ("Beyoğlu\'nun en güzel abisi", 456),
    ("Beyoğlu\'nun en güzel abisi", 456),
    ("Kavim", 400),
    ("Agatha\'nın anahtarı", 152),
    ("Korkuyu Beklerken", 202)
}
c.executemany('INSERT INTO books VALUES (?, ?)', books)
conn.commit()

c.execute('SELECT rowid, title FROM books') #böylelikle hepsinin satır numarasını öğrenebiliriz
data = c.fetchall()
print("80-1- ", data)

c.execute('DELETE FROM books WHERE rowid=2') #2. satırı bütün verileri ile beraber sildik
conn.commit()

c.execute('SELECT rowid, title FROM books') 
print("80-2- ", data)

c.execute('DELETE FROM books WHERE title="Beyoğlu\'nun en güzel abisi"') #title değeri "Beyoğlu\'nun en güzel abisi" olan bütün verileri seçti sildi(bütün satırı)
conn.commit()

c.execute('SELECT * FROM books')
data = c.fetchall()
print("80-3- ", data)
"""
SQLite rowid’leri yeniden kullanmaz. 
    Yeni eklenen satır rowid=4 olur. Y
    ani rowid=2 sonsuza dek boş kalır (ta ki tablo yeniden oluşturulana kadar).
"""

#81 - Update SQLite Data in Python
c.execute('UPDATE books SET title="Yeni Kitap" WHERE rowid=4') #silinen id leri unutmamak lazım
c.execute('UPDATE books SET title="New book" WHERE rowid=5')
c.execute('UPDATE books SET title="Esir şehrin insanları" WHERE rowid=6')

conn.commit()
conn.close()

c.execute('SELECT * FROM books')
data = c.fetchall()
print("81-1-", data)

c.execute('SELECT rowid,  title FROM books') # virgül önemli onsuz sadece rowidi yazar
data = c.fetchall()
print("81-2- ", data)

#82 - Create an SDK - Part 1
"""
📌 Creating SDK (SQLite bağlamında)

- SDK = Software Development Kit (Yazılım Geliştirme Kiti).
- Bir SDK, başka geliştiricilerin bir sistemi/servisi kolayca 
  kullanabilmesi için hazırlanmış kütüphane, fonksiyon ve doküman paketidir.

🔹 SQLite için "Creating SDK" ne demek?
- SQLite'i direkt kullanmak yerine, üzerine kolaylaştırıcı bir katman yazmak.
- Örn: get_books(), add_book(title, pages), delete_book(id) gibi hazır fonksiyonlar.
- Böylece geliştirici SQL sorgularıyla uğraşmaz, SDK fonksiyonlarını çağırarak işler.

👉 Python'daki sqlite3 modülü zaten basit bir SDK gibidir.
👉 Android'de "Room Library" SQLite için bir SDK örneğidir.
"""
import booksSDK
from book import Book

book = Book("Sivrisinek Şehirde", 184)

print("82-1- ", booksSDK.add_book(book))
print("82-2- ", booksSDK.get_books())
print("82-3- ", booksSDK.get_books_by_title("Sivrisinek Şehirde"))
print(c.lastrowid)
print("82-4- Silinen kitap sayısı:", booksSDK.delete_book_by_title("Sivrisinek Şehirde"))

booksSDK.add_book(book)
booksSDK.add_book(book)
booksSDK.add_book(book)
booksSDK.add_book(book)

for rowid, book in booksSDK.get_books(): #tuple şeklinde gelen veriyi parçalıyor ve rowid yi ve nesneyi alıyor
    print("82-5- ", f"Satır: {rowid} - {book}")

print("82-5-* ", booksSDK.delete_book_by_rowid(rowid))

for rowid, book in booksSDK.get_books():
    print("82-6- ", f"Satır: {rowid} - {book}")

booksSDK.update_book_by_title("Sivrisinek Şehirde", "Kürk Mantolu Madonna")  #ne kadar Sivrisinek Şehirde varsa hepsini değiştirir

for rowid, book in booksSDK.get_books():
    print("82-7- ", f"Satır: {rowid} - {book}")

print("82-4- Silinen kitap sayısı:", booksSDK.delete_book_by_title("Kürk Mantolu Madonna"))
booksSDK.add_book(book)


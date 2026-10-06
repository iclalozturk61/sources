#71 - Passing by Object Reference
class Book():

    def __init__(self, title, pages=None): 
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} is {self.pages} pages long"
    
    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        return False
    
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)

book1 = Book("Asiye Kovun Beni", 144)
book2 = Book("Asiye Kovun Beni", 144)
book3 = book1 

print("71-1- ", book1 == book2) 
print("71-2- ", id(book1) == id(book2), id(book1) == id(book3)) #1 ile 3 aynı 2 faklı
print("71-3- ", book1 is book3)

"""
id():
    -Her nesne bellekte bir yerde tutulur.
    -id() o nesnenin nerede yaşadığını söyler.
    -Aynı nesne → aynı id
    -Farklı nesne → farklı id

book1 is book3:
Bu ifade, iki değişkenin bellekte aynı nesneye mi işaret ettiğini kontrol eder. Yani:
    == → içerik eşit mi? (__eq__ ile tanımlanır)
    is → kimlik aynı mı? (bellek adresi aynı mı?)
"""
print("71-4- ", id(book2))

def doSomething(book2):
    print("71-5- ", id(book2))
    book2.title = "yeni bir kitap" #title ına erişip değiştirmek nesnenin konumunu bozmaz yeni bir neesne üretmedik
    print("71-6- ", id(book2)) #bu printte aynı sonucu alıyoruz. 
    book2 = Book("something new", 72) #REPLACE = book2 = ... fonksiyon içinde yeni bir nesne yaratır → id değişir. Burada daha fazla bu isimle eskisine erişemeyiz kayboldu ama fonksyon dışında erişebiliriz
    print("71-7- ", id(book2)) #bu printtten de anlıyoruz ki yerel book2 değişmiş

doSomething(book2)

print("71-8- ", book2, id(book2)) #eeen baştaki book2 nin içeriği değişti book2.title yüzünden ama adresi değişmedi 
#çünkü fon. içinde yeni nesne ürettip onu başka isim içine atadık

"""
Pass by Object Reference" ne demek?

Not: reference(Teknik Tanım): bilgi parçasının nerede saklandığını tanımlayan kod

Python’da bir değişkeni bir fonksiyona gönderdiğinde, o değişkenin bellekteki adresi (referansı) gönderilir. Yani:
    -Fonksiyon, orijinal nesneye erişir — bir kopyasına değil.
    -Bu davranışa bazen "pass by reference" denir ama Python’da teknik olarak:
    -"Pass by object reference" veya "pass by assignment" daha doğru.
    
book2.title = ... → orijinal nesneye erişim, id değişmez
book2 = Book(...) → yeni bir nesne yaratılır, ve book2 artık bu yeni nesneyi gösterir

Ama bu değişiklik sadece fonksiyon içindedir. Dışarıdaki book2 hâlâ eski nesneyi gösterir.

Fonksiyona book2 gönderildi → bu, orijinal nesnenin adresi
    book2.title = ... → orijinal nesneye doğrudan müdahale
    Bu yüzden dışarıdaki book2.title da değişmiş olur
    
Ama neden id(book2) değişmedi?
    Çünkü sen henüz yeni bir nesne yaratmadın. Sadece var olan nesnenin içeriğini değiştirdin. 
    id() sadece nesne kimliğini gösterir, içeriği değil.
"""

#72 - File IO - Reading and Writing to .txt File
"""
'a' → Append Mode (ekleme modu)
    -Dosya varsa, sonuna ekleme yapar.
    -Dosya yoksa, yeni dosya oluşturur.
    -Mevcut içerik silinmez.
    -Yazdığın veri, dosyanın sonuna eklenir.

'w' → Write Mode (yazma modu)
    -Dosya varsa, içeriği tamamen silinir.
    -Dosya yoksa, yeni dosya oluşturur.
    -Yazdığın veri, dosyayı baştan yazar.
"""
class Book():

    def __init__(self, title, pages=None): 
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False

    def __str__(self):
        return f"{self.title} is {self.pages} pages long"
    
    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        return False
    
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)
    
open("input.txt", 'a')
file = open("input.txt", 'w')
file.write("Kavim\t382\n")
file.write("Agatha'nin Anahtari\t152")
file.close()

file = open("input.txt", 'r')
data = file.read().split('\n')
file.close()

book1_data = data[0].split('\t') #tablara göre ayrım
print("71-1- ", book1_data)
book1 = Book(book1_data[0], book1_data[1])

book2 = Book(data[1].split('\t')[0], data[1].split('\t')[1]) #yukarıdakinin aynısı daha kısa sadece

print("71-3- ", book1)
print("71-4- ", book2)

"""
Eğer  kolay bir şeyler yapıyorsak .txt dosyaları kullanabiliriz. Veri tabanı şart değil.

Dosya kapatılmazsa ne olur?
1. Bellek ve kaynak sızıntısı (resource leak)
    -Açılan dosya sistemde bir kaynak (file descriptor) tutar.
    -Kapatılmazsa bu kaynak serbest bırakılmaz → sistemde birikmeye başlar.
    -Çok sayıda dosya açılırsa, işletim sistemi “dosya sınırına” ulaşır → yeni dosya açamazsın.

2. Veri yazımı tamamlanmayabilir
    -Özellikle 'w', 'a' gibi yazma modlarında:
    -Python veriyi önce buffer’a yazar.
    -file.close() çağrılmazsa → buffer’daki veri dosyaya tam yazılmayabilir.
    -Sonuç: dosyada eksik veya bozuk veri olabilir.

3. Dosya kilitlenebilir (özellikle Windows’ta)
    -Dosya açık kaldığı sürece başka bir program tarafından erişilemeyebilir.
    -Örneğin: VS Code, Excel veya başka bir script dosyayı açamaz → “file is in use” hatası alırsın.

4. Beklenmeyen davranışlar ve hata mesajları
    -Kodun ilerleyen satırlarında dosya ile işlem yapmaya çalışırsan → ValueError: I/O operation on closed file gibi hatalar alabilirsin.
    -Ya da tam tersi: dosya hâlâ açık sanılır ama içerik güncellenmemiştir.
"""

#73 - Intro to Exception Handling
"""
Olay veritabanları ve dosya okumalara geldiğinde, 
    Hata mesajında açıkça verilerin yazması güvenlik açığı oluşturabilir. 
    Bunun için kullanıcılara özel hata mesajları tanımlanır

İyi yazılımcı ne yapar?
    -Hata olasılığı olan kodu izole eder
    -try bloğunu küçük tutar → sadece riskli satırları kapsar
    -Spesifik hata türlerini yakalar (ValueError, FileNotFoundError)
    -Gerekirse finally ile kaynakları temizler
    -Büyük projelerde logging ile hata detaylarını kaydeder
"""
class Book():

    def __init__(self, title, pages=None): 
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        return False

    def __str__(self):
        return f"{self.title} is {self.pages} pages long"
    
    def __eq__(self, other):
        if self.title == other.title and self.pages == other.pages:
            return True
        return False
    
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)
    
open("input.txt", 'a')
file = open("input.txt", 'w')
file.write("Kavim\t382\n")
file.write("Agatha'nin Anahtari\t152")
file.close()

file = open("input.txt", 'r')
data = file.read().split('\n')
file.close()

book1_data = data[0].split('\t') #tablara göre ayrım
print("71-1- ", book1_data)
book1 = Book(book1_data[0], book1_data[1])

book2 = Book(data[1].split('\t')[0], data[1].split('\t')[1]) #yukarıdakinin aynısı daha kısa sadece

try:
    file = open("input.txt", 'r')

except FileNotFoundError as e: 
    print("73-1- ", e)
    print("73-1- ", "Cannot find file")

try:
    int(file.read())

except ValueError as e:
    print("73-2- ", type(e)) #bu şekilde e yani errorun type ını da yazdırabiliriz
    print("73-2- ", "İnte dönüşecek bir veri değil bunlar")

except Exception as e:
    print("73-3- ", e)
    print("73-3- ", "Something went wrong")

finally:
    file.close()
    print("73-4- ", "I always come here")

"""
Bu kodda ne oluyor:
try ın içinde hata olasılığı olan kodu çalıştırıyoruz.
    -Dosya açma (FileNotFoundError olabilir)
    -Dosya içeriğini int’e çevirme (ValueError olabilir)
    -Bir hata olursa, Python hemen ilgili except bloğuna atlar. Devamındaki kodu çalıştırmaz. 
    -bu sebeple onun except bloğununa gidilmez. Bu yüzden try bloğunu mümkün olduğunca küçük tutmak iyi bir pratiktir. h
    -her riskli durum için bir try bloğu açılabilir.
    -istenirse try ları iç içe de açabiliriz.

except blokları:
    -Spesifik hataları yakalıyoruz, istediğimiz özel hata mesajlarını yazdırabiliriz.
    -as e diyerek hata mesajını e değişkenine atıyoruz böylelikle e yi kullanarak hata mesajlarını yazdırabiliriz.


Genel Exception bloğu: 
    -Beklenmeyen hatalar için. Bütün hatalarda girilir. Eğer hata olmazsa girilmez.

finally bloğu:
    -Her durumda çalışır.
    -Kaynak temizliği için kullanılır (dosya kapatma gibi).
"""

#74 - Exception Handling using with PRATİK İÇİN https://www.youtube.com/watch?v=ly1In5XHrAA İZLENEBİLİR
"""
with yapısı, Python’da context manager(kaynağı açıp sonra otomatik olarak kapatan yapı) kullanmak için yazılır. 
En yaygın kullanım alanı: dosya açma ve kapama:
    -Dosyayı açar
    -İşin bitince otomatik olarak kapatır
    -Hata olsa bile file.close() çağrılır → kaynak sızıntısı olmaz

with yapısı her yerde kullanılabilir — yeter ki nesne bir context manager olsun. Örnekler:
    -Dosya işlemleri (open)
    -Thread kilitleri (threading.Lock)
    -Veritabanı bağlantıları (sqlite3.connect)
    -Web oturumları (requests.Session)
    -Zaman ölçümleri (timeit modülüyle)

Birinci ve ikinci kodun farkı:
    with yapısı dosyayı güvenli şekilde kapatır ama dosyayı açarken hata oluşursa, with bloğuna bile girilemez. 
    İşte bu yüzden bazı geliştiriciler önce try içinde dosyayı açar, sonra with ile devam eder.

"""
#birinci örnek
with open("input.txt") as file:
    if not file.closed:
        print("74-1- ", "opened")

if file.closed:
    print("74-1- ", "closed")

#ikinci örnek
try: 
    file = open("input.txt")

except OSError: #FileNotFoundError u inherit etmiş bir hata sınıfıdır.
    print("Cannot Open")

else: #eğer except e girilmezse else bloğuna girer
    with file:
        #code to pars with
        print("74-2- ", file.readline()) #readLine(): Dosyadan bir satır okur. Her çağrıldığında bir sonraki satıra geçer. 



#65 - Intro to Object Oriented Programming - Classes, __init__, Objects
"""
OOP (Object-Oriented Programming) Nedir?
    OOP, yazılımı nesneler üzerinden modellemeyi sağlayan bir programlama yaklaşımıdır. 
    Gerçek dünyadaki varlıkları (araba, kitap, kullanıcı vb.) kodda temsil etmek için kullanılır.

🧩 Temel Kavramlar
Kavram	        Açıklama
class	        Nesne şablonu. Özellikleri ve davranışları tanımlar.
object	        Sınıftan üretilen somut örnek.
attribute	    Nesnenin özellikleri (örneğin: renk, hız, başlık).
method	        Nesnenin davranışları (örneğin: hızlan, yazdır, sil).
self	        Nesnenin kendisini temsil eder. Kodun “ben” ifadesidir.
__init__	    Yapıcı metot. Nesne oluşturulurken ilk çalışan fonksiyondur.
encapsulation	Veriyi gizleme ve koruma (private/public).
inheritance	    Kalıtım. Bir sınıf başka bir sınıftan özellik alabilir.
polymorphism	Çok biçimlilik. Aynı isimli metod farklı şekillerde çalışabilir.

Neden self kullanılır?
    -Her nesne kendi verisini tutar.
    -self, o veriye erişmek için bir anahtardır.
    -Python, nesne metodlarını çağırırken otomatik olarak self’i gönderir.

Ne zaman self kullanılmaz?
    @staticmethod → nesneyle ilgisi olmayan fonksiyonlar
    @classmethod → sınıfın kendisiyle çalışan fonksiyonlar (cls kullanılır)

NOT: Self en başta olmak zorunda yoksa python en baştaki self zannediyor. Ve positional çağırılmak zorunda keyword verilemez.

Selfli vs Selfsiz:
class Hesaplayici:
    def __init__(self, sayi):
        self.sayi = sayi

    def kare(self):
        return self.sayi ** 2  # self ile nesneye bağlı işlem

    @staticmethod
    def kup(sayi):
        return sayi ** 3  # self yok, dışarıdan gelen veriyle işlem    
    
h1 = Hesaplayici(4)

print("Kare:", h1.kare())         # ✅ Nesneye bağlı, self kullanıyor → 16 #TEKRARDAN PARAMETRE VERMENE GEREK YOK NESNE İLE HALLETTİN
print("Küp:", Hesaplayici.kup(4)) # ✅ Sınıfa bağlı, self yok → 64 #PARAMETREYİ VERMELİSİN NESNE YOK
print("Küp (nesneyle):", h1.kup(4)) # ✅ Nesneyle de çağrılabilir → 64

Constructer mı __init__ mi?
    __init__, nesnenin kimliğini ve davranışını başlatır. Tıpkı modül alias’ı gibi, nesneye özel veri tanımlar.
    __new__, daha derin bir yapı; nesnenin bellekteki varlığını oluşturur.
Diğer dillerde (Java, C++, C#) constructor doğrudan nesne oluşturur. Python’da bu görev ikiye bölünmüştür.

Pythonda dinamik olarak halihazırda sınıfın içinde var olmayan attiributelar eklenebilir: satır 70 de örneği var    
"""

class Book():
    def __init__(self, title): 
        print("65- Initializer nesne ürettiğinde direk çalışan yapıdır, bu da kanıtı", self)
        self.title = title
        

book1 = Book("Beyoğlu'nun En Güzel Abisi") #nesneye bağlı olarak verileri tutabiliyoruz
print("65-1- ", book1.title) #başlığı parametre olarak vermedim nesne ile halletmiştim

if isinstance(book1, Book): #book1 'in Book türünden olup olmadığını böyle kontrol edebiliriz.
    print("65-2- ", "yes it is in book")
else:
    print("65-2- ", "no it is not book")

book = Book("şeytan ayrıntıda gizlidir") #Dinamik attribute ekleme
book.year_of_pub = "2022"  # sınıfta yoktu ama ekledik!
print("65-3- ", book.year_of_pub) # çıktı: 2022


# 66 - Creating and Invoking Methods

class Book():
    def __init__(self, title, pages=None): #pages=None demezsek onu vermeden nesne oluşumu yapamayız TypeError: Book.__init__() missing 1 required positional argument: 'pages' verir eksik argüman
        print("66- Initializer nesne ürettiğinde direk çalışan yapıdır, bu da kanıtı", self)
        self.title = title
        self.pages = pages
    
    def is_long(self):
        if self.pages > 100:
            return True
        return False

book2 = Book("Beyaz Leke", 768)
print("66-1- ", book2.title) #farklı nesne farklı sonuç

print("66-2- ", book2.is_long())

#67 - Class Level Variables
"""
-Sınf seviyesindeki variableslara direk Sinifadi.Değişkenadı diye erişebiliyoruz 
    ama nesneye bağli methodlarda nesneismi.methodismi ile erişilir.

-Burada favorites listesi tüm Book nesneleri için ortak. 
    Yani book1.favorites diye erişmeye çalışırsan Python önce book1’in kendi içinde favorites var mı diye bakar, bulamazsa sınıfa döner. 
    Ama doğrudan Book.favorites demek daha net ve Pythonik.
"""
class Book():

    favorites = []

    def __init__(self, title, pages=None): 
        self.title = title
        self.pages = pages
    
    def is_long(self):
        if self.pages > 100:
            return True
        return False

book1 = Book("Beyoğlu'nun En Güzel Abisi")
book2 = Book("Beyaz Leke", 768)

Book.favorites.append(book1)
Book.favorites.append(book2)
Book.favorites.append("Eklenen String de olabilir") 

print("67- ", Book.favorites) #[<__main__.Book object at 0x0000022286536CF0>, <__main__.Book object at 0x00000222867B4A50>] konumunu verir

for b in Book.favorites:
    print("67-1- ", b, b.title) #title a eriştik

# 68 - Intro to Method Overrides - __str__
"""
__str__ Nedir?
    -Python'da özel bir metottur (dunder method: double underscore). 
    -print(nesne) veya str(nesne) çağrıldığında otomatik çalışır. Artık return ettiği değer kullanılır bundan zaten override(geçersiz kılmak) deniyor.
    -Override edilmezse, nesnenin bellek adresini verir (pek estetik değil).

"""
class Book():

    favorites = []

    def __init__(self, title, pages=None): 
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} is {self.pages} pages long"

book1 = Book("Beyoğlu'nun En Güzel Abisi", 456)
book2 = Book("Beyaz Leke", 768)

Book.favorites.append(book1)
Book.favorites.append(book2)

for b in Book.favorites:
    print("68- ", b)

#69 - __eq__ Method Override
"""
-__eq__ override etmek, nesnelerin eşitlik mantığını tanımlamak demektir. 
-Yani book1 == book2 gibi bir karşılaştırma yaptığında Python’un neye göre “eşit” diyeceğini sen belirliyorsun.

-Eğer __eq__ override edilmezse, Python iki nesnenin bellek adresine bakar. Ama biz overriide edebiliriz:

******** book1 == book2 dediğimizde ne oluyor *********
pyhton arka planda "book1.__eq__(book2)" yi çalistiriyor. self, book1 i aliyor. book2 de otomatikmen other a kaliyor.

ASLINDA BÜTÜN == OPERATÖRLERİ ARKA PLANDA __eq__ METHODUNU ÇAĞIRIR:
    -Sayılar arasında == → sayısal eşitlik kontrolü (int.__eq__)
    -String’ler arasında == → karakter dizisi eşitliği (str.__eq__)
    -Listeler arasında == → eleman bazlı eşitlik (list.__eq__)
    -Nesneler arasında == → senin override ettiğin __eq__ çalışır
"""

class Book():

    def __init__(self, title, pages=None): 
        self.title = title
        self.pages = pages

    
    def __str__(self):
        return f"{self.title} is {self.pages} pages long"
    
    def __eq__(self, other):
        print(self, other)
        if self.title == other.title and self.pages == other.pages:
            return True
        return False

book1 = Book("Beyoğlu'nun En Güzel Abisi", 456)
book2 = Book("Beyoğlu'nun En Güzel Abisi", 456)

print("69- ", book1 == book2)

#70 - __hash__ and Collections 
"""
Python'da biz bir sınıf tanımladığımızda — yani class Book: gibi — ve hiçbir özel davranış override etmediysen, 
    o sınıftan türetilen nesneler varsayılan olarak hashable kabul edilir.

__eq__ ile eşitlik mantığını değiştirdiğinde, Python artık __hash__'in güvenilir olup olmadığını bilemez. 
    Hash değerleri, eşitlik mantığına bağlıdır. Eğer iki nesne == ile eşitse, onların hash() değerleri de aynı olmalı. 
    Bu tutarlılığı sağlayamazsan, set, dict gibi yapılarda tuhaf davranışlar ortaya çıkar.
    
    data = {book1, book2} şeklinde kullanilamaz, TypeError: unhashable type: 'Book' verir

Eğer sinifin nesneleri hash lemek için kullanilmayacaksa okuma kolayliği için sinif içinden hashlemeyi kapamak en iyisi: 
    __hash__ = None #denir

    Eşitlik mantığı özelleştirilmişse (__eq__) ama hash mantığı tanımlanmadıysa, Python zaten otomatik olarak __hash__ = None atar. 
        Bu bir güvenlik önlemidir.

    Ama biri bunu manuel olarak yazdıysa, sana şunu demek istiyor olabilir:
        -“Bu nesnelerin eşitliği var ama hashlenmesi mantıklı değil.”
        -“Bu nesneler mutable (değişebilir), o yüzden hashlenmeleri riskli.”
        -“Bu sinifi bilinçli olarak set ve dict dışında tutuyorum.”
    Yani __hash__ = None yazmak, bu sınıfın nesnelerinin hashlenmesini bilinçli olarak devre dışı bırakmak demektir.
    
    Peki bunu neden yapalım?
    -Mutable (değişebilir) nesneler için hashlenme risklidir. Çünkü nesnenin durumu değişirse, hash değeri de değişebilir. 
        Bu da set/dict gibi yapılarda tutarsızlıklara yol açar.
"""

class Book():

    def __init__(self, title, pages=None): 
        self.title = title
        self.pages = pages

    
    def __str__(self):
        return f"{self.title} is {self.pages} pages long"
    
    def __eq__(self, other):
        print(self, other)
        if self.title == other.title and self.pages == other.pages:
            return True
        return False
    
    # __hash__ = None #mutable değerler varsa sınıfı hashleme için kullanmayacaksan kapayabilirsin bu özelliği
    
    def __hash__(self):
        return hash(self.title) ^ hash(self.pages)
    """
    hash(self.title) ^ hash(self.pages):
    hash(self.title) → title attribute’unun hash değeri
    hash(self.pages) → pages attribute’unun hash değeri
    ^ → Bit düzeyinde XOR işlemi (ikisini birleştiriyor ama çakışmayı azaltacak şekilde)

    Yani bu metod, title ve pages değerlerini birleştirerek nesneye özgü bir hash değeri üretiyor. 
    Bu sayede iki nesne aynı title ve pages’e sahipse, aynı hash’e sahip olurlar — ama farklıysa, hash’leri de farklı olur.
    """

book1 = Book("Beyoğlu'nun En Güzel Abisi", 456)
book2 = Book("Beyaz Leke", 456)

data = {"nesne1": book1, "nesne2": book2} #dict içinde kullanılabilir çünkü key in hashable olması lazım value değil
print("70-1 ", hash(book1), hash(book2))
book1.title = "ölümsüz aile"
book2.title = "ölümsüz aile"
print("70-2 ", hash(book1), hash(book2)) #hash değerleri değişti ve artık aynı değere sahip oldukları için HASH DEĞERLERİ AYNI OLUR
"""
book1 in title ını değiştirdiğim için hash değeri de değişti 
    Eğer nesneyi hashable yapılara koymuyorsan (set, dict key vs.),
    Veya nesne değiştirilmeyecekse (immutable gibi davranıyorsa) sorun olmaz.
"""





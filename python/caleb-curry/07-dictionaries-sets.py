#55 - Intro to Dictionaries
"""
Python'da dictionary (sözlük), verileri anahtar-değer çiftleri şeklinde saklayan özel bir veri yapısıdır. 
Liste gibi sıralı değildir ama çok daha esnek ve güçlüdür çünkü her değere bir anahtar üzerinden erişilir.

Sözlüklerin Özellikleri:
-Sırasızdır: Elemanların sırası sabit değildir (Python 3.7+ ile eklenme sırası korunur ama bu garanti değildir).
-Değiştirilebilir: İçeriği sonradan güncellenebilir.
-Anahtarlar benzersizdir: Aynı anahtar birden fazla kez kullanılamaz.
-Değerler her tür olabilir: Sayı, liste, başka bir sözlük vs.

-Python'da sözlüklerin (dictionary) çalışma prensibi, hash tablosu mantığına dayanır. Bu da demek oluyor ki:
-Sözlükteki anahtarlar (keys), hızlı erişim için hashable olmak zorundadır. Variables ın hashable olmasına gerek yok.
-Çünkü Python, her anahtarın hash() değerini hesaplayarak onu bir tabloya yerleştirir.
-Bu sayede my_dict[key] gibi bir erişim, doğrudan hash üzerinden yapılır — yani çok hızlıdır.

Hashable Olan Nesneler
Nesne Türü	    Hashable mı?	     Açıklama
int, str	    ✅ Evet	            Değiştirilemez (immutable)
tuple	        ✅ Evet	            İçindeki elemanlar da hashable ise
list, dict	    ❌ Hayır	            Değiştirilebilir (mutable)
frozenset	    ✅ Evet	            Sabit set

O(1) --> constant time : sürekli aynı olan değişmez çalışma zamanını ifade eder kütüphaneler de bu şekildedir

"""
#I'm not sure of exact internals on how the hash is used, but imagine it like so:
#You have an area of memory with 8 spots, and you need to store the value at some spot...
#Hash fonksiyonu, bir girdiyi (örneğin bir string, sayı, dosya vs.) alır ve sabit uzunlukta, genellikle rastgele görünen bir çıktı üretir. 
print("0- ", hash("hello")) # 4539124796312321521

emails = {
        "caleb" :  "caleb@email.com", #caleb = key, caleb@email.com = value
        "iclal" : "iclal@email.com",
        (5, 8) : "selam",
        # [1,2,3] : "hi" TypeError: unhashable type: 'list'
 }

print("55- ", emails)

print("56- ", emails["caleb"]) #bulamazsa Key Error verir

if "iclal" in emails: #daha güvenlidir (bulunmama durumuna karşın)
    print("56- ", emails["iclal"])

print("56- ", emails.get("caleb")) #birinci parametresi erişeceği key, ikinci parametresi default value
print("56- ", emails.get("caleb", "Not Found")) #ikinci parametresi bulamazsa döneceği değerdir

#57 - Add Items to Dictionary (3 Ways)

emails["josh"] = "j@email.com"

emails.update({"samiel" : "s@email.com", "ryan" : "r@email.com"})

emails.update(ikbal = "iko@email.com")

print("57- ", emails)

#58 - Loop through Dictionary
emails = {
        "caleb" :  "caleb@email.com", #caleb = key, caleb@email.com = value
        "iclal" : "iclal@email.com",
        (5, 8) : "selam",
        # [1,2,3] : "hi" TypeError: unhashable type: 'list'
 }

for k in emails:
    print("58- ", k, emails[k]) #valueyi yazdırmak için pek önerilen bir yol değil


#59 - Looping through Key Value Pairs + Counting Words
emails = {
        "caleb" :  "caleb@email.com", #caleb = key, caleb@email.com = value
        "iclal" : "iclal@email.com",
        (5, 8) : "selam",
        # [1,2,3] : "hi" TypeError: unhashable type: 'list'
 }

for k, elem in emails.items(): #bu şekilde de erişebiliriz
    print("59-1- ", k, elem)

conjunctions = {"for" : 0, "and" : 0, "nor" : 0, "but" : 0, "or" : 0, "yet" : 0, "so" : 0}

completely_original_poem = """I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side"""

data = completely_original_poem.split()

for k in data:
    if str.lower(k) in conjunctions:
        conjunctions[str.lower(k)] += 1

print("59-2- ", conjunctions)

#60 - Working with Sets
"""
Set, Python'da benzersiz ve sırasız öğelerden oluşan bir veri yapısıdır. Setin içindeki verilerin hashable (değiştirilemez) olması gerekir.

Neden Hashable Olmalı?
    -Hızlı erişim için: set içinde bir elemanın olup olmadığını kontrol etmek (x in my_set) çok hızlıdır 
    çünkü Python elemanın hash’ini alır ve doğrudan tabloya bakar. Bu, O(1) zaman sağlar.

    -Değişmezlik (immutability): Hash değeri sabit olmalı ki tablo bozulmasın. 
    Eğer bir eleman değişirse (örneğin bir list), hash değeri de değişebilir. Bu durumda eleman artık bulunamaz hale gelir. 
        Örnek:
            python
            s = set()
            s.add([1, 2])  # TypeError: unhashable type: 'list'

    Veri bütünlüğü: Hash değeri değişirse, set içindeki veri bozulur. 
    Bu yüzden sadece değiştirilemeyen (immutable) türler hashlenebilir: int, str, tuple, frozenset gibi.

Setler yes or no algoritalarında çokça kullanılırlar. Arama, intersection(ortak elmanları bulma), difference(birinde olup diğerinde olmayanları bulma) gibi işlemler için idealdirler.

"""

conjunctions = {"for", "and", "nor", "but", "or", "yet", "so"}
seen = set() #boş set tanımlamak için set() kullanılır, {} dictionary tanımlamak için kullanılır

completely_original_poem = """I still hear your voice when you sleep next to me
I still feel your touch in my dreams
Forgive me my weakness, but I don't know why
Without you it's hard to survive
'Cause every time we touch, I get this feeling
And every time we kiss I swear I could fly
Can't you feel my heart beat fast, I want this to last
Need you by my side or yet so"""

data = completely_original_poem.split()

for word in data:
    if str.lower(word) in conjunctions:
        seen.add(str.lower(word))

print("60- ", seen)

#61 - Remove Duplicates in a List using Sets
colors = ['red', 'red', 'green' , 'blue' , 'blue', 'blue', 'blue']

colors[:] = list(set(colors))

print("61-1- ", colors)

#arka planda olanlar:
colors = ['red', 'red', 'green' , 'blue' , 'blue', 'blue', 'blue']
count = [ [colors.count(color), color] for color in set(colors)]
print("61-2 ", count)

#algoritmik yol
colors = ['red', 'red', 'green' , 'blue' , 'blue', 'blue', 'blue']

unique_color = []

for color in colors:
    if color not in unique_color: #yeninin içinde yoksa ekle
        unique_color.append(color)

colors[:] = unique_color
print("61-3- ", colors)

#list comprehensionlı yol:
colors = ['red', 'red', 'green', 'blue', 'blue', 'blue', 'blue']
seen = set()

#1. yol
counts = [[colors.count(item), item] for item in set(colors)]
print("61-4- ", counts)

#2. yol
colors[:] = [c for c in colors if not (c in seen or seen.add(c))] #seen.add(c) ihtiyaç olursa çalışır ve None döner yani or un cevabı c in seen e bağlı
#(c seenda yoksa false dönecek ve seen.add(c) yi çalıştırcak, c seen da varsa or un cevabı + çıktığı için hiç seen.add çalışmıcak)
print("61-5- ", colors)



#62 - Union and Intersection - Set Operations:
"""
       _____ ______      
     /      /\      \
    /    A /C \  B   \     
    \      \  /      /
     \______\/______/

union = İki kümenin tüm benzersiz elemanlarını alır (BİRLEŞİM KÜMESİ)
| operatörü kullanılır, listlerde felan çalışmaz bu, set gibi veri türleri için tanımlanmıştır. 

intersection: Intersection, yani kesişim, iki küme (set) arasında ortak olan elemanları bulma işlemidir

ikisinin de hem operatörü hem de fonksyonu var örnekteki gibi:

"""
my_fav = {"red", "green", "blue", "black", "purple"}
her_fav = {"blue", "orange", "purple", "green"}

all_favs = my_fav | her_fav  # A + B + C
print("62-1- ", all_favs) 

all_favs = my_fav.union(her_fav) # A + B + C
print("62-2- ", all_favs)

wedding_colors = my_fav & her_fav # C
print("62-3- ", wedding_colors)

wedding_colors = my_fav.intersection(her_fav) # C
print("62-4- ", wedding_colors)

#63 - Difference and Symmetric Difference - Set Operations
"""
       _____ ______      
     /      /\      \
    /    A /C \  B   \     
    \      \  /      /
     \______\/______/
"""
my_fav = {"red", "green", "blue", "black", "purple"}
her_fav = {"blue", "orange", "purple", "green"}

only_mine = my_fav - her_fav # A
print("63-1- ", only_mine)

only_mine = my_fav.difference(her_fav) # A
print("63-2- ", only_mine)


only_her = her_fav - my_fav # B
print("63-3- ", only_her)

only_her = her_fav.difference(my_fav) # B
print("63-4- ", only_her)

only_mine = my_fav - her_fav # A
only_her = her_fav - my_fav # B
symmetric_fav = only_her | only_mine # A + B
print("63-5- ", symmetric_fav)

symmetric_fav = my_fav ^ her_fav # A + B
print("63-6- ", symmetric_fav)

symmetric_fav = my_fav.symmetric_difference(her_fav) # A + B
print("63-7- ", symmetric_fav)

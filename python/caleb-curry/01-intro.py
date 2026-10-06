#2 - Intro to Lists:
"""
biz bir liste oluşturduğumuzda aslinda arka planda sınıfın adını bir object haline getiriyoruz. 
o listenin asıyla yani objectle de list sınıfının içindekilere erişiyoruz.

örneğin: "append" bir methoddur .append diyerek ona erişiyoruz. 
list → Python’da daha önceden tanımlanmış bir sınıf
healty → Bu sınıfın bir örneği (instance)

method ve stendalone fonksyon farkı: methodlar sınıfların içinde tanımlanmış fonksyonlardır. Append gibi. 
O sınıfın nesnesi ile çağrılırlar ama stendalone fonksyonlara erişirken böyle bir şeye gerek yok her yerden erişilebiliriz.
"""
healty = ["patlıcan" , "et" , "sebze"] 

healty.append("muz")

print("2 " , healty)
print()

#3- Checking if them in the list:
healty = ["patlıcan" , "et" , "sebze"] 

if ("domates" in healty): #listeden eleman kontrolü böyle yapılır
    print("3 " , "domatesi bulduk")
else:
    print("3 " , "domatezsiz yaşanır mı ")
print()

#4- working with list: bir listenin içindekileri diğerinde de var mı? (Benim kodum)
healty = ["patlican" , "salatalik" , "brokoli", "köfte"]
backpack = ["cips" , "salatalik" , "kurabiye" , "jelibon" , "köfte" , "patlican" , "brokoli"]
diet_list = []

for i in backpack:
    for j in healty:
        if i == j:
            diet_list.append(i)

print("4" , diet_list)
print()

# 5 - Removing from Lists using List Comprehension: bir listenin içindekiler diğerinde de varsa onlara erişmek:
#yeni bir liste yaratmadan backpack i koruyan yöntem
healty = ["patlican" , "salatalik" , "brokoli", "köfte"]
backpack = ["cips" , "salatalik" , "kurabiye" , "jelibon" , "köfte" , "patlican" , "brokoli"]

print(id(backpack))
backpack[:] = [item for item in backpack if item in healty] #Meali: item diye bir değişkenim olsun o backpack içinde dolaşsın 
#onun bütün elemanlarını alsın ama eğer healtnın içinde varsa
print(id(backpack)) #bu yöntemle backpack ögesi kaybolmaz çünkü üst satırda backpack[:] diyerek bütün elemanlarına tek tek eriştik 

print("5 " , backpack)

#yeni liste yaratarak backpack i korumayan yöntem
healty = ["patlican" , "salatalik" , "brokoli", "köfte"]
backpack = ["cips" , "salatalik" , "kurabiye" , "jelibon" , "köfte" , "patlican" , "brokoli"]

print(id(backpack))
backpack = [item for item in backpack if item in healty] #Meali: item diye bir değişkenim olsun o backpack içinde dolaşsın 
#onun bütün elemanlarını alsın ama eğer healtnın içinde varsa
print(id(backpack)) #bu yöntemle backpack ögesi kaybolur çünkü üst satırda backpack[] dedik

print("5 " , backpack)
print()

#6 - Intro to List Comprehension: List Comprehension ile yaptığımızı döngülerle de yapabiliriz onun için örnekler
healty = ["patlican" , "salatalik" , "brokoli", "köfte"]
backpack = ["cips" , "salatalik" , "kurabiye" , "jelibon" , "köfte" , "patlican" , "brokoli"]

healty_backpack = []

#healty_backpack[:] = [item for item in backpack if item in healty]

for item in backpack:
    if item in healty:
        healty_backpack.append(item)

print(healty_backpack)

#karelerini alan örnek
square = []

for i in range(10):
    square.append(i ** 2) 

print("6 " , square)

squares = [i ** 2 for i in range(10) if i % 2 == 0] #döngülerle yaptığımız şeyleri böyle de yapabiliriz sondaki gibi verilerle oynayabilir koşula bağlı tutabiliriz
print("6 " , squares)
print()

#7 - Length of List with len: 
# n --> list size
# n - 1 --> highest index num 

greetings = ["hi" , "hello" , "sa"]

for item in greetings:
    print("7 ", item) #bu örnekte listenin uzunluğu(n) ne kadar artarsa döngüdeki aşama sayısı da n kadar artacak çok büyük bir sorun değil 
#ama kimi örneklerde n^2 gibi artabilir bunlar performansı olumsuz etkiler

for i in range(len(greetings)): #length'i i ile beraber de böyle kullanabiliriz 
    print("7 ", i, greetings[i])
print()

# 8 - Count - Counting an Element in List:
backpack = ["sword", "bag", "zihgir", "yay", "zihgir", "zihgir"]

backpack.append("zihgir")

print("8-" , backpack.count("zihgir")) #bir listedeki eleman sayısı böyle sayılır

if backpack.count("yay") >= 1: 
    backpack.append("yay")

if "yay" in backpack: #bununla bir üstteki aynı şey
    backpack.append("yay")

# 9 - Intro to Sets: “Her öğeden yalnızca bir tane bulunmasına izin veren, sırasız bir koleksiyon.”
#sırayı korumaz karışır, genelde listede bir şeyin var olup olmadığını anlamak için kullanılır
backpack = ["sword", "bag", "zihgir", "yay", "zihgir", "zihgir"]
backpack2 = {"sword", "bag", "zihgir", "yay", "zihgir", "zihgir"}

print("9- ", backpack2)
#print(backpack2.count("zihgir")) AttributeError: 'set' object has no attribute 'count' alınır zaten set yapmışsın bir tane olacağını biliyorsun sayamazsın diyor.

print("9- " , "zihgir" in backpack2 )
print()

#10 - Count Each Element in List - List Comprehension
backpack = ["sword", "bag", "zihgir", "yay", "zihgir", "zihgir" ,
            "bardak", "bag", "zihgir", "yay", "zihgir", "zihgir",
            "sword", "bag", "salam", "yay", "tahta", "zihgir",
            "sword", "su", "zihgir", "ok", "zihgir", "zihgir"]

count = [print("10- " , item , backpack.count(item)) for item in set(backpack) ]
#backpack'in set halinde(her şeyden bir tane bulunan) dolaşıyor her elemanı item'e atıyor, en son da item i ve item'in sayısını yazıyor
print()

# 11 - Counter (from collections):
"""
Kısaca Counter Ne İşe Yarar?
Her bir öğenin frekansını tutar.

En çok geçen öğeleri kolayca bulmanı sağlar.

Çok kullanışlı sözlük benzeri bir yapıdır.

Counter’ın en çok kullanılan yöntemlerinden biri:

python
sayac.most_common(2)
# Çıktı: [('elma', 3), ('kiraz', 2)]
Bu, listedeki en sık geçen ilk iki öğeyi verir.

"""
from collections import Counter

backpack = ["sword", "bag", "zihgir", "yay", "zihgir", "zihgir" ,
            "bardak", "bag", "zihgir", "yay", "zihgir", "zihgir",
            "sword", "bag", "salam", "yay", "tahta", "zihgir",
            "sword", "su", "zihgir", "ok", "zihgir", "zihgir"]

print("11- " , Counter(backpack))
print()





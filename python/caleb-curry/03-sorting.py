#27 - Sort List with sort Method: alfabetik sıralar
workdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

workdays_copy = workdays[:]

workdays_copy.sort() #orjinal veriyi değiştirir o yüzden copy oluşturduk

print("27- ", workdays_copy)

#28 - Sort with the Sorted Method: alfabetik olarak sıralar ama .sort gibi orjinal dataya dokunmaz, 
# return ile sıralanmış halini döndürür. 
# Önemli bir diğer farkı ise: sort() sadece listelerle çalışır, 
# sorted() ise Iterable yani (liste, tuple, string, dictionary vs.) ile çalışabilir.
# İkisi de sayısal verilerle çalışabilir.
workdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
print("28- ", sorted(workdays)) 

data = [89, 55, 48, 1, 0, 5, 6, 3]
print("28- ", sorted(data)) #küçükten büyüğe sıralar

numbers = sorted([1, 3, 45, 89, 0, 2]) #sortede direk hızlı bir şekilde böyle de veri verebiliriz 
print("28- ", numbers)

# 29 - Sort Data in Reverse Order: Büyükten küçüğe sıralama
#1.yol
data = [89, 55, 48, 1, 0, 5, 6, 3, -8]

data.sort()
data.reverse()
print("29-1- ", data)

#2.yol: reverse, sorted fonksyonunun keyword parametresidir. 
#reverse=False → Artan sıralama (default)
#reverse=True → Azalan sıralama

data = [89, 55, 48, 1, 0, 5, 6, 3, -8]

data_sorted = sorted(data, reverse=True) 

print("29-2- ", data_sorted) 

#30 - Case Insensitive Sort:
strings = ['a', 'A', 'abc', 'ABC', 'aBc', 'aBC', 'Abc']
strings.sort() #normalde sort fonksyonu büyük küçük harfe duyarlıdır, büyükleri öne alır.
print("30- ", strings) 

strings.sort(key= str.lower) 
print("30- ",strings)
"""
sorted(iterable, key=None, reverse=False)

key parametresi sort fonksyonunun keyword parametresidir fonksyon türleri alır ve sort da aldığı fonksyona göre sıralama yapar.
Bu örnekte önce hepsini küçültür böylelikle büyük küçük harf gözetmeksizin sıralama yapılmış olur.
Ve hepsini küçük gördüğü için listedeki sıralarına göre yazılırlar, ilk olan baştadır

Örneğin kendi key fonksyonumuzu da yazabiliriz:

def uzunluk(s):
    return len(s)

strings = ['elma', 'armut', 'muz']
sorted(strings, key=uzunluk)
# Çıktı: ['muz', 'elma', 'armut']

"""

#31 - Sort by String Length (len): uzunluğa göre sıralayan program
random = ["a", "A", "aa", "AAA", "HELLO", "b", "c", "a"]
print("31- ", sorted(random, key=len)) #sorted la yapıp return ini kullanabiliriz

#32 - Lexicographic Number Sort (Sort Numbers as Strings): alfabetik sıralamaya göre yazıyor yani 12 > 111 çünkü 2 gelmiş bir yerine
numbers = [1, 54, 76, 12, 111, 4343, 6, 8888, 3, 222, 1, 0, 222, -1, -122, 5, -30]

numbers.sort(key= str)
print("32- ", numbers)

#33 - Compare and Sort Various Types: değerleri sayısal olarak karşılaştırma
"""
stuff.sort(key=float) dedik çünkü float fonksyonu değerleri sayısal olarak karşılaştırılabilecek bir hale sokar:
'5' → float('5') → 5.0
'5.5' → float('5.5') → 5.5
**True → float(True) → 1.0
**False → float(False) → 0.0

"hello" diye çevrilemeyen bir değer girilirse hata verir
"""
age = 5
stuff = [True, False, 0, -1, "0", "1", "10", age < 30, "20", "2", "5", "9001", "5.5", "6.0", 6]

stuff.sort(key = float)
print("33- ", stuff)

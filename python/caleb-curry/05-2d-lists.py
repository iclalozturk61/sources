#42 - Working with List of Lists (2D Lists): c# da jagged array(düzensiz iç içe diziler) denir.
"""
Burada for inner_list in grades: döngüsünde, inner_list bazen bir sayı oluyor (5 veya 10). 
Sonra for grade in inner_list: satırında, sayı üzerinde döngü kurmaya çalıştığı için şu hatayı alırsın:
TypeError: 'int' object is not iterable, bunu düzeltmek için liste olup olmadığını kontrol etmeliyiz.
"""
grades = [[10,20,60] , [50] , [100, 90, 80], 5, 10]

for inner_list in grades:
    if isinstance(inner_list, list):
        print("42-1-", end=" ")
        for grade in inner_list:
            print( grade, end=" ")
        print()
    else:
        print("42-1- ", inner_list)
    

for i in range(len(grades)):
    if isinstance(grades[i], list):
        print("42-2- ", end=" ")
        for j in range(len(grades[i])):
            print(grades[i][j], end=" ")
        print()
    else:
        print("42-2- ", grades[i])
    

#43 - Create Function to print 2D List

grades = [[10,20,60] , [50] , [100, 90, 80]]

def print_2d(grades):
    for inner_list in grades:
        print("43- ", end=" ")
        for grade in inner_list:
            print(grade, end=" ")
        print()

print_2d(grades)


#44- Combining List Elements with join Method 
data = ["Python", "is", "fun"]
delimiter = " " #delimiter = ayıraç, bu örnekte boşlkla birleitirildi ama '-', ',', '/' gibi şeyler de alabilir
print("44-1- ", delimiter.join(data))

data = ["Python", "is", "fun", 5, 10]
delimiter = " "
print("44-2- ", delimiter.join(str(data))) 
"""
bu kod beklenen şekilde çalışmaz çünkü 
burada str(data) ifadesi aslında tüm listeyi tek bir stringe çevirir. 
str(data) → "['Python', 'is', 'fun', 5, 10]"
Bu durumda join() metodu, bu stringin karakterleri üzerinde çalışmaya çalışır. 
Yani ' ' karakteri, '[', 'P', 'y', 't', ... gibi karakterlerin arasına eklenir. Bu da beklenmeyen bir sonuç üretir.
Yani bütün karakterleri birleştirip hepsinin arsına boşluk ekliyor. Doğru çözüm:
"""

data = ["Python", "is", "fun", 5, 10]
delimiter = " "
print("44-3- ", delimiter.join(str(item) for item in data)) #generator expression

"""
Generator Expression Nedir?
# List comprehension ([]'lı olan)
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# Generator expression (()'lı olan)
squares_gen = (x**2 for x in range(5))
print(squares_gen)  # <generator object ...>

list comprehension'da gerçekten arka planda bir liste oluşturuyor. (list comprhension örnekleri 02-list in içinde var.)
Generator expression da her bir öge tek tek üretilir daha az yer kaplar.

",".join(["a", "b", "c"])      # Liste
",".join(("a", "b", "c"))      # Tuple
",".join(x for x in ["a", "b", "c"])  # Generator
join methodu iterable yani yukardakilerinin tamamını kabul eder. Ama en az yer kaplayanı generator
"""

#45 - Sort List of Lists
data = [[10, 2, 3], [10, 4], [ 4, 5000, 6], [10]]

print("45-1- ", sorted(data)) 

print("45-1- ", sorted(data, reverse=True)) #reverse=True ile ters sıralama yapar, birinci aşamadan terse çevrilir. Yani listelerin içine dokunmaz.  

data2 = [["ball", "apple"], ["amazon"], ["amz", "zen"]]

print("45-2- ", sorted(data2))

"""
Nasıl çalışır? 
Öncelikle her listenin ilk elemanına bakacak ona göre sıralayacak eğer aynı eleman varsa ikinci elemana bakacak ona göre sıralayacak.(Alfabetik gibi)
Not: Python, sıralama yaparken önce ilk elemanlara bakar. Eğer ilk elemanlar aynı tipte değilse (örneğin biri int, biri list), 
karşılaştırma yapamaz ve bu hatayı verir. Eğer karşılaştırılan herhangi bir konumda farklı tipler (örneğin biri int, biri list) varsa, 
Python karşılaştırma yapamaz ve yine aynı hatayı verir: TypeError: '<' not supported between instances of 'list' and 'int'
"""

#46 - Custom key Function with 2D Lists
data = [1, 8, 5555, 95, -8, -555, -4, 0]

print("46-1- ", sorted(data, key=abs)) #sorted fonksyonu ikinci parametre olarak methodları alıyor bu örnekte: abs = absolute (mutlak değer fonksyonu) kullanılmış.

data = [[10, 2, 3], [10, 4, 2], [4, 5, 6], [10, 10, 10]]
print("46-2- ", sorted(data, key=sum)) #listelerin elemanlarını toplayıp sıralayan örnek: oyunlardaki tolam puan bulma uygulaması gibi

data = [[10, 2, 3, 30], [10, 4, 2, 10, 10, 10, 10, 10, 10], [4, 5, 6, 100], [10]]

def avg(data):
    return sum(data) / len(data)

print("46-3- ", sorted(data, key=avg)) #böyle kendi yazdığımız fonksyonları da verebiliyoruz
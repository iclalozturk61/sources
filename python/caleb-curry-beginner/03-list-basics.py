#list
ages = [1,2,3]
people = ["hatice", "beyza" , "zeynep" , "feyza"]
my_favorite_things = ["friends" , 7 , ['tabi' , 'netflix' , 'youtube']]
print(id(my_favorite_things))

my_favorite_things[0] = "how I met your mother"
print(id(my_favorite_things)) #aynı id yi veriyor çünkü listler mutabledır. Elemanları değiştirilebilir başka yeni oluşturmaya gerek yok.

print(len(my_favorite_things)) #kendi içindeki diğer listeleri de bir saydığı için 3 eleman

#How to Copy a List (Slicing and copy Function)
print(my_favorite_things[:]) #bu şekilde bütün elemanlarına erişip yazdırabiliyoruz

copy1 = my_favorite_things[:] #bu şekilde tanımlayınca  my_favorite_things değişikliklerden etkilenmiyor
copy1[0] = "the mentalist" 

print(copy1 , my_favorite_things) 

copy2 = my_favorite_things #bu şekilde tanımlayınca  my_favorite_things değişikliklerden etkileniyor
copy2[0] = "the big bang teori" #çünkü bu tanımlama "alias" takma ad koyma olarak biliniyor, aynı şeye farklı bir isimle refere ediyorsun 

print(copy2 , my_favorite_things)

copy3 = my_favorite_things.copy() #copy fonksyonu kopyalama yapar my_favorite_things değişklerden etkilenmez
copy3[0] = "gassal"

print(copy3 , my_favorite_things)

#Intro to Nested Lists (2D Lists)
my_favorite_things = ["friends" , 7 , ['tabi' , 'netflix' , ['youtube' , 'instangram']]]
print(my_favorite_things[2][2][0]) #liste içindeki listeye böyle erişiyoruz
print(len(my_favorite_things))
print(len(my_favorite_things[2]))
print(len(my_favorite_things[2][2]))

#How to Deep Copy a List (copy.deepcopy)
copy4 = my_favorite_things.copy() #copy() fonksyonu immutable değerlerini kopyalar ama mutable değerler için alias(takma ad koyma) yapar
copy4 [2][1] = "disney plus" #eriştiğimiz değer bir liste olduğu içn alias yapacak

print(copy4 , my_favorite_things) 

import copy
copy5 = copy.deepcopy(my_favorite_things) #copy.deepcopy() fonsyonu yeni bir liste oluşturup bütün değerleri kopyalar.
#immutable veya mutable olmasına bakmaz ama yenii bir liste oluşturduğu için bellekte fazla yer kaplar
copy5[2][1] = "blu tv"
print(copy5 , my_favorite_things)

#Combining Lists (Concatenation for Lists)
least_favorite_things = ["tyt biyoliji" , "altyazısız bölümler"]
print(my_favorite_things + least_favorite_things) #böyle birleştirme yapılabiliyor

least_favorite_things = least_favorite_things + ["mantar"] #böyle ekleme yapılabiliyor
least_favorite_things.append("rush hour") #böyle de ekleme yapılabiliyor bu daha öneriliyor 
print(least_favorite_things)
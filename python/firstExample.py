print(16/2) #8.0 yazar 
print(5 + 3) #8 yazar
print( (6*2) + (8 /4) - 1) # bazen gerek olmasa bile görünüşü basitleştirmek için parantez kullanılabilir
print((((5 + 5)))) #fazla parantezler sorun çıkarmaz

"""" bu şekilde çoklu yorum satırı yazılabiliyor
round fonksyonu hakkında: bankacı yuvarlaması (banker's rounding) fonksyonudur: eğer yuvarlanacak sayı 5 ile bitmiyorsa 
sıkıntı yok normal matematikteki kurallar uygulanır ama 5 ile bitiyorsa en yakın çift sayıya yuvarlanır.
"""
yuvarlama = round(2.5) #normalde 3 e yuvarlanması gerekiyordu ama 2 çift o yüzden 2 ye yuvarladı
print(yuvarlama)
round(2.344, 2)  # → 2.34 , virgülden sonra gelen rakam noktadan sonraki kaç basamak saklanacak şekilde yuvarlanacağını işaret eder
round(2.345, 2)  # → 2.34  → çünkü 0.345 en yakın çift olan 0.34’e gider
round(2.355, 2)  # → 2.36  → çünkü 0.355 en yakın çift olan 0.36

import math
print(math.ceil(3.3)) #yukarıya yuvarlar
print(math.floor(3.6)) #aşağıya yuvarlar

print(5+5, 'hey', 10.3) #print farklı türleri aynı anda basabilir
print('hi', end= " ") #end komutu şunu yapar "" arasındakini yazar ama imleci alt satıra geçirmez
print('selam')


#variable naming rules
age1 = 1 #GOOD
age_of_users = 2 #GOOD
#age-3=3 #NOT GOOD
#4age = 4 #NOT GOOD
ag5e = 5 #GOOD
Age = 6 #NOT RECOMMENDED
#return = 5 #NOT GOOD it is keyword


# Floor Division (Double Forward Slash)
result = 10 / 3   # / --> float division 
print(result)   # // --> integer division

new_result = 10 // 3  #// math.floor() un işini yapıyor virgülden sonrasını atıyor
print(new_result)

#modulus
pizza = 10
people = 3
print('left over', 10 % 3) # % kalan bulma operatörüdür

#Raising Numbers to a Power
print(3 * 3 * 3)
print(3 ** 5) # ** üs işlemleri için kullanılıyor
result1 = math.pow(3 , 5) # birinci sayının ikinci sayı üssünü alır
print(result1)
#**********************STRING************************

#escape characters
print("Hello\nI\'m iclal\töztürk\rhey")
print("\x3A") #hexadecimal karakter numarası böyle verilir

print(r"merhabalar \t selam \n hehe") #Raw string: başa konan r ile escape characterlere bakılmaz ne yazdıysan kabul edilir 


#Double vs Single Quotes
print("annem 'iki ekmek al' dedi") #olur
print('annem "iki ekmek al" dedi') #olur
# print('annem 'iki ekmek al' dedi') olmaz
# print("annem "iki ekmek al" dedi") olmaz


#concenation = expectin 1 argument "eğer birleştirmek gibi"
msg1 = "selam"
msg2 = "iclal"

print(msg1, msg2) #seperate arguemts
print(msg1 + " " + msg2) #concenation 
print("hey" "there")

msg3 = ("uzuuuuun bir string"
"devam ediyor") #parantezi koymasaydım ikinci satırı görmezdi
print(msg3)
msg4 = "slm"
print(msg4 + "aleykum") #araya ya virgül ya da + koymak gerekiyor

#Multiline Strings (Three Double Quotes) = yanyana yazmasın alt satıra geçmelere saygılı olsun siye böyle yapılıyor.
#alt satıra geçmesini istemediğimizde \ koyuyoruz

poem = """Ağlasam sesimi duyar mısınız,
Mısralarımda;
Dokunabilir misiniz,
Gözyaşlarıma, ellerinizle?

Bilmezdim şarkıların bu kadar güzel,
Kelimelerinse kifayetsiz olduğunu
Bu derde düşmeden önce.

Bir yer var, biliyorum; \
Her şeyi söylemek mümkün;\
Epeyce yaklaşmışım, duyuyorum; \
Anlatamıyorum."""

print(poem)

#Slicing Strings 
sentence = "where am I?"
#           012345678910
#      -li: 10987654321
print(sentence[3:]) #3. dahil
print(sentence[:3]) #3. dahil değil

#Negatives with String Slicing
print(sentence[-4:]) #sondan 4. karakterden başlıyor ileri doğru (4. dahil)
print(sentence[:-7]) #sondan 7. karakterden öncesini yazdrıyor (7.dahil değil)

#Slicing with Two Numbers
print(sentence[6:8]) #6. dahil 8 dahil değil
print(sentence[6:-3]) #6. dahil -3. dahil değil
start_number = 6
print(sentence[start_number:start_number + 3]) #değişken kullanımına izin var

#Strings are Immutable : Bir string oluşturulduktan sonra, içeriği değiştirilemez., bir değişiklik yapılması durumunda
#başka değişken oluşturulur, bu değişkenin korunması konusunda fayda sağlar
task = "Substring"
print(id(task)) #id fonksyonu değişkenin bellekte nerede tutulduğuna dair bilgi verir

#task[0] = 's' #type error verir çünkü değiştirilemez

task = "Like"
print(id(task)) #id lerini farklı olması da bunun kanıtı

#length fonksion
print(len(task)) #uzunluğunu yazar hep index numarasının bir eksiğini yazar

#Convert Integer to String (Concat int and str)
msg5 = "please subscribe"
print("your message was " + str(len(msg5)) + " characters long") #str() fonksyonu ile dönüştürmek lazım yoksa erorr verir 
print("your message was " , len(msg5) , " characters long") #bu şekilde erorr vermez çünkü conconation yapmıyor




# Creating a Function
#Benefits: We can save lines of code if function is large
#One source of truth. No repeat of code. Need changes?
#update one spot
#Can improve code readability

def greet(): # bu şekilde tanımlanır
    print("merhabalar")
    print("iclal \n")    

greet()
greet()
greet()
greet()
print()

#Arguments and Parameters YARIM KALDI
def greet(name): #bunun adı parameters fonksyonun aldığı şeydir (parameters are the variables on the inside of the function)
    print("merhabalar" , name , "argüman örneğidir")

greet("iclal") #bunun adı arguments fonksyona verdiğimiz şeydir (arguments you pass the things)
print()

#return break gibi ama o döngüler için kullanılır bunu fonksyonlar için kullanılır. Fonksyonun içinde döngü varsa break ve continue kullanılabilir ama direk fonksyon içnde kullanılamaz
def greet(name):
    if name == "fellas":
        print("1. return çıktısı")
        return 
    print("fonksyonun içindeki asla okunmayacak şeyler")
    
greet("fellas")
print()

#return vs else to Exit Function: ikisi de olur ama okunabilirlik ve basitlik gereği return bence daha iyi
def greet(name):
    if name == "fellas":
        print("1. else ile çıkıldı")
     
    else: 
        print("fonksyonun içindeki asla okunmayacak şeyler")
    
greet("fellas")
print()

#NOT: aynı dosya içinde aynı isimle iki fonksyon üretilirse python öncekileri geçersiz kılar sadece sonuncuyu önemser

#How to Return a Value from Function
#fonksyonlarla kodları uzaklara götürmek abstraction olarak bilinir. Abstraction: Soyutlama, bir yazılım bileşeninin iç işleyişini gizleyip, sadece kullanıcıya gerekli olan arayüzü göstermektir

def greet_2(name):
    if name == "hatice":
        return "oo nabıyon lan " + name #bu şekilde return'e değer verilir
    return "merhabalar greet_2 çıktısı " + name 

returned = greet_2("ikra") #bu şekilde kullanılır
print(returned)
print(greet_2("hatice"))
print()

#Default Parameters : normalde parametre alan fonksyonları argümansız çağıramazsın 
# eroor verir bu şekilde: TypeError: greet_2() missing 1 required positional argument: 'name', 
# hem bunu engellemek için hem de argüman verilmemesi durumu için kodu tekrar yazmamak için böyle bir şey bulmuşlar

def greet(name = "users"): #argüman verilmezse "users" kullanılacak verilirse gelen yeni değer kulllanılacak
    if name == "rabia":
        return "hoş geldin anam, greet'den rabia ile çıkıldı"
    return "hey there " + name 

print(greet())
print(greet("rabia"))
print()

#Multiple Arguments / Parameters:
def greet(name = "Users" , be_nice = True):
    if not be_nice:
        return "MUL/ nabıyon lan burda " + name
    return "MUL/ hoş geldiniz ne arzu edersiniz" + name

print(greet("iclal" , True)) #bu şekilde birden fazla argüman verebiliriz ama birini eksik yazamayız error veriyor 
#tek birini verirsen bu şimdi hangisi diye düşünüyor
print()

#Keyword Arguments: defalt parametrelerin defalt kalması ve eroor aldan deiğer değerlere argüman geçebilmemizi sağlar
def greet(name = "Users" , be_nice = True):
    if not be_nice:
        return "KEY/ nabıyon lan burda " + name
    return "KEY/ hoş geldiniz ne arzu edersiniz" + name

print(greet(be_nice=False)) #bu şekilde bir değerin argümanını vermesek bile argümanın hangisine gideceğini karıştırmaz 
#defalt parametrelrle bu şekilde kullanılabilir

#bu durum print fonksyonu için de geçerli: normalde print(x, y, end=" ") yapıyoruz 
#bunu yaparken arka planda print'in end isimdeki parametresinin değerini Key parameters ile değiştiriyoruz.
#yani aslında def print(values, end="/n") idi biz değiştirdik
print()

#Passing Arguments by Keyword or Position
def greet(name = "Users" , be_nice = True):
    if not be_nice:
        return "PAS/ nabıyon lan burda " + name
    return "PAS/ hoş geldiniz ne arzu edersiniz" + name

print(greet("kite" , be_nice=False)) # Position arguments Keyword argument'den sonra gelemez
#SyntaxError: positional argument follows keyword argument error u alınır.
#aynı printteki gibi : print(end=" " , x) olmaz error verir
print()

#Positional Only Parameter: kimi parametrelerin sadece positional olarak çağırılmasını isteriz. Böyle parametrelerin yanına / konur.
# / dan önceki parametreler positional only olur. Onlara Keyword olarak passing yapmak istediğimizde:
#  TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name' error verilir

""" Neden? : 
1. API'nin kontrolünü sıkılaştırmak
Eğer bir fonksiyonun belirli parametrelerini sadece konumla geçilmesini istiyorsan, kullanıcıların keyword ile çağırmasını engelleyebilirsin.

Böylece fonksiyonun nasıl çağrılacağını sen belirlemiş olursun, bu da standart kullanım sağlar.

2. Parametre isimlerini gizli tutmak
Bazen bir parametrenin ismi gelecekte değişebilir, ama fonksiyonun çağrılma şeklinin etkilenmesini istemezsin.

Position-only ile kullanıcı parametre ismine bağımlı olmaz → isim değiştirsen bile kırılmaz.

3. Özel kullanım durumları
Bazı built-in veya C-extension fonksiyonlar zaten position-only parametreler kullanır (len(obj) gibi).
"""

def greet(name = "Users", / , be_nice = True):
    if not be_nice:
        return "POS/ nabıyon lan burda " + name
    return "POS/ hoş geldiniz ne arzu edersiniz" + name

print(greet("ikbal" , be_nice = False))
print()

#Keyword Only Arguments: sadece Keyword olarak passing edilecek parametreleri belirlemek için kullanılır. 
# * dan sonra gelenler sadece Keyword olur, arada kalanlar iki türlü de kullanılabilir
""""
neden?
1. Anlaşılır Fonksiyon Çağrıları
2. Yanlışlıkla Karışan Argümanların Önüne Geçmek
3. API Stabilitesi ve Geleceğe Hazırlık
Yeni parametreler eklediğinde eski çağrıları bozmadan ilerleyebilirsin. Keyword-only sayesinde eski kodlar kırılmaz, yeni parametreler daha kontrollü şekilde tanımlanır.
4. Kullanıcıyı Düşünmeye Zorlamak
Bazı argümanlar kritikse ve çağıranın dikkatlice karar vermesi gerekiyorsa, keyword-only tanımlamak onun bu parametreyi fark etmesini sağlar.
"""
def greet(name, / , mix , * ,be_nice = True):
    if not be_nice:
        return "KEY/ nabıyon lan burda " + name
    return "KEY/ hoş geldiniz ne arzu edersiniz " + name + mix

print(greet("selam" , mix = "ikisi de olur" , be_nice=False))
print()

#Function to Work with Lists
def greet_all(people):
    for person in people:
        print("FUN/ Hello " + person)

friends = ["hüreyde" , "adil" , "fatma"]

greet_all(friends)
print()

#Function Taking Unlimited Arguments (Packing): parametrenin bsşıns konan * işareti gelen birden fazla argümanı 1 parametreye indirir. PACKİNG yapar. 
# aksi takdirde TypeError: greet_all() takes 1 positional argument but 3 were given error alınır
def greet_all(*people):
    for person in people:
        print("FUN2/ Hello " + person)

greet_all("hasan" , "rabia" , "elif")
print()

#Unpacking Data: bir argümanı birden fazla parametreye vermek istediğimizde bunu kullanırız. 
#argümanı verirken başına * işareti konur. 
#unpacking: paketlenmiş veriyi açıp tek tek sanki birden fazla veri varmış gibi verir
#aksi takdirde TypeError: print_info() missing 2 required positional arguments: 'age' and 'email' error alınır
def print_info(name, age, email):
    print("FUN3/ " + name + " is " + str(age) + ". Reached at " + email)

info = ["iclal", 20, "iclalozturkts@gmail.com"]

print_info(*info) #önce birinci elemana ulaşacak sonra 2 sonra 3...
print()

#Functions Calling Functions: fonksyon içinde başka fonksyonu çağırabiliriz: 
# fonksyonda kullanmak istediğimizde hali hazırda tanımlı olması için program aşağıdan yukarı çalışmış gibi oldu
def greet(person, first_time=False):
    if first_time:
        return "FUN4/ ooo ilk ha hoş geldin " + person
    return "FUN4/ hoş geldin" + person

def greet_all(people):
    for person in people:
        print(greet(person, True))

people = ["zeynep", "beyza", "ayşe"] #hepsinin değişken kapsamı (scope)'u farklı olduğu için karışmıyorlar

greet_all(people)
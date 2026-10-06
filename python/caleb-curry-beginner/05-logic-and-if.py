#Boolean and Comparison Operators
age = 5
can_vote = age > 18 #can_vote boolean türünden bir değişkendir ve True ve False değerlerini alabilir
print(can_vote)

#İf Statement
if age > 18:
    can_vote = True
    print("artık oy kullanabilirsiniz") #satır sınırlaması yok, süslü parantez yok tab da ise ifin içindedir

print(can_vote)

#if elif else
if age >= 65:
    print("oo akbil bedava")
elif age == 61:
    print("trabzoon")
elif age > 18:
    print("eh işte idare eder")
else :
    print("oo bebe")

happy = False
if happy:
    print(":)")
else:
    print(":(")

#or Operator (Intro to Logical Operators)
name = "İclal"
if name == "iclal" or "İclal":
    print("name is iclal")
if False or print("heey bura boş"): #ilk durum doğruysa diğerini hiç umursamaz or operatöründe birinin doğru olması yeterli
    print("buranın önemi yok ")

#and Operator
reagent = False
point = 50

if reagent and point < 100: #and operatöründe ikisininde doğru olması lazım
    print("and if'ine girildi")

#not operator
subscribe = False
if not subscribe:
    print("please subscribe")

print("A != B" , "A" != "B ")

#Control Flow and Logic Review(Kontrol Akışı ve Mantık (Gözden Geçirme Tekrar))
my_grades = [100, 100, 100]
your_grades = [95, 99, 92]
print("same grades?:", my_grades == your_grades)
your_grades = [100 , 100, 100]
print("same grades?" , my_grades == your_grades) #böyle değerleri karşılaştırırız 

print("are grades the same object?" , my_grades is your_grades) #ifade ettikleri objectleri karşılaştırır
print("are grades the same object?" , my_grades is my_grades)

print("is A before B?" , "ABC" < "BCD")
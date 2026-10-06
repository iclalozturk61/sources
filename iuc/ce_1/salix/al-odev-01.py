####### 1.Soru #######
#a ve b yi yer degiştirmemiz gerek lakin yalnızca atama işlemi ile yapamayız. 
#Override eder bunu engellemek için de a nın ilk değerini güvende tutacak bir temp değişkeni tanımladım:

print("A ve B sayılarını giriniz: ")
a = int(input("A sayisi: "))
b = int(input("B sayisi: "))    

print(f"Girdi: a={a}, b={b}")

temp = a 
a = b #
b = temp

print(f"Çıktı: a={a}, b={b}")



####### 2.Soru #######
print("Bir cümle giriniz:")
sentence = input()

firstCharecter = sentence[0]
lastCharecter = sentence[-1]
print(f"Cümlenin ilk karakteri: {firstCharecter}, son karakteri: {lastCharecter}")

lengthOfSentence = len(sentence)
print(f"Cümlenin uzunluğu: {lengthOfSentence}")

reversedSentence = sentence[::-1]
print(f"Cümlenin ters hali: {reversedSentence}")    



####### 3.Soru #######
print("A ve B sayılarını giriniz: ")
a = int(input("A sayisi: "))
b = int(input("B sayisi: "))    

print("Lütfen yapmak istediğiniz işlemi giriniz: (toplama, çıkarma, çarpma, bölme)")

operation = input().lower()

match operation:
    case "toplama":
        print(f"a + b = {a+b}")
    case "çıkarma":
        print(f"a - b = {a-b}")
    case "çarpma":
        print(f"a * b = {a*b}")
    case "bölme":
        print(f"a / b = {a/b}")
    case _:
        print("Geçersiz işlem girdiniz.")



####### 4.Soru #######
print("Kenar uzunluklarını giriniz:")
side1 = int(input("1. Kenar: "))
side2 = int(input("2. Kenar: "))
side3 = int(input("3. Kenar: "))

triangleRules = (side1 + side2 > side3) and (abs(side1 - side2) < side3)

if triangleRules:
    if side1 == side2 == side3:
        print("Eşkenar üçgendir")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("İkizkenar üçgendir")
    else:
        print("Çeşitkenar üçgendir")
else:
    print("Bu kenarlarla bir üçgen oluşturulamaz.")



####### 5.Soru #######
print("Bir pozitif sayı giriniz:")
number = int(input())

if number < 0:
    print("Lütfen pozitif bir sayı giriniz.")
    exit()

checkingSqrt = (number ** 0.5).is_integer()

if checkingSqrt:
    print(f"{number} sayısı tam karedir")
else:
    print(f"{number} sayısı tam kare değildir")
    


#Getting User Input
""""
print("give us a number:")
number1 = input()
print("another:")
number2 = input()
print(number1 + number2) #örn: 8+10=810 yazıyor çünkü input string türünde dönüyor retun olarak
"""

#Type Casting
print(type(int("5"))) #type komutu değişkenin hangi veri tipinde olduğunu verir

""""
print("what is your favorite number?")
fav_num1 = int(input()) #inte çevirerek 199.satırdaki sorunu çözeriz, input direk string alır
print("other?")
fav_num2 = int(input())
print(fav_num1 + fav_num2)
print("any decimal?")
fav_num3 = float(input())
print(str(fav_num1) + "+" + str(fav_num2) + "=" + str(fav_num1 + fav_num2)) #str() siz olmazdı print kendi içinde string ve int değişkenlerini toplayamaz
print(fav_num1 + fav_num2 + fav_num3) #float ve int değerleri için hata vermez
"""
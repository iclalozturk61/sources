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
#35 - How to Convert String to List using split: 
msg = "Pay attention, to, everything I ,say"

words = msg.split() #defalt: boşluklara göre böler
print("35- ", words)

words = msg.split(",") #bir vürgülden diğerine kadar, eğer virgüllerle ayrılmış bir liste varsa iyi bir yöntemdir.
print("35- ", words)

words = msg.split(", ") #virgül sonrası boşluklu bir liste varsa iyi bir yöntemdir.
print("35- ", words)

words = msg.split("t") #ayırıcıların arasında başka bir şey olmaması durumuna örnek. 
print("35- ", words)

#36 - Split String by New Line
msg = """Pay attention, 
to everything 
I say"""

words = msg.split("\n") #satırlardan bölünmek isterse böyle  yapılır
print("36-", words)
 
msg = """\ 
Pay attention, \ 
to everything 
I say \
""" 
# pythonda """ """ arasına konan \ işareti o satırı aşağı indirme anlamına gelir orda alt satıra geçmez
# ama \dan sonra boşluk varsa python onu strinigin içinde gerçekten de \ var dşye yorumlar ve orda alt satıra geçer 
# ve yazdırırken de \\ şeklinde yazdırır kaçış ifadesi kullanır.

words = msg.split("\n")
print("36-", words)

#37 - Fill List from User Input
"""
print("Sup nerd tell us your favorite veggies.")
print("Example input (seperated by spaces):")
print("patlican salatalık domates kabak")

data = input()

favs = data.split()

for food in favs:
    print("37- yoo said:", food)
"""

#38 - Loop to Fill List From User Input:
"""
print("Sup nerd tell us your favorite veggies.")
print("hit enter after each food. q for quit")

favs = []

while True:
    data = input()
    if str.lower(data) == 'q':
        break
    favs.append(data)

for food in favs:
    print("38- ", food)
"""

#39 - Create a Stack - Use a List as a Stack
#Stack, yığın anlamına gelir. LIFO - Last In First Out prensibiyle çalışır. 
#Yani son eklenen ilk çıkar. Bu yüzden stack veri yapısı olarak kullanılır.
#list veri yapısı ile stack oluşturulabilir. özel bir yazımı felan yok list yazar gibi kullanılır. Kullanımı farklı yazımı aynı.
# path ve backtrack içeren uygulamalarda kullanılır. 

#stack ankaşılsın diye örnekler
stack = []
stack.append("Plate A")
stack.append("Plate B") 

print("39- ", stack.pop())  # LIFO - Last In First Out ilk B çıktı çünkü son eklenen B idi
print("39- ", stack.pop())  # PHILO - Pirst in Last Out ilk A girdi bu yüzden A son çıkacak
"""
#uygulama içi kullanım örneği
print("Sup nerd tell us your favorite veggies.")
print("hit enter after each food. r  for remove q for quit")
favs = []
while True:
    data = input()
    if str.lower(data) == 'q':
        break
    elif str.lower(data) == 'r':
        print("39- you just removed", favs.pop())
        continue
    favs.append(data)
    print("39- ", favs)

for food in favs:
    print("39- ", food)
"""

#40 - Create a Queue - Use a List as a Queue
#Queue, kuyruk anlamına gelir. FIFO - First In First Out prensibiyle çalışır.
#Yani ilk eklenen ilk çıkar. Aynı gerçek sıradaki gibi ilk gelen ilk girer, işleme alınır ilk çıkar.
#list veri yapısı ile queue oluşturulabilir. özel bir yazımı felan yok list yazar gibi kullanılır. Kullanımı farklı yazımı aynı.
"""
#queue ankaşılsın diye örnekler
queue = []

queue.append("data 1")
queue.append("data 2")

print("40- ", queue)
queue.pop(0)
print("40- ", queue)
    
#uygulama içi kullanım örneği
print("Sup nerd tell us your favorite veggies.")
print("hit enter after each food. r  for remove q for quit")

favs = []

while True:
    data = input()
    if str.lower(data) == 'q':
        break
    elif str.lower(data) == 'r':
        print("40- you just removed", favs.pop(0)) #0 yazmak yetiyor her daim ilk eleman olacak zaten
        continue
    favs.append(data)
    print("40- ", favs)

for food in favs:
    print("40- ", food)
"""
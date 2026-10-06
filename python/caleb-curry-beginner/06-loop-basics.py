#FOR LOOP
friends = ["iclal", "hatice", "sidre", "beyza"]

for friend in friends:
    print(friend)

#Print without Newline using end Parameter
for friend in friends:
    print(friend, end = " ") #defalt olarak gelen print sonrası alt satıra geçmeyi iptal edip " " ekliyor.
print()#en sonda defalt olarak alt satıra geçmesi için yapıldı

#range() fonction
for i in range(10): #for(i = 0; i < 10; i++) nın işini yapıyor range(STOP) ANLAMINA GELİR TEK PARAMETRE VERİLİRSE
    print(i, end=" ")
print()

#Range Starting Position
for i in range(15,35,5):  #range(START , STOP , STEP(ARTIŞ MİKTARI))
    print(i, end=" ")
print()

#Step in Range Explained
for i in range(200 , 1 , -1): #azaltma işlemi de yapılabiliyor
    print(i, end=" ")
print()

#Range Sum : belli bir düzendeki sayıların toplamını bulma yolları
print(sum(range(10))) #sum fonksyonu iterabledir (değiştirilebilir) bir döngü gibi işler, hepsini toplar

sum = 0
for i in range(10) : #sum() fonksyonu da aynı böyle çalışıyor
    sum = sum + i
print(sum)

#Create a List from Range
my_list = list(range(5))
print(my_list)

#for Loop with Index
friends = ["iclal", "hatice", "sidre", "beyza"]

for i in range(len(friends)):
    print(i , friends[i], end = " ")
print()
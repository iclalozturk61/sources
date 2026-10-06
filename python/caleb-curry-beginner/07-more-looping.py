#break 
flag = False #aranan değerin olmaması halinde "yoktur" yazmak için ben buldum flag yöntemini
friends = ["iclal", "hatice", "Sidre", "beyza"]
for friend in friends:
    print(friend)
    if friend == "sidre":
        flag = True
        print("sidreyi bulduk")
        break
if not flag:
    print("sidre yok burda")

#continue
friends = ["iclal", "hatice", "sidre", "beyza" , "sidre" , "sidre"]
for friend in friends:
    if friend == "sidre":
        print("sidreyi bu sefer de bulduk")
        continue #sadece döngüdeki bu stepi geçecek yani sidre bulunduğunda direk listenin bir sonraki elemanına geçecek,341 satırını işlemicek
    print(friend , "... bu sidre değil")

#else instead of continue
friends = ["iclal", "hatice", "sidre", "beyza" , "sidre" , "sidre"]
for friend in friends:
    if friend == "sidre":
        print("sidreyi bu sefer yine bulduk")
    else:
        print(friend , "... bu sidre değil")

#pass: kod iskelesini oluştururken daha ne yazacağını bilmediğin yerler yazılır örneğin
#if, for veya sınıf ve fonksyonların içleri olabilir, böylelikle python derler hata vermez
friends = ["iclal", "hatice", "sidre", "beyza" , "sidre" , "sidre"]
for friend in friends:
    if friend == "sidre":
        pass #normalde python bu kodu derlemez if'in içi boş diye

#else with for: 324. satırda flag ile yaptığım işin aynısını yapıyor
friends = ["iclal", "hatice", "sidre", "beyza" , "sidre" , "sidre"]
for friend in friends:
    if friend == "beyza":
        print("beyza buralarda")
        break
else: print("beyza yok burada") #break ile döngüden çıktıysan else ın içindeki komut önemsenmez ama breakle değilde normal yoldan çıktıysan elseın içindeki komut işleme alınır

#while Loop: fordan pek farkı yok sadece daha detaylı görünümü var tercih meselesi, update i istediğin yerde yapabilmen işine gelebilir
i = 27 # 1-initilazation(tanımlama)
while i >= 0: # 2-conditon(koşul)
    print(i, end=" ")
    i -= 3 # 3- update

#else with while loop
numbers = [0, 1, 5, 8, 9, 45, 27, 3]

square = 500
i = 0
while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i] , "squarede more than" , square)
        break
    else: print(numbers[i] , "squared less than" , square)
    i += 1
else: print("none of their squared more than" , square)

#flag with while loop
numbers = [0, 1, 5, 8, 9, 5, 8, 3]

flag = False
square = 500
i = 0
while i < len(numbers):
    if numbers[i] ** 2 > square:
        print(numbers[i] , "squarede more than" , square)
        flag = True
        break
    else: print(numbers[i] , "squared less than" , square)
    i += 1
if not flag: #else ile aynı görevi görüyor tercih meselesi
    print("None of them large enough!")

#do while loop: pyhonda do while yok ama taklitleri var
i = 0
print(i) #ya ilk aşamayı yukarıda yapıp do while a benzetecen
while i < 10:
    print(i)
    i += 1

i = 0
while True: #veya böyle yazılır, 
    print(i)
    i += 1
    if i > 9:
        break

#sentinel loop / indefinite loop
print("Do you want to continue? Y/N")
response = input()
while response == "Y": #ne zaman biteceği baştan belli olmayan döngü 
    print("Do you want to continue? Y/N")
    response = input()
print("birinci infinite looptan çıkıldı")

while True:
    print("Do you want to continue? Y/N")
    response = input()
    if response != "Y":
        break
print("ikinci infinite looptan çıkıldı")

#sentinel loop / indefinite loop örnekleri
while True:
    print("Do you want to continue? Y/N")
    response = input()
    if response != "Y" or response != "y": #bu şekilde response != Y gerçekleşmesi durumunda direk içine giriyor ikinci koşula bakmıyor
        break
print("üçüncü infinite looptan çıkıldı")

while True:
    print("Do you want to continue? Y/N")
    response = input()
    if response != "Y" and response != "y": #böyle olur Y değilse y de değilse çık
        break 
print("dördüncü infinite looptan çıkıldı")

while True: 
    print("Do you want to continue? Y/N")
    response = input()
    if response == "Y" or response == "y": # böyle de olur sıkıntı yok 
        continue
    break
print("beşinci infinite looptan çıkıldı")

#lower and upper fonksyon
while True:
    print("devam etmek istiyor musunuz?")
    response = input()
    if response.lower() == 'y': #alışkanlık olarak kullanıcıdna gelen değer sağa yazılıyor yoksa ilk olarak upper fonk. yapılacak normalde işlem sırası gereği if 'y' == respoonse.upper() olmalı
        continue #kullanıcıdan gelen bilgiyi küçük harfe çeviriyor sonra 'y' ile karşılaştırıyor
    break
print("altıncı infninite döngüden çıkıldı")

while True:
    print("devam etmek istiyor musunuz?")
    response = input()
    if 'Y' == response.upper(): #kullanıcıdan gelen bilgiyi büyük harfe çeviriyor sonra 'Y' ile karşılaştırıyor
        continue
    break
print("yedinci infninite döngüden çıkıldı")

#isupper() ve islower()
while True:
    print("continue? N/Y")
    response = input()

    if response.isupper() : #string türündeki karakterlerin büyük mü küçük mü yazıldığını kontrol eder.
        print("TAMAM BAĞIRMA")

    if response.islower() : #bir karakteri bile koşulu sağlamazsa False döner
        print("DUYAMADIM")
    
    if response.upper() != 'Y':
        break
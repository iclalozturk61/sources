#13 - Insert into List: .insert komutuyla listelere ekleme yapılabilir. 
# İlk olarak eklemek istediğimiiz index num veriyoruz sonra eklemek istediğimiz veriyi veriyoruz. 
# Eklediğimiz veriden sonrakilerin index numaraları kayacak onu da unutmamak lazım.
workdays = ["monday", "tuesday", "thursday", "friday"]

print("13- ", workdays[3])

workdays.insert(2, "wednesday")

print("13- ", workdays[3])

print("13- ", workdays)
print()

#14 - Remove Item by Index from List with del and with remove: 
# remove'da veriyi bilmen gerekiyor index numa gerek yok, 
# del'de veriyi bilmene gerek yok index num lazım
#NOT: bunlar sildiğin veriyi saklamaz hiç bir şeyi return yapmaz 
workdays = ["monday", "tuesday", "thursday", "friday", "saturday"]
workdays.insert(2, "wednesday")
print("14- ", workdays)

workdays.remove("saturday")
print("14- ", workdays)

del workdays[2] 
print("14- ", workdays)
print()

# 15 - Remove Item from List with pop: pop ile bi şeyi silersek bize return ile sildiğimi şeyi geri döndürür 
# böylelikle hata olması durumunda kolaylıkla geri alınabilir. Ayrıca backtracking (geri izleme) ile çok iyi çalışır: 
# Eğer yol çıkmaza girerse, son yapılan seçim geri alınır → işte burada .pop() devreye girer!
workdays = ["monday", "tuesday", "thursday", "friday", "saturday"]
workdays.insert(2, "wednesday")

popped = workdays.pop(5)
print("15- " , "we just removed" , popped)
print("15- " , workdays)
print()

#16 - Slicing with del Operator:
workdays = ["monday", "tuesday", "thursday", "friday", "saturday"]
workdays.append("sunday")

del workdays[workdays.index("tuesday"): workdays.index("tuesday") + 3] #aralık belirterek silme yapabiliriz
print("16- ", workdays)
print() 

#17 - Removing all Occurrences of Item in List:
backpack = ["sword", "bag", "zihgir", "yay", "zihgir", "zihgir" ,
            "bardak", "bag", "zihgir", "yay", "zihgir", "zihgir",
            "sword", "bag", "salam", "yay", "tahta", "zihgir",
            "sword", "su", "zihgir", "ok", "zihgir", "zihgir"]

while backpack.count("zihgir") > 0: #teknik işe yarar ama iyi bir teknik değil çok fazla tekrarlanan iş var 
    #her bir zihgir için bütün listeyi baştan dönecek
    backpack.remove("zihgir")

print("17- ", backpack)
print()

#18 - Slicing a list and [:] Explained
print("18- ")
backpack = ["sword", "bag", "zihgir", "yay", "zihgir", "zihgir"]

backpack1 = backpack # bu şekilde atama onları aynı şeye işaret eder hale getiriyor aynı id verir
print(id(backpack) , id(backpack1)) 
print()

backpack2 = backpack[:] #: koyarak copy işlemi yapıyoruz içindeki veriler aynı ama aynı şey değil, id leri de bundan farklı zaten
print(id(backpack) , id(backpack2)) 
print()

print(id(backpack))
backpack[:] = [1, 2, 3] # REPLACE: :  koyduğum için içindekileri değiştirdim hala aynı şey aslında 
print(id(backpack))
print()

print(id(backpack))
backpack = [1,2,3] # böyle yaparsak artık başka bir liste olur
print(id(backpack))
print()

# 19 - Remove Elements From List within for Loop:
backpack = ["zihgir", "bag", "zihgir", "yay", "zihgir", "zihgir", "fitness" ]
            
for item in backpack: #backpack[:] diyerek çözülebilir
    print("19- ", item) 
    if(item == "zihgir"):
        backpack.remove(item)

print("19- ",backpack)
 #ASLA FOR DÖNGÜSÜ KULLANARAK LİSTEDEN BİR ŞEYLER SİLME
""""
AÇIKLAMA: 
    Listeyi üzerinde dönerken aynı anda değiştirmek, Python'da sık karşılaşılan bir hata kaynağıdır.  
for item in backpack döngüsü, listenin orijinal uzunluğuna göre sabit bir indeksleme uygular.  
Ancak sen, backpack.remove(item) ile eleman silince, Python arka planda indeksleri kaydırır 
bu da bazı "pizza slice" öğelerinin atlanmasına neden olur.

    Başladı ilh zihgiri sildi artık 2. elemana bakması lazım ama biz 1 eleman sildiğimiz için artık 
ikinci eleman eskiden 3. olan 2.zihgir, zihgirler hep bir arayla dizildiyse sıkıntı yok ama 
iki zihgir arka arkaya gelirse atlanma olur


"""
print()

#Diğer çözüm yolu, yeni liste oluşturmak
backpack = ["zihgir", "bag", "zihgir", "yay", "zihgir", "zihgir", "fitness" ]

new_backpack = []

for item in backpack:
    if item != "zihgir":
        new_backpack.append(item)

print("19- ",new_backpack)
print()
        
#20 - Remove Elements using List Comprehension
backpack = ["zihgir", "bag", "zihgir", "yay", "zihgir", "zihgir", "fitness" ]

backpack[:] = [item for item in backpack if item != "zihgir"]

print("20- ", backpack)
print()

#21 - How to Use reverse Method with Lists:
data = [1, 2, 3, 4, 5]

data_copy = data[:]

data_copy.reverse() #argüman almaz, değer dönmez direk listeyi tersine döndürür o yüzden eski hali korunmak isteniyorsa kopya oluşturulur

print("21- ", data_copy)
print()

#22 - How to Swap Variables and List Elements:
##1.yol##
me = "iclal"
you = "idc"

me, you = you, me #bu python'ın sağlamış olduğu bir kolaylık böyle swap değiştirme yapılabilir
print("22-1- ", me, you)

##2.yol##
me = "iclal"
you = "idc"

temp = me
me = you
you = temp #depo değişken kullanarak swap, diğer dillerde fln kullanılır 
print("22-2- ", me, you)

##3.yol##
data = ["a", "b", "c", "d","e", "f"]

for index in range(len(data) // 2): #// integer olarak ikiye bölme anlamına gelir, böylelikle eleman sayısı tekse ortadakine dokunmayacak sorun olmicak, 
    #çiftse de tam yarısı kadar gurup olmuş olacak zaten 
    data[index] , data[-index -1] = data[-index -1] , data[index] #örnek: b'nın indexi 1 e'ninki -2 yani direk -index diyince olmuyor sıfır yüzünden bir tane geri çekmek lazım 

print("22-3- ", data)

##4.yol##: başka liste üretip ilk listeyi sondan başa olarak atamak:
data = ["a", "b", "c", "d","e", "f"]
data_reverse = []

for item in reversed(data): #reversed() fonksyonu data'yı değiştirmez sadece reversed halini döndürür
    data_reverse.append(item)

print("22-4- ", data, data_reverse)

###5.yol###: slicing list yöntemi:
data = ["a", "b", "c", "d","e", "f"]

data[:] = data[::-1] #2. :'den sonrası step yani karakterler arası nasıl geçiş yapılacağıdır. [::-1] yapınca sondan geriye gelmiş oluruz.

print("22-5- ", data)
print()





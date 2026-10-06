#**********************STRING************************
# #escape characters
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
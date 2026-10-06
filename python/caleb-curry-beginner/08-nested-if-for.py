"""
nested if: iç içe ifler anlamına gelir
*and ve or ile benzer kodlar yazılabiliyor ama anlaması zorlaşıyor ve karmaşık hale geilyor, gözden kaçan durumlar olabiliyor, 
buglar çıkabiliyor.
*eğer ifin içinde hem and ler hem de orlar olacaksa karışık kullanım yerine nestede if önerilir
"""
logging = True
logging_in = False  
name = "iclal"

if logging:
    if logging_in:
        print("ooo welcome" + name)
    else:
        print("welcome someone")
     

age = 25
fun = False
likes_to_dance = False

if (age < 30 or fun) and likes_to_dance:
    print("you are invited")
else:
    print("sit down on your seat")

if age < 30 or fun:
    if likes_to_dance:
        print("you are invited too")
    else:
        print("you dont know dance?")
else:
        print("sit down in your home")
    

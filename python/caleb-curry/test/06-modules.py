#48 - Intro to Modules
"""
🧩 Python Modülleri Hakkinda Kisa Not
Modül nedir? Python’da .py uzantili, belirli işlevleri barindiran dosyalardir. Kodun parçalanarak daha düzenli ve tekrar kullanilabilir hale gelmesini sağlar.

Ne işe yarar?
Kodun okunabilirliğini artirir
Fonksiyonlari ve siniflari gruplandirir
Başka projelerde tekrar kullanilabilir
Karmaşik yapilari sadeleştirir

Nasil kullanilir?
import modul_adi ile içeri aktarilir
from modul_adi import fonksiyon_adi ile sadece gerekli kisimlar çekilir

Modül türleri:
📦 Yerleşik modüller: Python ile birlikte gelir (math, os, random)
🧪 Harici modüller: pip ile yüklenir (requests, numpy)🛠️ Kendi modüllerin: Projeye özel yazdiğin .py dosyalari

Dosya gezgininde modül incelemek:
Fonksiyonlari, siniflari ve değişkenleri görerek modülün ne işe yaradiğini anlayabilirsin
__init__.py varsa, bu klasör bir paket olarak tanimlanmiştir

Pythondaki modullerin indexleri: https://docs.python.org/3/py-modindex.html
"""

# 49 - from module import Explained
from random import randint, seed
print("49-1 ", randint(0,10))
# print(type(random)): böyle yazdıramayız artık çünkü random un tamamını eklemedik NameError: name 'random' is not defined uyarısı alırız

print("49-2", type(seed))

"""
Bu durumun pros(avantajı) ve cons(dezavantajı) nedir?
Pros: prefix(ön ek) gerekmeden kullanım sağlar. random. demek zorunda değiliz
Cons: bu isimlerde başka değişken kullanamyız artık aşağıda örnek olacak:
"""
seed = "apple"
print("49-3", seed) #en son seed e ne atanmışsa onu yazacak şuan apple

from random import seed
print("49-4 ", seed) #şuan <bound method Random.seed of <random.Random object at 0x000001A7C5B2D590>> verir en son import edildi çünkü, aliasing olarak da adlandırılır bu durum

#50 - How to Alias an Import (import as)
"""
Aliases nedir? Daha önce listelerin birbirine atanmasinda karşilaşmiştik, yeniden adlandirma veya farkli isimle çağirmak gibi düşünülebilir.
list1 = list2 gibi şeyler yapmiştik birinci caleb curry birinci oynatma listesinde kopyalama bölümünde. Şimdi ise bu özelliği kisaltma için kullanicaz:
Örnek:
def uzun_fonksiyon_adi(x):
    return x * 2

kisa = uzun_fonksiyon_adi
print(kisa(5))  # Çikti: 10

Aslinda rename yapmiş oluyoruz, başka bir isimle erişerek. Bundan sonra eski ismi ile çağirmaya çalişsak bile not defined error verecek. Ve başka değişkenler için kullanabileceğiz ayni ismi.
"""

import datetime as dt #datetime modulunu rename yaptık dt ile 

datetime = 12

print("50- ", datetime, dt.datetime.now()) #şuan datetime 12 ye eşitlenmiş durumda, dt ile datetime moduluna erişebiliyoruz. dt.datetime.now() sistem saatien ve gününe ulaşıp yazar

# 51 - Why you should NEVER import *
"""
import * ne işe yarar?
    o modulun içindeki bütün fonksyonları almış olursun.
Pros:
    - Kısa ve hızlı kullanım sağlar. Bu sayede modul adını yazmadan direkt fonksiyonları kullanabilirsin. Örnek:
        from math import *  # Artık math.sqrt() yerine direkt sqrt() yazabilirsin.
    - Modülün tüm içeriğini tek seferde alır.
Cons:
    - İsim çakışmalarına neden olabilir. (Pek çok modul import edildiği zaman, aynı isimde fonksiyonlar varsa hangisinin kullanılacağı belirsizleşir.)
    Örnek:
        from math import *
        from random import *
        print(sqrt(16))  # Hangi sqrt() kullanılıyor? Math mi, Random mı?
    - Kodun okunabilirliğini azaltır.
"""
print("51- ", dir()) #dir() fonksiyonu, mevcut isim alanındaki tüm isimleri listeler. Yani şu an hangi modüllerin ve fonksiyonların yüklü olduğunu gösterir. Mesela şuan datetime', 'dt', 'randint', 'seed'var. Eğer import * yaparsak, bu liste daha da uzayacak ve hangi fonksiyonun nereden geldiğini anlamak zorlaşacak.

# 52 - How to Create Your Own Module 
"""
-Modul hiç yoksa verdiği hata: ModuleNotFoundError: No module named 'utils'
-Modulu bulmuşsa ama içindeki fonksyona erişemediyse vereceği hata: AttributeError: module 'utils' has no attribute 'stats_range'
-Modul üretince otomatik _pycache klasörü oluşuyor. Bu klasör, modülün derlenmiş (bytecode) halini içerir. Python, modülleri ilk kez yüklediğinde bu klasörü oluşturur ve sonraki yüklemelerde daha hızlı erişim sağlar.
-İsim çakışmasını önlemek için:
    İsim çakışması şu durmlarda olur:
        1. Modulun kendi içinde hali hazırda yerleşik bir fonksiyonun ismi ile aynı isimde bir fonksiyon varsa
        2. Çakışacak isimde fonksiyon veya değişken içeren modulleri from ... import ... yaparsak
    Çözüm yolları:
        - ya modulun içindeki foksyonun adını range yapmayacaz 
        - ya da utils.range diye çağırcaz 
        - ya da from utils import range dicez. Böyle yapınca:
            yerleşik range ulaşmak için başka yollar bulmamız gerekir çünkü bizim range onu gölgeler. Yollar:
                1. __builtins__ üzerinden erişim: print("Yerleşik range:", __builtins__.range(5)) şeklinde.
                2. Başta alias ile saklama (önceden yakalama)
                3. from builtins import range şeklinde yaparak, yerleşik range'i direkt kullanabiliriz.
                    _builtin_range = range  # yerleşik olanı sakladık
                    from utils import range  # artık range senin özel fonksiyonun
                    print("Özel range:", range([1, 2, 3]))
                    print("Yerleşik range:", _builtin_range(5))
                4. builtins modülünü import etmek

   
""" 
#*from utils import range 
#*print("52- ", range([1,2,5,14,2,89,-8])) 

# 53 - Sys.path and Changing Module Paths
"""
Sys modulu kullanılırken neden genelde interaktif moda geçilir? 
    -Çünkü sys modülü, Python'un çalışma ortamı hakkında bilgi sağlar ve bazı ayarları değiştirmeye olanak tanır. 
    -İnteraktif modda, bu ayarları anında test etmek ve görmek daha kolaydır. 
    -Ayrıca, sys modülü genellikle komut satırı argümanlarını işlemek veya Python'un çalışma ortamını incelemek için kullanılır, bu tür işlemler interaktif modda daha pratiktir.
Örnek sys fonksiyonları:
import sys
print(sys.version)  # Python sürümünü gösterir
print(sys.platform)  # Çalıştığınız platformu gösterir (örneğin, 'win32', 'linux', 'darwin')
print(sys.path)  # Python'un modül arama yollarını gösterir
print(sys.argv)  # Komut satırı argümanlarını gösterir

sys.ps1 nedir?
    -sys.ps1, Python'un interaktif kabuğunda (REPL) kullanılan bir değişkendir. 
    -Bu değişken, kullanıcıya komut girmesi için gösterilen birincil istemi (prompt) temsil eder. 
    -Varsayılan olarak, sys.ps1 değeri '>>> ' olarak ayarlanmıştır, bu da kullanıcıya yeni bir komut girmesi gerektiğini belirtir.
    -Eğer kullanıcı özel bir istem (prompt) belirlemek isterse, sys.ps1 değerini değiştirebilir. 
    
    Örneğin:
        import sys
        sys.ps1 = ">>> "  # Varsayılan istem    
        sys.ps1 = "~~~ "  # İkincil istem (örneğin, devam eden satırlar için)

sys.path nedir?
    -sys.path, Python'un modül arama yollarını içeren bir listeyi temsil eder. 
    -Python, bir modül import edildiğinde, bu listeyi kullanarak modülü bulmaya çalışır. 
    -Liste, Python'un standart kütüphane dizinlerini, kullanıcı tarafından eklenen dizinleri ve çalışma dizinini içerir.
    -Eğer bir modül sys.path'te belirtilen dizinlerde bulunamazsa, Python "ModuleNotFoundError" hatası verir.
    -sys.path'i değiştirmek, Python'un modül arama davranışını etkileyebilir. Örneğin, sys.path.append("konum bilgisi") ile yeni bir dizin ekleyerek Python'un o dizinde bulunan modülleri de aramasını sağlayabilirsiniz.
    -Bu, özellikle projelerinizde özel modüller kullanıyorsanız veya belirli bir dizindeki modülleri öncelikli olarak kullanmak istiyorsanız faydalı olabilir.

    -Python import sırasında bu listedeki dizinleri sırayla tarar. Aynı isimde iki modül varsa, ilk bulduğunu yükler. 
        İşte bu yüzden alias çakışmalarında veya özel modül yazarken sys.path'in sırası kritik hale gelir.
    
    -Proje dışı dizinler sys.path.append("konum") denmeden import edilemez.  → Başka bir klasördeki modülü doğrudan import etmek istersen, sys.path'e manuel eklemen gerekir.
"""

import sys
print("53- ", sys.path) #

#import utils #böyle yaparsak utils modülünü bulamaz çünkü sys.path içinde yok, başka klasörde olduğu için erişilemiyor.
#sys.path.append("c:\\Users\\user\\source\\python\\caleb-curry") #böyle yaparsak utils modülünü import edebiliriz AMA KONUMU AÇIKÇA YAZMAK İSTEMİYORSAN:

from os.path import dirname, abspath
current_dir = dirname(dirname(abspath(__file__))) #şu anki dosyanın klasörünü verir NASIL?: 
sys.path.append(current_dir)

"""
Parçalar Ne işe yarar?
__file__	               Bu dosyanın tam adı (örneğin main.py)
abspath(__file__)	       Dosyanın tam yolunu verir → C:/Users/Iclal/proje/main.py
dirname(...)	           Bu yolun klasörünü alır → C:/Users/Iclal/proje (kaç klasör yukarı çıkmak istiyorsak o kadar dirname ekleriz)
dirname(dirname(...))	   Bir üst klasöre çıkar → C:/Users/Iclal
"""

import utils  

print("53-", utils.range([1,2,5,14,2,89,-8])) 



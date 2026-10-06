def replace_ı_with_i(text):
    return text.replace("ı", "i").replace("İ", "I")  # Türkçedeki büyük 'İ' harfi genelde 'I' ile eşleşir

# Örnek kullanım:

metin ="""
#50 - How to Alias an Import (import as) 
Aliases nedir? Daha önce listelerin birbirine atanmasında karşılaşmıştık, yeniden adlandırma veya farklı isimle çağırmak gibi düşünülebilir. 
list1 = list2 gibi şeyler yapmıştık birinci caleb curry birinci oynatma listesinde kopyalama bölümünde. Şimdi ise bu özelliği kısaltma için kullanıcaz:
Örnek:
def uzun_fonksiyon_adi(x):
    return x * 2

kisa = uzun_fonksiyon_adi
print(kisa(5))  # Çıktı: 10

Aslında rename yapmış oluyoruz, başka bir isimle erişerek. Bundan sonra eski ismi ile çağırmaya çalışsak bile not defined error verecek. Ve başka değişkenler için kullanabileceğiz aynı ismi.
"""
print(replace_ı_with_i(metin))
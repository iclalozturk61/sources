"""
İclal Öztürk 
Salix Yapay Zeka Kuluçka 
Ödev-1
"""

def find_included_max(homes, budget):
    included_max = 0

    for home in homes:
        if home <= budget and home > included_max:
            included_max = home
            
    return included_max
    
emlak_ücretleri =  [1000000, 2400000, 18000000, 900000, 6000000, 7000000, 1500000, 20000000, 3000000, 1500000]

emlak_ücretleri.sort()
print(emlak_ücretleri)

print("Bütçenizi giriniz:")
budget = int(input())

included_max = find_included_max(emlak_ücretleri, budget)

if included_max == 0:
    print("Bütçeniz dahilinde uygun emlak bulunmamaktadır.")
else:
    print(f"Bütçeniz dahilinde alabileceğiniz en yüksek ücretli emlak: {included_max}")





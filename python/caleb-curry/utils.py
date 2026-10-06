import sys
def range(data):
    data.sort()
    return data[-1] - data[0]

print(sys.path) # sys.path ile pythonun modül arama yollarını görebiliriz. Buraya kendi klasörümüzü ekleyebiliriz.
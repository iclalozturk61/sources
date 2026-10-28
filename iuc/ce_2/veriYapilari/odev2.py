#node, stack ve queue sınıfları lab kayıtlarıyle aynı olduğu için yorum satırı eklenmemiştir.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")

        data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return data

    def is_empty(self):
        return self.top is None

    def size(self):
        return self.count

    def display_items(self):
        current = self.top
        items = []
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.head.data
        self.head = self.head.next
        if self.head is None: #son elemanı çıkardıysak:
            self.tail = None #kuyruk da none olmalı
        self.count -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self.count

    def display_items(self):
        current = self.head
        items = []
        while current is not None:
            items.append(current.data)  # Elemanları listeye ekliyoruz
            current = current.next
        return items

class Truck:
    def __init__(self, plaka):
        self.plaka = plaka
        self.packages = Stack()
        self.capacity = 5

class KSI: #kargo süreç izleme sınıfıdır işleri dışarıdan daha anlaşılabilir yönetmek için kullanılır
    def __init__(self):
        self.beklemeKuyrugu = Queue() #kuyruk olduğu için kuyruk türünde
        self.rampadakiTruck = None

    def addTruck (self, plaka):
        new_truck = Truck(plaka)
        self.beklemeKuyrugu.enqueue(new_truck)
        print(f"{plaka} kuyruğa eklendi.")

    def takeToRamp(self):
        if self.beklemeKuyrugu.is_empty():
            print("Kuyruk boş rampaya alınacak kamyon yok.")
            return

        if self.rampadakiTruck is not None:
            print("Rampa dolu başka kamyon alınamaz")
            return

        self.rampadakiTruck = self.beklemeKuyrugu.dequeue()
        print(f"{self.rampadakiTruck.plaka} rampaya alındı")

    def addPackages (self, paketNum):
        if self.rampadakiTruck is None:
            print("rampada araç yok yükleme yapılamaz")
            return

        if self.rampadakiTruck.packages.size() == self.rampadakiTruck.capacity:
            print("kamyon doldu daha yükleme yapılamaz")
            return

        self.rampadakiTruck.packages.push(paketNum)
        print(f"{paketNum} araca yüklendi")

    def removePackages(self):
        if self.rampadakiTruck is None:
            print("rampada kamyon yok paket alınamaz")
            return

        if self.rampadakiTruck.packages.is_empty():
            print("araçta paket yok geri alınamaz")
            return

        alinanPaket= self.rampadakiTruck.packages.pop() #direkt pop ile geri alabiliriz stack ayrıcalığı
        print(f"{alinanPaket} aractan indirildi")

    def removeTruckFromRamp(self):
        if self.rampadakiTruck is None:
            print("rampada kamyon yok çıkarılamaz")
            return

        print(f"{self.rampadakiTruck.plaka} rampadan çıkarıldı")
        self.rampadakiTruck = None

    def showWaitingTruck(self):
        if self.beklemeKuyrugu.is_empty():
            print("kuyruk boş")
            return

        print("Sıradaki kamyonlar:")
        trucks = self.beklemeKuyrugu.display_items()
        i = 1 #araçların sırasının yazılması istendiği için sayaç olarak kullanıldı
        for truck in trucks:
            print(f"{i}. {truck.plaka} bekliyor")
            i += 1

    def showRampTruck(self):
        if self.rampadakiTruck is None:
            print("Rampada kamyon bulunmamaktadır.")
            return

        print(f"Rampadaki Kamyon: {self.rampadakiTruck.plaka}")
        print("Paketler:")
        print("TOP")

        if self.rampadakiTruck.packages.is_empty():
            print("(Paket yok)")
        else:
            for paket in self.rampadakiTruck.packages.display_items():
                print(f" {paket} ")

        print(f"Kapasite: {self.rampadakiTruck.packages.size()}/{self.rampadakiTruck.capacity}")

    def searchPackage(self, target_code):
        if self.rampadakiTruck is None:
            print("Rampada kamyon yok.")
            return

        if self.rampadakiTruck.packages.is_empty():
            print("Kamyonda hiç paket yok.")
            return

        temp_stack = Stack()
        found = False
        count = 0

        while not self.rampadakiTruck.packages.is_empty():
            pkg = self.rampadakiTruck.packages.pop() #stack türündeki bir veriye index vb erişemediğimiz bu şekilde yapmaya mecbur kaldık, biraz işlem yoğunluğu var ama yapılabilecek bir şey yok
            temp_stack.push(pkg)
            if pkg == target_code:
                found = True
                break
            count += 1

        while not temp_stack.is_empty():
            self.rampadakiTruck.packages.push(temp_stack.pop())

        if found:
            print(f"{target_code} paketine ulaşmak için {count} paket çıkarılmalıdır.")
        else:
            print(f"Aranan paket bu kamyonda bulunamadı.")

if __name__ == "__main__":
    ksi = KSI()
    while(True):
        print("\nKARGO DAĞITIM MERKEZİ")
        print("1  Yeni kamyon ekle")
        print("2  Sıradaki kamyonu rampaya al")
        print("3  Kamyona paket yükle")
        print("4  Kamyondan paket indir")
        print("5  Kamyonu rampadan çıkar")
        print("6  Bekleyen kamyonları göster")
        print("7  Rampadaki kamyonu göster")
        print("8  Acil paket ara")
        print("0  Programdan çık")

        islem = input()
        if islem == "1":
            print("plakayı giriniz:")
            plaka = input()
            ksi.addTruck(plaka)

        elif islem == "2":
            ksi.takeToRamp()

        elif islem == "3":
            print("paket numarasını giriniz:")
            paketNum = input()
            ksi.addPackages(paketNum)

        elif islem == "4":
            ksi.removePackages()

        elif islem == "5":
            ksi.removeTruckFromRamp()

        elif islem == "6":
            ksi.showWaitingTruck()

        elif islem == "7":
            ksi.showRampTruck()

        elif islem == "8":
            target = input("Aranan paket kodunu giriniz: ")
            ksi.searchPackage(target)

        elif islem == "0":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")

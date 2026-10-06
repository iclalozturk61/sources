class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleCircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)

        #liste boşsa
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.head.next = self.head
            self.head.prev = self.head
            return

        #liste doluysa en sona eklme:
        newNode.prev = self.tail
        self.tail.next=newNode
        self.head.prev = newNode
        newNode.next=self.head
        self.tail = newNode

    def display(self):
        #liste boşsa:
        if self.head == None:
            print("liste boş")
            return

        current = self.head

        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def delete(self, data):
        #liste boşsa:
        if self.head is None:
            return
        
        #listede tek eleman varsa
        if self.head == self.tail:
            if self.head.data == data:
                self.head = None
                self.tail = None
            return       

        #listede birden fazla eleman varsa ve ilk eleman silinecekse:
        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            return

        #aradaki veya sondaki silme
        current = self.head.next
        while current != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    current.next.prev = current.prev
                    current.prev.next=current.next
                return
            current = current.next
        print("aranılan değer bulunmadı")



        
    def search(self, data):
        #liste boşsa:
        if self.head == None:
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False
                
                
my_list = DoubleCircularLinkedList()
my_list.append(4)
my_list.append(9)
my_list.append(1)
my_list.append(6)
my_list.append(3)
my_list.append(7)
my_list.append(2)

my_list.display()
print(my_list.head.data)
print(my_list.head.prev.prev.data)
print(my_list.head.next.next.next.next.next.data)


        


        


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        # Liste boşsa
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        # Son düğümü bul
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def search(self, data):
        if self.head is None:
            return False

        current = self.head
        while current.next != self.head:
            if current.data == data:
                return True
            current = current.next

        return False

    def delete(self, data):
        if self.head is None:
            return

        current = self.head
        previous = None

        while True:
            if current.data == data:

                # Head siliniyorsa
                if current == self.head:

                    # Tek eleman varsa
                    if self.head.next == self.head:
                        self.head = None
                        return

                    # Son node'u bul
                    last = self.head
                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head

                else:
                    previous.next = current.next

                return

            previous = current
            current = current.next

            # Baştan tekrar gelindiyse eleman yok
            if current == self.head:
                break

    def display(self):
        if self.head is None:
            print("Liste boş.")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(HEAD)")

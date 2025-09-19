class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(val)
        else:
            self.head = Node(val)

    def display(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = {}
        for i in range(size):
            self.table[str(i)] = LinkedList()

    def hash(self, val):
        return str(val % self.size)

    def insert(self, val):
        self.table[self.hash(val)].insert(val)

    def display(self):
        for i in self.table:
            print('Slot',i)
            self.table[i].display()

# h = HashTable(5)
# h.insert(12)
# h.insert(22)
# h.insert(25)
# h.insert(15)
# h.insert(3)
# h.insert(34)
#
# h.display()
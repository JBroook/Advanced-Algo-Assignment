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

    def hash(self, s, g=31):
        hash_value = 0
        for i in range(len(s)):
            hash_value = hash_value*g + ord(s[i])
        return str(hash_value % self.size)

    def insert(self, key, val):
        self.table[self.hash(key)].insert(val)

    def _get_chain(self, val):
        return self.table[self.hash(val)]

    def get_item(self, key, val):
        node = self._get_chain(val).head
        while node:
            if node.val.data[key]==val:
                return node.val
            else:
                node = node.next

        return None

    def display(self):
        for i in self.table:
            print('Slot',i)
            self.table[i].display()

# h = HashTable(5)
# h.insert("Bottle")
# h.insert("Stroller")
# h.insert("Diaper")
# h.insert("Milk Powder")
# h.insert("Toy Stars")
# h.insert("Toy Ball")
#
# h.display()
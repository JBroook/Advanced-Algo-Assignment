import random
import string
import time

class Node:
    def __init__(self, val, key, next=None):
        self.val = val
        self.next = next
        self.key = key

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, key, val):
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(val, key)
        else:
            self.head = Node(val, key)

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
        # hash_value = 0
        # for i in range(len(s)):
        #     hash_value = hash_value*g + ord(s[i])
        # return str(hash_value % self.size)
        return str(hash(s) % self.size)

    def insert(self, key, val):
        chain = self.table[self.hash(key)]
        chain.insert(key, val)

    def _get_chain(self, key):
        return self.table[self.hash(key)]

    def get_item(self, key):
        node = self._get_chain(key).head
        while node:
            if node.key==key:
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

if __name__=="__main__":
    simple_list = []
    #75% load factor
    hash_table = HashTable(round(1000*1.3))
    for i in range(1000):
        #generates random string of uppercase letters and numbers
        s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        simple_list.append(s)
        hash_table.insert(s, s)

    #retrieve 10 generated strings to search for
    target_strings = []
    for _ in range(10):
        if simple_list[random.randint(0,999)] not in target_strings:
            target_strings.append(simple_list[random.randint(0,999)])

    start_time = time.perf_counter_ns()
    for search_string in target_strings:
        simple_list.index(search_string)

    end_time = time.perf_counter_ns()
    print("Search for 1D list complete.")
    print(f"Total time taken: {end_time-start_time} nanoseconds")
    print(f"Average time taken: {(end_time - start_time)/10} nanoseconds\n")

    start_time = time.perf_counter_ns()
    for search_string in target_strings:
        hash_table.get_item(search_string)

    end_time = time.perf_counter_ns()
    print(f"Search for hash table complete.")
    print(f"Total time taken: {end_time - start_time} nanoseconds")
    print(f"Average time taken: {(end_time - start_time) / 10} nanoseconds\n")
import random
import string
import time

class Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, size):
        self.original_size = size
        self.size = round(size/0.75)
        self.table = {}

    def hash(self, s):
        return str(hash(s) % self.size)

    def insert(self, key, val):
        new_item = Item(key, val)
        hash_key = self.hash(key)
        if hash_key in self.table:
            dynamic_list = self.table[hash_key]
            dynamic_list.append(new_item)
        else:
            self.table[hash_key] = [new_item]

    def _get_chain(self, key):
        if self.hash(key) not in self.table:
            return None

        return self.table[self.hash(key)]

    def get_item(self, key):
        item_list = self._get_chain(key)
        for item in item_list:
            if item.key==key:
                return item
        return None

if __name__=="__main__":
    simple_list = []
    hash_table = HashTable(1000)
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
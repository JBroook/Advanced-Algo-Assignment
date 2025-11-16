import random
import string
import time

class Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class PHashTable:
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
        return self.table[self.hash(key)]

    def get_item(self, key):
        item_list = self._get_chain(key)
        for item in item_list:
            if item.key==key:
                return item
        return None

class HHashTable:
    def __init__(self, size):
        self.original_size = size
        self.size = round(size/0.75)
        self.table = {}

    def hash(self, s):
        hash_value = 0
        g = 31
        for i in range(len(s)):
            hash_value = hash_value*g + ord(s[i])
        return str(hash_value % self.size)

    def insert(self, key, val):
        new_item = Item(key, val)
        hash_key = self.hash(key)
        if hash_key in self.table:
            dynamic_list = self.table[hash_key]
            dynamic_list.append(new_item)
        else:
            self.table[hash_key] = [new_item]

    def _get_chain(self, key):
        return self.table[self.hash(key)]

    def get_item(self, key):
        item_list = self._get_chain(key)
        for item in item_list:
            if item.key==key:
                return item
        return None

if __name__=="__main__":
    track_list = []
    horner_method = HHashTable(1000)
    default_method = PHashTable(1000)
    for i in range(1000):
        #generates random string of uppercase letters and numbers
        s = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        track_list.append(s)

    #time insert operation for horner method
    start_time = time.perf_counter_ns()
    for s in track_list:
        horner_method.insert(s, s)
    end_time = time.perf_counter_ns()
    print("Insertion for Horner's method table complete.")
    print(f"Total time taken: {end_time - start_time} nanoseconds")
    print(f"Average time taken: {(end_time - start_time) / 10} nanoseconds\n")

    # time insert operation for default method
    start_time = time.perf_counter_ns()
    for s in track_list:
        default_method.insert(s, s)
    end_time = time.perf_counter_ns()
    print("Insertion for Python's hash method table complete.")
    print(f"Total time taken: {end_time - start_time} nanoseconds")
    print(f"Average time taken: {(end_time - start_time) / 10} nanoseconds\n")

    #retrieve 10 generated strings to search for
    target_strings = []
    for _ in range(10):
        if track_list[random.randint(0,999)] not in target_strings:
            target_strings.append(track_list[random.randint(0,999)])

    start_time = time.perf_counter_ns()
    for search_string in target_strings:
        horner_method.get_item(search_string)

    end_time = time.perf_counter_ns()
    print("Search for Horner's method table complete.")
    print(f"Total time taken: {end_time-start_time} nanoseconds")
    print(f"Average time taken: {(end_time - start_time)/10} nanoseconds\n")

    start_time = time.perf_counter_ns()
    for search_string in target_strings:
        default_method.get_item(search_string)

    end_time = time.perf_counter_ns()
    print(f"Search for Python hash method table complete.")
    print(f"Total time taken: {end_time - start_time} nanoseconds")
    print(f"Average time taken: {(end_time - start_time) / 10} nanoseconds\n")
class HashTable:
    #Function to create a Node
    def __init__ (self, size = 7):
        self.data_map = [None] * size
    
    #Hash constructor
    def hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    #Function to print all nodes in the hash 
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    
    #function to set an item in a hashtable
    def set_item(self, key, value):
        index = self.hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    #Function to get an item in a hashtable
    def get_item(self, key):
        index = self.hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    #Function to return all the keys in a hashtable
    def keys(self):
        all_keys = []
        for i in range (len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

#Demo Operations
my_hash_table = HashTable()
my_hash_table.print_table()
print(my_hash_table.hash('bolts'))
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washer', 120)
my_hash_table.set_item('nuts', 1200)
my_hash_table.print_table()
print(my_hash_table.get_item('nuts'))
print(my_hash_table.get_item('lumber'))
print(my_hash_table.get_item('washer'))
print(my_hash_table.keys())


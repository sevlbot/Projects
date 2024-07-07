#   Title: DSAHashTable.py 
#   Author: Tenzin Deki Dokar 
#    Availability: Practical 7 DSA1002

import numpy as np
from DSAHashEntry import DSAHashEntry

class DSAHashTable():
    
    def __init__(self, size):
        self.size = self._nextprime(size) 
        self.table = np.empty(self.size, dtype = object) 
        self.count = 0
        for i in range(self.size):
            self.table[i] = DSAHashEntry()

    def getSize(self):
        return self.size

    def getCount(self):
        return self.count

    def display(self):
        if self.count == 0:
            print("Table is empty")
        elif self.count > 0:
            for i in range(self.size):
                if self.table[i].value != None:
                    print(self.table[i].value) 
        else:
            print("Error with counting, less than 0")


    # shift-add-XOR hash from DSA1002 lecture 9 slides 
    def _hash(self, key):
        hashindex = 0
        for ch in range(len(key)):
            hashindex = hashindex ^ ((hashindex << 5) + (hashindex << 2) + ord(key[ch]))
        hashindex = hashindex % self.size
        return hashindex

    # hashing function for step size
    def _hash2(self, key):
        calc = 0
        for ch in range(len(key)):
            calc += ord(key[ch]) 
        hashstep = 3 - (calc % 3)

        return hashstep % self.size

    # function to determine next prime number in sequence to use it for table size, results in less collisions
    def _nextprime(self, startval):
        if startval % 2 == 0:
            primeval = startval + 1
        else:
            primeval = startval
        primeval -= 2
        isprime = False
        while not isprime:
            primeval += 2
            i = 3
            isprime = True
            while i*i <= primeval and isprime:
                if primeval % i == 0:
                    isprime = False
                else:
                    i += 2
        return primeval

    def put(self, key, value):
        found = self._find(key)
        if found != None:
            return -1
        else:
            cur = self._hash(key) 
            orig = cur #original hash index
            arr = self.table
            if arr[orig].state == 0:
                arr[orig].set(key, value, 1)
                self.count += 1
            else:
                step = self._hash2(key)
                while arr[cur].state == 1 :
                    cur = (cur + step) % (self.size)
                arr[cur].set(key, value, 1)
                self.count += 1

    def get(self, key):
        return self._find(key)

    def remove(self, key):
        if self.count == 0:
            return -1 #nothing to remove
        found = self._find(key)
        if found == None:
            return -2 # entry doesnt exist
        else:
            found.set("", None, -1)
            self.count -= 1
        
    def _find(self, key):
        cur = self._hash(key)
        orig = cur
        arr = self.table
        if arr[cur].key == key:
            return arr[cur]
        elif arr[cur].state == 0:
            return None
        else:
            step = self._hash2(key)
            cur = (orig + step) % (self.size)
            while arr[cur].state != 0 and arr[cur].key != key:
                cur = (cur + step) % (self.size)
            if arr[cur].state == 0:
                return None
            else:
                return arr[cur]

        

    




        



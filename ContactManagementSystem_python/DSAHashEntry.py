#   Title: DSAHashEntry.py 
#   Author: Tenzin Deki Dokar 
#    Availability: Practical 7 DSA1002

class DSAHashEntry():
    def __init__(self):
        self.key = ""
        self.value = None
        self.state = 0

    def set(self, key, value, state):
        self.key = key
        self.value = value
        self.state = state

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

    def getState(self):
        return self.state

    def __str__(self):
        return "Key: " + self.key + "\n" + str(self.value)



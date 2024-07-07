#   Title: DSADListNode.py 
#   Author: Tenzin Deki Dokar 
#    Availability: Practical 4 DSA1002

class DSAListNode():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value) 

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getNext(self):
        return self.next

    def setNext(self, _next):
        self.next = _next

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev

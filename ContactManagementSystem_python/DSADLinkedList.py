#   Title: DSADLinkedList.py 
#   Author: Tenzin Deki Dokar 
#    Availability: Practical 4 DSA1002

from DSADListNode import *

class DSADLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def display(self):
        if self.isEmpty():
            print("List is empty")
        else:
            prevNode = None
            curNode = self.head
            llist = ""
            while curNode != None:
                if curNode.getNext() == None:
                    llist += str(curNode.value)
                else:
                    llist += str(curNode.value) + "\n"
                curNode = curNode.getNext()
            print(llist)

    def insertFirst(self, value):
        newNode = DSAListNode(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.list = str(newNode.value) 
            self.count += 1
        else:
            self.head.setPrev(newNode)
            newNode.setNext(self.head)
            self.head = newNode
            self.count += 1

    def insertLast(self, value):
        newNode = DSAListNode(value)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.count += 1
        else:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
            self.count += 1


    def removeFirst(self):
        nodeValue = None
        if self.isEmpty():
           return -1 
        
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            if self.head != None:
                self.head.setPrev(None) #prev used to point to removed head node
            else:
                self.tail = None
            self.count -= 1
        return nodeValue

    def removeLast(self):
        nodeValue = None
        if self.isEmpty():
           return -1 
        else:
            nodeValue = self.tail.getValue()
            temp = self.tail
            self.tail = self.tail.getPrev()
            if self.tail != None:
                self.tail.setNext(None)
            else:
                self.head = None
            temp.setPrev(None)
            self.count -= 1
        return nodeValue


    def get(self, valuetf):
        nodeValue = None
        if self.isEmpty():
            return None
        elif self.tail.value == valuetf:
            return self.tail
        elif self.head.value == valuetf:
            return self.head
        else:
            exit = False
            prevNode = None
            curNode = self.head
            while not exit:
                prevNode = curNode
                curNode = curNode.getNext()
                if curNode == None:
                    exit = True
                elif curNode.getValue() == valuetf:
                    exit = True
            if curNode == None:
                return None
            else:
                return curNode

    def isEmpty(self):
        return self.head == None

from DSAHashTable import DSAHashTable
from DSAContact import DSAContact
from DSADLinkedList import DSADLinkedList
import numpy as np

class ContactManagement():
    def __init__(self):
        self.list = DSAHashTable(30) #set an initial size

    def display(self):
        self.list.display()

    def addContact(self, number, name, email, group):
        contact = DSAContact(number, name, email, group)
        self.list.put(number, contact) #uses put function of hash table to add contact

    def deleteContact(self, number):
        self.list.remove(number) # uses remove function of hash table to remove contact
    
    def getContactNum(self, number): 
        entry = self.list.get(number) # uses get function of hash table to get contact

        if entry != None: # if the contact exists
            contact = entry.value # uses the contacts value
        
        else:
            contact = entry # if it doesnt exist, just return None

        return contact
    
    def getContactName(self, name):
        matchednames = DSADLinkedList() #linked list to store contact 
        for i in range(self.list.size): # traversing through the whole table
            if self.list.table[i].value != None: # if the entry is not empty
                if self.list.table[i].value.name == name: #if name matches
                    matchednames.insertLast(self.list.table[i].value) #add contact to linked list

        return matchednames # returns a linked list of contacts with same name


    def updateContact(self, oldnumber,  number, name, email, group): # updates accordingly in imenu, use old info as well as new info
        self.deleteContact(oldnumber) # remove old contact
        self.addContact(number, name, email, group) # add new contact
    
    def filterContact(self, group):
        filtered = None
        
        if self.list.count != 0: # check if list is not empty
            filtered = DSADLinkedList()

            for i in range(self.list.size):
                if self.list.table[i].key != "" and self.list.table[i].value.group == group: #if the entry is occupied and its group matches
                    filtered.insertLast(self.list.table[i].value)

        return filtered

    # using quick sort algorithm
    def sortContact(self): # returns quick sorted separate array, does not print it
        contacts = None
        if self.list.count != 0:
            contacts = np.empty(self.list.count, dtype = object)
            j = 0 #counter for array
            for i in range(self.list.size):
                if self.list.table[i].key != "":
                    contacts[j] = self.list.table[i].value
                    j += 1
            #else it is empty
            contacts = self._quickSort(contacts)

        return contacts

#   Title: DSASorts.py 
#   Author: Tenzin Deki Dokar 
#    Availability: Practical 9  DSA1002

    # sort contacts alphabetically
    def _quickSort(self, contacts):
        self._quickSortRecurseMedian(contacts, 0, len(contacts)-1)
        return contacts

    # recursively call quick sort until only one index is left
    def _quickSortRecurseMedian(self, contacts, leftidx, rightidx):
        if leftidx < rightidx:
            pivotidx = self._median(contacts, leftidx, rightidx)

            newpivotidx = self._doPartitioning(contacts, leftidx, rightidx, pivotidx)

            self._quickSortRecurseMedian(contacts, leftidx, newpivotidx - 1)
            self._quickSortRecurseMedian(contacts, newpivotidx + 1, rightidx)

    #select median of three values as index
    def _median(self, contacts, leftidx, rightidx):
        mididx = (leftidx + rightidx)//2
        pivotidx = -1

        # using .lower() function make sure it is properly alphabetically sorted
        if contacts[leftidx].name.lower() <= contacts[mididx].name.lower() <= contacts[rightidx].name.lower() or contacts[rightidx].name.lower() <= contacts[mididx].name.lower() <= contacts[leftidx].name.lower():
            pivotidx = mididx

        elif contacts[mididx].name.lower() <= contacts[rightidx].name.lower() <= contacts[leftidx].name.lower() or contacts[leftidx].name.lower()  <= contacts[rightidx].name.lower() <= contacts[mididx].name.lower():
            pivotidx = rightidx

        else:
            pivotidx = leftidx

        return pivotidx
    # sort and place pivot in sorted location
    def _doPartitioning(self, contacts, leftidx, rightidx, pivotidx):
        pivotval = contacts[pivotidx]
        contacts[pivotidx] = contacts[rightidx]
        contacts[rightidx] = pivotval

        curidx = leftidx

        for i in range (leftidx, rightidx):
            if pivotval.name.lower() > contacts[i].name.lower():
                temp = contacts[i]
                contacts[i] = contacts[curidx]
                contacts[curidx] = temp
                curidx += 1
        newpivotidx = curidx
        contacts[rightidx] = contacts[newpivotidx]
        contacts[newpivotidx] = pivotval

        return newpivotidx
    
    











        



    

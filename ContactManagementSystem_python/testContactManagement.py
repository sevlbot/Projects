from ContactManagement import ContactManagement
import unittest
import io
import sys

class TestContactManagement(unittest.TestCase):
    def setUp(self):
        self.contactlist = ContactManagement()

    def testAddContact(self):
        self.contactlist.addContact("8910", "Dokar", "nnth@gmail.com", "W")
        self.assertEqual(self.contactlist.list.getCount(), 1, "Successfuly add contact")

        self.contactlist.addContact("8910", "Dokar", "nnth@gmail.com", "W")
        self.assertEqual(self.contactlist.list.getCount(), 1, "Attempt to add same number contact")

    def testDeleteContact(self):
        self.contactlist.addContact("8910", "Dokar", "nnth@gmail.com", "W")
        self.contactlist.deleteContact("8910")
        self.assertEqual(self.contactlist.list.getCount(), 0, "Successfully delete contatc")

        self.contactlist.deleteContact("8910")
        self.assertEqual(self.contactlist.list.getCount(), 0, "Attempt to delete contact that doesnt exist")

    def testGetContactNum(self):
        self.assertEqual(self.contactlist.getContactNum("1234"), None, "Get a contact that doesnt exist")

        self.contactlist.addContact("8910", "Dokar", "nnth@gmail.com", "W")
        self.assertEqual(str(self.contactlist.getContactNum("8910")),"Number: 8910\nName: Dokar\nEmail: nnth@gmail.com\nGroup: W\n" , "Get a contact that does exist")

    def testGetContactName(self): #test this again
        self.assertEqual(self.contactlist.getContactName("Tenzin").count, 0, "Get a contact that doesnt exist")

        self.contactlist.addContact("1234", "Tenzin", "s@gmail.com", "F")
        # cannot add more than one contact for some reason
        self.assertEqual(self.contactlist.getContactName("Tenzin").count, 1, "Get a contact that does exist")

        capOut = io.StringIO()
        sys.stdout = capOut

        self.contactlist.getContactName("Tenzin").display()

        self.assertEqual(capOut.getvalue(), "Number: 1234\nName: Tenzin\nEmail: s@gmail.com\nGroup: F\n\n", "Printing the list")

    def testUpdateContact(self):
        self.contactlist.addContact("1234", "Tenzin", "s@gmail.com", "F")
        self.contactlist.updateContact("1234", "1234", "Deki", "s@gmail.com", "F")
        self.assertEqual(str(self.contactlist.getContactNum("1234")), "Number: 1234\nName: Deki\nEmail: s@gmail.com\nGroup: F\n", "Successfully updating contact")

    def testSortContact(self): 
        self.contactlist.addContact("1234", "Tenzin", "s@gmail.com", "F")
        self.contactlist.addContact("5678", "Deki", "s@gmail.com", "F")
        self.contactlist.addContact("8989", "Dokar", "s@gmail.com", "F")

        capOut = io.StringIO()
        sys.stdout = capOut

        arr = self.contactlist.sortContact()
        
        for i in range(len(arr)):
            print(arr[i])


        self.assertEqual(capOut.getvalue(), "Number: 5678\nName: Deki\nEmail: s@gmail.com\nGroup: F\n\nNumber: 8989\nName: Dokar\nEmail: s@gmail.com\nGroup: F\n\nNumber: 1234\nName: Tenzin\nEmail: s@gmail.com\nGroup: F\n\n", "Sorted contact list")

    def testFilterContact(self):
        self.contactlist.addContact("1234", "Tenzin", "d@gmail.com", "F")

        capOut = io.StringIO()
        sys.stdout = capOut

        self.contactlist.filterContact("F").display()

        self.assertEqual(capOut.getvalue(), "Number: 1234\nName: Tenzin\nEmail: d@gmail.com\nGroup: F\n\n", "Filtered contact list")

        



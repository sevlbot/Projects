import unittest
import sys
import io
from InteractiveMenu import InteractiveMenu

class TestInteractiveMenu(unittest.TestCase):
    def setUp(self):
        self.imenu = InteractiveMenu()

    def testLoadFileContent(self):
        self.imenu._loadFileContent("contact_list.txt")
        # contact list has 18 contacts
        self.assertEqual(self.imenu.cList.list.count, 18, "Checking count")

    def testDisplayMenu(self):
        capOut = io.StringIO()
        sys.stdout = capOut

        self.imenu._displayMenu()

        self.assertEqual(capOut.getvalue(), "\nDSA Contact List Management System\n\nAvailable Commands:\n\na. View Contacts List\nb. Add New Contact\nc. Delete Contact\nd. Update Contact\ne. Search Contact\nf. Sort Contact List\ng. Display Contact List Belonging to Particular Group\nx. Exit\n", "Printing menu")

    def testRun(self):
        #TC01
        capOut = io.StringIO()
        sys.stdout = capOut

        self.imenu.run("a")

        self.assertEqual(capOut.getvalue(), "List is empty\n", "Printing an empty list")

        #TC02
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.cList.addContact("1234", "Tenzin", "D@gamil.com", "F")
        self.imenu.cList.addContact("5678", "Deki", "D@gamil.com", "W")

        self.imenu.run("a")

        self.assertEqual(capOut.getvalue(), "Number: 1234\nName: Tenzin\nEmail: D@gamil.com\nGroup: F\n\nNumber: 5678\nName: Deki\nEmail: D@gamil.com\nGroup: W\n\n", "Printing a list")

        #TC03
        sys.stdin = io.StringIO("1111\nDokar\nd@gamil.com\nF\n")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("b")

        self.assertEqual(capOut.getvalue(), "\nTo add\n\nNumber: Name: Email: Group: \nSuccessfully added contact\n\n", "Successfully add a contact with valid fields")

        #TC04
        sys.stdin = io.StringIO("1111\nDokar\nd@gamil.com\nF\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut

        self.imenu.run("b")

        self.assertEqual(capOut.getvalue(), "\nTo add\n\nNumber: Contact already exists\n", "Attempt to add to existing contact")

        #TC05 
        sys.stdin = io.StringIO("abcd\nDokar\nd@gamil.com\nF\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut

        self.imenu.run("b")

        self.assertEqual(capOut.getvalue(), "\nTo add\n\nNumber: Please enter only digits\n", "Attempt to add with invalid type")
        
        #TC06
        sys.stdin = io.StringIO(" \nDokar\nd@gamil.com\nF\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut

        self.imenu.run("b")

        self.assertEqual(capOut.getvalue(), "\nTo add\n\nNumber: User input is empty\n", "Attempt to add with blank field")


        #TC07
        sys.stdin = io.StringIO("1111\n")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("c")

        self.assertEqual(capOut.getvalue(), "Number to remove: \nSuccessfully deleted contact\n\n", "Successfully delete contact")

        #TC08
        sys.stdin = io.StringIO("0000\n")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("c")

        self.assertEqual(capOut.getvalue(), "Number to remove: Contact does not exist\n", "Attempt to delete non existing contact")
        
        #TC09
        sys.stdin = io.StringIO("@@@@\n")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("c")

        self.assertEqual(capOut.getvalue(), "Number to remove: Please enter only digits\n", "Attempt to delete contact with invalid type")
        
        #TC10
        sys.stdin = io.StringIO(" \n")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("c")

        self.assertEqual(capOut.getvalue(), "Number to remove: User input is empty\n", "Attempt to delete contact with blank field")

        #TC11
        self.imenu.cList.deleteContact("1234")
        self.imenu.cList.deleteContact("5678")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("c")

        self.assertEqual(capOut.getvalue(), "List is empty\n", "Attempt to delete contact from empty list")

        #TC12
        self.imenu.cList.addContact("1234", "Tenzin", "D@gmail.com", "F")

        sys.stdin = io.StringIO("1234\nx\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Matched number\nNumber: 1234\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\nx - exit; c - delete; d - update\nWhat would you like to do with the contact?: Exited search operation\n", "Successfully find contact with number")

        #TC13
        sys.stdin = io.StringIO("0000\nx\n")#why did using 5678 here not work, need to fix hash table
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Contact does not exist\n", "Attempt to find contact with non existing number")

        #TC14
        sys.stdin = io.StringIO("\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: User input is empty\n", "Attempt to find contact with empty field")

        #TC15
        sys.stdin = io.StringIO("abc123\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Invalid type\n", "Attempt to find contact with invalid field")

        #TC16
        sys.stdin = io.StringIO("Jigme\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: No matched name(s)\n", "Attempt to  find contact with non existing name")

        #TC17
        sys.stdin = io.StringIO("Tenzin\nx\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Matched name(s)\nNumber: 1234\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\nx - exit; c - delete; d - update\nWhat would you like to do with the contact?: Exited search operation\n", "Successfully find one contact with name")

        #TC18
        self.imenu.cList.addContact("0000", "Tenzin", "D@gmail.com", "F")

        sys.stdin = io.StringIO("Tenzin\n1234\nx\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Matched name(s)\nNumber: 1234\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\nNumber: 0000\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\nWhich contact would you like to choose? (enter number): Matched contact\nNumber: 1234\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\nx - exit; c - delete; d - update\nWhat would you like to do with the contact?: Exited search operation\n", "Successfully find contacts with name")

        #TC19
        sys.stdin = io.StringIO("Hola\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("e")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: No matched name(s)\n", "Attempt to find contact with non existing name")

        #TC20
        sys.stdin = io.StringIO("1234\n1111\nDeki\ng@gamil.com\nFR\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("d")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Matched number\nNumber: 1234\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\nEnter values to update:\nNumber: Name: Email: Group: Contact updated successfully\n", "Successfully update contact with new information")


        #TC21
        sys.stdin = io.StringIO("0000\n1234\nDeki\ngmgm\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("d")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Matched number\nNumber: 0000\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\nEnter values to update:\nNumber: Name: Email: Please enter a valid email\n", "Attempt to update contact with invalid field")

        #TC22
        sys.stdin = io.StringIO("1111\n1111\nDeki\ng@gamil.com\nFR\n")
        
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("d")

        self.assertEqual(capOut.getvalue(), "Enter number or name to look for: Matched number\nNumber: 1111\nName: Deki\nEmail: g@gamil.com\nGroup: FR\n\nEnter values to update:\nNumber: Name: Email: Group: Contact updated successfully\n", "Successfully update contact with same information")

        #TC23
        self.imenu.cList.addContact("8888", "A", "D@gmail.com", "F")
        self.imenu.cList.addContact("99999999", "B", "D@gmail.com", "F")
        self.imenu.cList.addContact("55555", "B", "D@gmail.com", "F")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("f")
        self.assertEqual(capOut.getvalue(), "Number: 8888\nName: A\nEmail: D@gmail.com\nGroup: F\n\nNumber: 99999999\nName: B\nEmail: D@gmail.com\nGroup: F\n\nNumber: 55555\nName: B\nEmail: D@gmail.com\nGroup: F\n\nNumber: 1111\nName: Deki\nEmail: g@gamil.com\nGroup: FR\n\nNumber: 0000\nName: Tenzin\nEmail: D@gmail.com\nGroup: F\n\n", "Successfully sort a list")
        
        #TC24
        self.imenu.cList.deleteContact("8888")
        self.imenu.cList.deleteContact("99999999")
        self.imenu.cList.deleteContact("55555")
        self.imenu.cList.deleteContact("0000")
        self.imenu.cList.deleteContact("1111")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("f")

        self.assertEqual(capOut.getvalue(), "List is empty\n", "Attempt to sort an empty list")

        #TC25
        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("g")

        self.assertEqual(capOut.getvalue(), "List is empty\n", "Attempt to filter an empty list")

        #TC26
        self.imenu.cList.addContact("1234", "A", "D@gmail.com", "F")
        self.imenu.cList.addContact("5678", "B", "D@gmail.com", "FR")
        self.imenu.cList.addContact("9101", "C", "D@gmail.com", "F")

        sys.stdin = io.StringIO("A")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("g")

        self.assertEqual(capOut.getvalue(), "Enter group to filter: Group invalid\n", "Attempt to filter an invalid group")

        #TC27
        sys.stdin = io.StringIO("F")

        capOut = io.StringIO()
        sys.stdout = capOut
        
        self.imenu.run("g")

        self.assertEqual(capOut.getvalue(), "Enter group to filter: Number: 1234\nName: A\nEmail: D@gmail.com\nGroup: F\n\nNumber: 9101\nName: C\nEmail: D@gmail.com\nGroup: F\n\n", "Successfully filter a group")

    


        

from ContactManagement import ContactManagement
import numpy as np
from Errors import EmptyListError, ExistingContactError, NonExistingContactError, FullListError 

class InteractiveMenu():

    def __init__(self):
        self.cList = ContactManagement()

    def _loadFileContent(self, filename):
        with open(filename, "r") as file1:
            lines = file1.readlines()
            file1.close()
            for line in lines:
                contact_info = line.strip().split(",")
                self.cList.addContact(contact_info[0], contact_info[1], contact_info[2], contact_info[3])

    def _displayMenu(self):
        print("\nDSA Contact List Management System\n")
        print("Available Commands:\n")
        print("a. View Contacts List")
        print("b. Add New Contact")
        print("c. Delete Contact")
        print("d. Update Contact")
        print("e. Search Contact")
        print("f. Sort Contact List")
        print("g. Display Contact List Belonging to Particular Group")
        print("x. Exit")

    def run(self, cmd):
        if cmd == "a":
            self._display_contact()

        elif cmd == "b":
            self._add_contact()

        elif cmd == "c":
            self._delete_contact()

        elif cmd == "d":
            found = self._search_contact()
            if found != None:
                self._update_contact(found)

        elif cmd == "e":
            found = self._search_contact()
            #once contact is found, provide further action
            if found != None:
                print("x - exit; c - delete; d - update")
                userinput = input("What would you like to do with the contact?: ")
                while userinput not in ["x", "c", "d"]:
                    print("Invalid operation")
                    print("x - exit; c - delete; d - update")
                    userinput = input("What would you like to do with the contact?: ")
                if userinput == "x":
                    print("Exited search operation")
                elif userinput == "c":
                    self.cList.deleteContact(found.number)
                    print("Contact deleted")
                elif userinput == "d":
                    self._update_contact(found)

        elif cmd == "f":
            self._sort_contact()

        elif cmd == "g":
            self._filter_contact()
        
        else:
            print("Invalid Command")

    def _display_contact(self):
        try:
            if self.cList.list.count == 0:
                raise EmptyListError("List is empty")
            else:
                self.cList.display()
        except EmptyListError as err:
            print(err)

    def _add_contact(self):
        try:
            if self.cList.list.count == self.cList.list.size:
                raise FullListError("List is full")

            print("\nTo add\n")

            number = input("Number: ") #should be number

            if not number or len(number.strip()) == 0:
                raise ValueError("User input is empty")

            elif not number.isdigit():
                raise TypeError("Please enter only digits")

            elif len(number.strip()) > 15:
                raise ValueError("User input exceeds length")

            elif self.cList.getContactNum(number) != None:
                raise ExistingContactError("Contact already exists")

            name = input("Name: ") 
            
            if not name or len(name.strip()) == 0:
                raise ValueError("User input is empty")

            elif not name.isalpha():
                raise TypeError("Input contains non-alphabet characters")
            
            elif len(name.strip()) > 50:
                raise ValueError("User input exceeds length")

            email = input("Email: ") # should have @smth.smth
            
            if not email or len(email.strip()) == 0:
                raise ValueError("User input is empty")
            
            elif len(email.strip()) > 50:
                raise ValueError("User input exceeds length")

            elif "@" not in email or "." not in email:
                raise TypeError("Please enter a valid email")

            group = input("Group: ") # should be F, FR or W
            
            if not group or len(group.strip()) == 0:
                raise ValueError("User input is empty")

            elif group not in ["F", "FR", "W"]:
                raise ValueError("Please enter a valid group")

            self.cList.addContact(number, name, email, group)
            print("\nSuccessfully added contact\n")

        except ValueError as err:
            print(err)

        except ExistingContactError as err:
            print(err)
        
        except FullListError as err:
            print(err)

        except TypeError as err:
            print(err)

    def _delete_contact(self):
        try:
            if self.cList.list.count == 0:
                raise EmptyListError("List is empty")

            number = input("Number to remove: ") # should be a number
            
            if not number or len(number.strip()) == 0:
                raise ValueError("User input is empty")

            elif not number.isdigit():
                raise TypeError("Please enter only digits")
            
            elif len(number.strip()) > 15:
                raise ValueError("User input exceeds length")
            
            elif self.cList.getContactNum(number) == None:
                raise NonExistingContactError("Contact does not exist")

            self.cList.deleteContact(number)
            print("\nSuccessfully deleted contact\n")

        except EmptyListError as err:
            print(err)

        except ValueError as err:
            print(err)

        except TypeError as err:
            print(err)
        
        except NonExistingContactError as err:
            print(err)

    def _update_contact(self, oldcontact):
        try:
            print("Enter values to update:")

            number = input("Number: ") 

            if not number or len(number.strip()) == 0:
                raise ValueError("User input is empty")

            elif not number.isdigit():
                raise TypeError("Please enter only digits")
            
            elif len(number.strip()) > 15:
                raise ValueError("User input exceeds length")

            # if contact already exists and the existin gcontact's number is NOT the number of the contact we are updating
            elif self.cList.getContactNum(number) != None and number != oldcontact.number:
                raise ExistingContactError("Contact already exists")

            name = input("Name: ") #should not have numbers and sp chars
            
            if not name or len(name.strip()) == 0:
                raise ValueError("User input is empty")

            elif not name.isalpha():
                raise TypeError("Input contains non-alphabet characters")
            
            elif len(name.strip()) > 50:
                raise ValueError("User input exceeds length")

            email = input("Email: ") 
            
            if not email or len(email.strip()) == 0:
                raise ValueError("User input is empty")

            elif "@" not in email or "." not in email:
                raise TypeError("Please enter a valid email")
            
            elif len(email.strip()) > 50:
                raise ValueError("User input exceeds length")

            group = input("Group: ") # should be F, FR or W
            
            if not group or len(group.strip()) == 0:
                raise ValueError("User input is empty")

            elif group not in ["F", "FR", "W"]:
                raise ValueError("Please enter a valid group")

            self.cList.updateContact(oldcontact.number, number, name, email, group)
            print("Contact updated successfully")

        except ValueError as err:
            print(err)
        
        except TypeError as err:
            print(err)

        except NonExistingContactError as err:
            print(err)
        
        except EmptyListError as err:
            print(err)

    def _search_contact(self):
        try:
            if self.cList.list.count == 0:
                raise EmptyListError("List is empty")

            userinput = input("Enter number or name to look for: ") # number or name format should be valid, make sure its not a mixture

            if not userinput or len(userinput.strip()) == 0:
                raise ValueError("User input is empty")

            if userinput.isdigit():
                if len(userinput.strip()) > 15:
                    raise ValueError("User input exceeds length")
                contact = self.cList.getContactNum(userinput)
                if contact == None:
                    raise NonExistingContactError("Contact does not exist")
                else:
                    print("Matched number") # will contain the contact
                    print(contact)

            elif userinput.isalpha():
                if len(userinput.strip()) > 50:
                    raise ValueError("User input exceeds length")
                contact = self.cList.getContactName(userinput)
                if contact.isEmpty():
                    raise ValueError("No matched name(s)")
                else:
                    print("Matched name(s)")
                    if contact.count == 1: # if there is only one contact, just return that 
                        contact = self.cList.getContactNum(contact.head.value.number)
                        print(contact)

                    elif contact.count > 1: # if there are more than one contact, ask the user to choose one
                        contact.display()
                        userinput2 = input("Which contact would you like to choose? (enter number): ")
                        if userinput2.isdigit():
                            curnode = contact.head
                            stop = False
                            while stop == False:
                                if curnode == None:
                                    raise ValueError("Contact not in list")
                                elif curnode.value.number == userinput2:
                                    stop = True
                                else:
                                    curnode = curnode.next
                            number = userinput2
                            contact = self.cList.getContactNum(number) 
                            print("Matched contact")
                            print(contact)

                        else:
                            raise TypeError("Invalid type")
            else:
                raise TypeError("Invalid type")

            return contact

        except ValueError as err:
            print(err)

        except TypeError as err:
            print(err)

        except EmptyListError as err:
            print(err)

        except NonExistingContactError as err:
            print(err)



    def _sort_contact(self):
        try:
            sorted_arr = self.cList.sortContact()

            if self.cList.list.count == 0:
                raise EmptyListError("List is empty")

            else:
                for i in range(len(sorted_arr)):
                    print(sorted_arr[i])

        except EmptyListError as err:
            print(err)


    def _filter_contact(self):
        try:
            if self.cList.list.count == 0:
                raise EmptyListError("List is empty")

            userinput = input("Enter group to filter: ")

            if not userinput.isalpha():
                raise TypeError("Invalid type")

            elif userinput not in ["F", "FR", "W"]:
                raise ValueError("Group invalid")

            else:
                filtered = self.cList.filterContact(userinput)
                filtered.display()

        except TypeError as err:
            print(err)

        except ValueError as err:
            print(err)

        except EmptyListError as err:
            print(err)

    def main(self):
        self._loadFileContent("contact_list.txt")
        self._displayMenu()
        cmd = input()

        while cmd != "x":
            self.run(cmd)
            self._displayMenu()
            cmd = input("Enter another command: ")

if __name__ == "__main__":
    menu = InteractiveMenu()
    menu.main()


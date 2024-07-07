import unittest
from DSADLinkedList import DSADLinkedList
import sys
import io

class testLinkedList(unittest.TestCase):

    def setUp(self):
        self.list = DSADLinkedList()

    def testInsertFirst(self):
        self.list.insertFirst("Tenzin")
        self.assertEqual(str(self.list.head), "Tenzin", "Head points to new node")
        self.assertEqual(str(self.list.tail), "Tenzin", "Tail points to new node")

        self.list.insertFirst("Deki")
        self.assertEqual(str(self.list.head), "Deki", "Head points to new node")
        self.assertEqual(str(self.list.tail), "Tenzin", "Tail points to old node")

        self.list.insertFirst("Dokar")
        self.assertEqual(str(self.list.head), "Dokar", "Head points to new node")
        self.assertEqual(str(self.list.tail), "Tenzin", "Tail points to old node")

    def testInsertLast(self):
        self.list.insertLast("Tenzin")
        self.assertEqual(str(self.list.head), "Tenzin", "Head points to new node")
        self.assertEqual(str(self.list.tail), "Tenzin", "Tail points to new node")

        self.list.insertLast("Deki")
        self.assertEqual(str(self.list.head), "Tenzin", "Head points to old node")
        self.assertEqual(str(self.list.tail), "Deki", "Tail points to new node")

        self.list.insertLast("Dokar")
        self.assertEqual(str(self.list.head), "Tenzin", "Head points to old node")
        self.assertEqual(str(self.list.tail), "Dokar", "Tail points to new node")

    def testRemoveFirst(self):
        self.assertEqual(self.list.removeFirst(), -1, "Nothing to remove")

        self.list.insertLast("Tenzin")
        self.list.removeFirst()
        self.assertEqual(self.list.head, None, "Removing only item")
        self.assertEqual(self.list.tail, None, "Removing only item")

        self.list.insertLast("Tenzin")
        self.list.insertLast("Deki")
        self.list.removeFirst()
        self.assertEqual(str(self.list.head), "Deki", "Head points to remaining node")
        self.assertEqual(str(self.list.tail), "Deki", "Tail points to remaining node")

        self.list.insertLast("Tenzin")
        self.list.insertLast("Deki")
        self.list.insertLast("Dokar")
        self.list.removeFirst()
        self.assertEqual(str(self.list.head), "Tenzin", "Head points to remaining node")
        self.assertEqual(str(self.list.tail), "Dokar", "Tail points to remaining node")

    def testRemoveLast(self):
        self.assertEqual(self.list.removeLast(), -1, "Nothing to remove")

        self.list.insertLast("Tenzin")
        self.list.removeLast()
        self.assertEqual(self.list.head, None, "Removing only item")
        self.assertEqual(self.list.tail, None, "Removing only item")

        self.list.insertLast("Deki")
        self.list.insertLast("Tenzin")
        self.list.removeLast()
        self.assertEqual(str(self.list.head), "Deki", "Head points to remaining node")
        self.assertEqual(str(self.list.tail), "Deki", "Tail points to remaining node")

        self.list.insertLast("Dokar")
        self.list.insertLast("Tenzin")
        self.list.removeLast()
        self.assertEqual(str(self.list.head), "Deki", "Head points to remaining node")
        self.assertEqual(str(self.list.tail), "Dokar", "Tail points to remaining node")

    def testGet(self):
        self.assertEqual(self.list.get("Tenzin"), None, "Empty list")

        self.list.insertLast("Tenzin")
        self.assertEqual(str(self.list.get("Tenzin")), "Tenzin", "With only one item")

        self.assertEqual(self.list.get("Deki"), None, "Getting an item that doesnt exist")

        self.list.insertLast("Deki")
        self.list.insertLast("Dokar")
        self.assertEqual(str(self.list.get("Deki")), "Deki", "Getting an item that does exist")

    def testDisplay(self):
        capOut = io.StringIO()
        sys.stdout = capOut

        self.list.display()

        self.assertEqual(capOut.getvalue(), "List is empty\n", "Printing empty list")

        self.list.insertLast("Tenzin")
        self.list.insertLast("Deki")
        self.list.insertLast("Dokar")

        capOut = io.StringIO()
        sys.stdout = capOut

        self.list.display()
        self.assertEqual(capOut.getvalue(), "Tenzin\nDeki\nDokar\n", "Printing list")

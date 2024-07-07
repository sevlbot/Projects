import unittest
from DSAHashTable import DSAHashTable
import io
import sys

class testDSAHashTable(unittest.TestCase):

    def setUp(self):
        self.htable = DSAHashTable(100)
        self.htable.put("1", "Tenzin")
        self.htable.put("2", "Deki")

    def testPut(self):
        self.htable.put("2", "Deki")
        self.htable.put("3", "Dokar")
        self.assertEqual(self.htable.count, 3)

        self.assertEqual(self.htable.put("2", "Deki"), -1, "Cannot overwrite existing entry")
    
    def testGet(self):
        self.assertEqual(str(self.htable.get("1")),"Key: 1\nTenzin", "Retrieve existing entry" )

        self.assertEqual(self.htable.get("3"), None, "Retrieving entry that doesnt exist")

    def testRemove(self):
        self.htable.remove("1")
        self.assertEqual(self.htable.count, 1, "Successfully remove existing key")
        
        self.assertEqual(self.htable.remove("3"), -2, "Entry doesnt exist")

        self.htable.remove("2")
        self.assertEqual(self.htable.remove("2"), -1, "Table is empty")

    def testDisplay(self):
        capOut = io.StringIO()
        sys.stdout = capOut

        self.htable.display()

        self.assertEqual(capOut.getvalue(), "Tenzin\nDeki\n", "Printing table")

        self.htable.remove("1")
        self.htable.remove("2")
        
        capOut = io.StringIO()
        sys.stdout = capOut

        self.htable.display()

        self.assertEqual(capOut.getvalue(), "Table is empty\n", "Printing empty table")



#import unittest2 as unittest
import unittest
from autocast import autocast
import sys


@autocast
def castit(input):
    return type(input)

@autocast
def noneit(input):
    return input

class TestDM(unittest.TestCase):
    def testStrToStr(self):
        self.assertEqual(castit('ohai'), str)
        self.assertEqual(castit('foo bar baz'), str)

    def testStrToList(self):
        self.assertEqual(castit('[1,2,3,4]'), list)

    def testStrToInt(self):
        self.assertEqual(castit('1'), int)
        self.assertEqual(castit('10'), int)
        self.assertNotEqual(castit('5.4'), int)

    def testIntToInt(self):
        self.assertEqual(castit(1), int)
        self.assertEqual(castit(10), int)
        self.assertNotEqual(castit(5.5), int)

    def testStrToFloat(self):
        self.assertEqual(castit('5.5'), float)
        self.assertEqual(castit('100.22222222224'), float)
        self.assertEqual(castit(202.50), float)

    def testBool(self):
        self.assertEqual(castit('true'), bool)
        self.assertEqual(castit('True'), bool)
        self.assertEqual(castit(True), bool)
        self.assertEqual(castit('false'), bool)
        self.assertEqual(castit('false'), bool)
        self.assertEqual(castit(False), bool)


    def testNone(self):
        if sys.version_info > ( 2, 7, 0 ):
            self.assertIsNone(noneit('none'))
            self.assertIsNone(noneit('None'))
        else: # we are on 2.6 or before, we will skip the none test
            return True

if __name__ == "__main__":
    unittest.main()
        


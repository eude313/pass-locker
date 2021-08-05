from user import first
import unittest

#first test
class TestContact(unittest.TestCase):
    def setUp(self): 
        self.name = first('carbon')

import unittest
from info import info

class TestUSer(unittest.TestCase):
    def setUp(self):
      self.new_credential = info("user_name","password","email@ms.com")  
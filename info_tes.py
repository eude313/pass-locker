import unittest
from info import info

class TestUSer(unittest.TestCase):
    def setUp(self):
      self.new_credential = info("user_name","password","email@ms.com")  
    #tearDown method should
    def tearDown(self):
        info.credential_array = []
    def test_init(self):
        self.assertEqual(self.new_credential.user_name, "user_name")
        self.assertEqual(self.new_credential.email, "email@ms.com")
        self.assertEqual(self.new_credential.password, "password")
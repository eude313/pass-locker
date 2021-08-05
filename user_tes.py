import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        
        self.new_user = User("carbon","Miki","0712345678","miki@ms.com")

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "carbon")
        self.assertEqual(self.new_user.last_name, "Miki")
        self.assertEqual(self.new_user.phone_number, "0712345678")
        self.assertEqual(self.new_user.email, "miki@ms.com") 

import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        
        self.new_user = User("James","Muriuki","0712345678","james@ms.com")# create user object



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
    def test_save_user(self):
        self.new_user.save_user()#saving the new user
        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com")#save user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
      #tear down method
    def tearDown(self):  
        User.user_list = []

    #delete method 
    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Test","user","0712345678","test@user.com")#new user
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
        #finding info by number
    def test_find_by_number(self): 
        self.new_user.save_user()
        test_user = User("Test","user","0711222344","test@user.com")
        test_user.save_user()

        found_user = User.find_by_number("0711222344")

        self.assertEqual(found_user.email,test_user.email)
    def test_contact_exists(self):
        self.new_user.save_user()
        test_user  = User("Test","user","0711223344","test@user.com")#new user
        test_user.save_user()
        user_exists = User.user_exists("0711222344")

        self.assertTrue(user_exists)
    #displaying info of users 
    def test_display_all_users(self):
        self.assertEqual(User.display_users(),User.user_list)
        
    def test_copy_email(self):
        self.new_user.save_user()
        User.copy_email("0712345678")

        self.assertEqual(self.new_user.email,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
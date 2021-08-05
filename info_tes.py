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
        #saving info
    # def test_save_cred(self):
    #     self.new_credential.save_credential()  
    #     self.assertEqual(len(info.credential_array), 1)
    #it returns alist of saved credentials
    # def test_display_credentials(self):
    #   self.assertEqual(info.display_credential(),info.credentials_array)
if __name__=="__main__":
    unittest.main()
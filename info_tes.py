
import unittest
from info import Info

class TestUSer(unittest.TestCase):
    def setUp(self):
      self.infomation_array = Info("user_name","password","email@ms.com")  
    #tearDown method should
    def tearDown(self):
        Info.infomation_array = []
    def test_init(self):
        self.assertEqual(self.infomation_array.user_name, "user_name")
        self.assertEqual(self.infomation_array.email, "email@ms.com")
        self.assertEqual(self.infomation_array.password, "password")
        #saving Info
    def test_save_info(self):
        self.infomation_array.save_info,Info.display_info()
        # self.assertEqual(len(Info.infomation_array),1)
    # it returns alist of saved infodisplay_infos
    def test_display_info(self):
        self.assertEqual(Info.display_info(),Info.infomation_array)
if __name__=="__main__":
    unittest.main()
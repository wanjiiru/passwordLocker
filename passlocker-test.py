from passLocker import Credential
from passLocker import UserData
import pyperclip
import unittest


class Testcredential(unittest.TestCase):
    '''
    '''


    def setUp(self):
        '''
        set up structure before every test
        '''
        self.new_creds = Credential("liz","pass")



    def tearDown(self):
        '''
        clean up after running each test
        '''
        Credential.cred_list = []


    def test_init(self):
        '''
        Test for case initialization
        '''
        self.assertEqual(self.new_creds.uname, "liz")
        self.assertEqual(self.new_creds.passwrd, "pass")

    def test_authentication(self):
        '''
        Tests proper autentication for log in purposes
        '''
        self.new_creds.save_creds()
        self.assertEqual(len(Credential.cred_list), 1)









class TestUserData(unittest.TestCase):
    '''
    '''


    def setUp(self):
        '''
        set up structure before every test

        '''
        self.new_user_data = UserData("facebook","wanjiiru","pass")


    def tearDown(self):
        '''
        clean up after runnong each test
        '''
        UserData.user_data_list = []



    def test_init(self):
        '''
        Test for test case initialization"
        '''
        self.assertEqual(self.new_user_data.acc_name, "facebook")
        self.assertEqual(self.new_user_data.acc_username, "wanjiiru")
        self.assertEqual(self.new_user_data.acc_password, "pass")

    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_user_data.create_password()
        self.assertEqual(len(UserData.user_data_list),1)



    def test_show_data(self):
        '''
        Testing if the data can be displayed.
        '''
        self.new_user_data.create_password()
        test_this = UserData("twitter","liz", "pass")
        test_this.create_password()

        found_user_data = UserData.show_user_data("twitter")
        self.assertEqual(found_user_data.acc_name,test_this.acc_name)




if __name__ == "__main__":
    unittest.main()




        


        










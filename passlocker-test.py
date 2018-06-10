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


        



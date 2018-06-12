
import pyperclip
class Credential:

    cred_list=[]

    '''
    class that generates new instance of contacts
    '''

    def __init__(self, uname, passwrd):
        '''
        '''
        self.uname=uname
        self.passwrd=passwrd


    def save_creds(self):
        '''
        '''
        Credential.cred_list.append(self)


    @classmethod
    def creds_exist(cls,uname):
        '''
        Method that checks if the username exist

        '''
        for credential in cls.cred_list:
            if credential.uname==uname:
                return True
        return False


    @classmethod
    def authenticate_creds(cls, uname, passwrd):
        '''
        Method that checks if the username and password are correct
        '''
        for cred in cls.cred_list:
            if cred.uname == uname and cred.passwrd == passwrd:
                return cred
        return 0


class UserData:
    '''
    class that generates new instance of user data
    '''
    user_data_list = []
    user_data_list2 = str(user_data_list)

    def __init__(self, acc_name,acc_username, acc_password):
        '''
        '''
        self.acc_name = acc_name
        self.acc_username =  acc_username
        self.acc_password = acc_password

    def create_password(self):
        '''
        creates a passord and acc name
        '''
        return UserData.user_data_list.append(self)


    @classmethod
    def show_user_data(cls):
        '''
        Displays all passwords and other acc details 
        '''
        return cls.user_data_list


    @classmethod
    def find_by_acc_name(cls, acc_name):
        '''
        Finds user data using the user acc name
        '''

        for found in cls.user_data_list2:
            if found == acc_name:
                return found
                



    @classmethod
    def data_exists(cls, acc_name):
        '''
        Checks if data exists
        '''
        for data in cls.user_data_list:
            if data.acc_name == acc_name:
                return data





    



    
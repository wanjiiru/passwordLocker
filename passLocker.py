
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

    @classmethod
    def find_by_uname(cls,uname):
        '''
        Method that finds credentials bu username
        '''
        for credential in cls.cred_list:
            if credential.uname==uname:
                return uname


class UserData:
    '''
    class that generates new instance of user data
    '''
    user_data_list=[]


    def __init__(self, acc_name,acc_username, acc_password, acc_id):
        '''
        '''
        self.acc_name = acc_name
        self.acc_username =  acc_username
        self.acc_password = acc_password
        self.acc_id = acc_id

    def create_password(self):
        '''
        '''
        UserData.user_data_list.append(self)


    @classmethod
    def show_user_data(cls, number, index):
        '''
        '''
        for password in cls.user_data_list:
            if password.acc_id == number:
                if password.acc_id == index:
                    return password


    @classmethod
    def copy_password(cls, number, index):
        '''
        '''
        my_password = UserData.show_user_data(number,index)
        pyperclip.copy(my_password.acc_password)



    @classmethod
    def data_exists(cls, number):
        '''
        '''
        for data in cls.user_data_list:
            if data.acc_id == number:
                return True
        return False





    



    
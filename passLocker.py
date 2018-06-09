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
        '''
        for credential in cls.cred_list:
            if credential.uname==uname:
                return True
        return False

    @classmethod
    def find_by_uname(cls,uname):
        '''
        '''
        for credential in cls.cred_list:
            if credential.uname==uname:
                return uname

    
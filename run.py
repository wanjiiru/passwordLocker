#!/usr/bin/env python3
from passLocker import Credential

def create_creds(uname, password):
    '''
    '''
    new_cred = Credential(uname,password)
    return new_cred


def save_creds(credential):
    '''
    '''
    credential.save_creds()


def find_creds(uname):
    '''
    '''
    return Credential.find_by_uname(uname)


def check_existing_cred(uname):
    '''
    '''
    return Credential.creds_exist(uname)



def main():
        print("Hello, welcome to password locker!, What is your name?")
        user_name = input('Name:')
        print(f'hello {user_name}. what would you like to do?')
        # print('hello {}. what would you like to do?'.format(user_name))



if __name__=='__main__':
    main()

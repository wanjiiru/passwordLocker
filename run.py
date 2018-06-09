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

def authenticate_creds(uname, passwrd):
    '''
    '''
    return Credential.authenticate_creds(uname,passwrd)





def main():
        print("Hello, welcome to password locker!, What is your name?")
        user_name = input('Name:')
        print(f'hello {user_name}. what would you like to do?')
        print('\n')
        while True:
            print("Use the following short short codes : cc - create a new account, lg - log in , ex - exit")
            short_code = input().lower()

            if short_code == 'cc':
                            print("New Account")
                            print("-"*10)

                            print ("username ....")
                            uname = input()

                            print("password ...")
                            password = input()
                            save_creds(create_creds(uname,password)) # create and save credentials
                            print ('\n')
                            print(f"Your new account with username : '{uname}' and password '{password}' has been successfully created")
                            print ('\n')


            elif short_code == "lg":
                            print("Enter username and password to login:")
                            print("-"*50)
                            username = input("Username: ")
                            passwrd = input("Password: ")
                            log_in = authenticate_creds(username, passwrd)
                            if log_in==0:
                                print("\n")
                                print("Invalid username and/or password")
                                print("-"*25)
                            elif log_in!=0:
                                print("\n")
                                print(f"Welcome {log_in.uname}! What would you like to do?")


                            

if __name__=='__main__':
    main()

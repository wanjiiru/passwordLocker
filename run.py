#!/usr/bin/env python3
from passLocker import Credential
from passLocker import UserData
import random
import string
import time


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

def user_data(acc_name,acc_username, acc_password, acc_id):
    '''
    '''
    data = UserData(acc_name, acc_username, acc_password, acc_id)
    return data


def create_new_data(mydata):
    '''
    '''
    mydata.create_password()


def show_data(mydata, index):
    '''
    '''
    return UserData.show_user_data(mydata, index)

def copy_pass(number, index):
    '''
    copies passowrd to the clipboard
    '''
    UserData.copy_password(number, index)



def generate_password(count):
    '''
    Funstion that generates a random password
    '''

    password_list = []
    generated_password = random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase )
    password_list.append(generated_password)
    return ''.join(password_list)






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
                            uname = input("Username: ")
                            passwrd = input("Password: ")
                            log_in = authenticate_creds(uname, passwrd)
                            if log_in==0:
                                print("\n")
                                print("Invalid username and/or password")
                                print("-"*25)
                            elif log_in!=0:
                                print("\n")
                                print(f"Welcome {log_in.uname}! What would you like to do?")
                                while True:
                                    print("Use the following short short codes : ap - add new password, sp - see your passwords , ex - exit")
                                    short_code== input()  
                                    if short_code== "ap":
                                        print("Enter account name such as facebook, instagram or Gmail:.......")
                                        my_account = input()
                                        print("What is you preferred password length?")
                                        pass_length = int(input("Password length"))
                                        acc_password = generate_password(pass_length)
                                        acc_name = log_in.acc_name
                                        acc_username = log_in.user_name
                                        acc_id = log_in.acc_id
                                        create_new_data(user_data(acc_name, acc_id, acc_username, acc_password))
                                        print("\nHold on tight....")
                                        time.sleep(1.0)
                                        print("\n")
                                        print(f"Generated  password for {my_account} is {acc_password}")
                                        print(".."*10)
                            elif short_code = "sp":
                                



if __name__=='__main__':
    main()

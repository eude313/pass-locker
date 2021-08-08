from user import User
from info import Info
import random

    #creatingg a new usser
def create_user(first, lastn, phone, email):
    new_user = User(first, lastn, phone, email)
    return new_user
def save_info(infomation):
    
    infomation.save_infomation()
    
def save_user(user):
   
    user.save_user()
    
def delete_info(infomation):
   
    infomation.delete_infomation()
    
def del_user(user):
   
    user.delete_user()
    
def display_user():
    
    return User.display_users()

def display_info(name, word, email):
   
    infomation_array = Info(name, word, email)
    return infomation_array

def display_info():
    return Info.infomation_array()

def main():

    print("Welcome to your Password Locker, choose your path")

    while True:
        print("Allowed Actions: \n acu - create a new user account with a user-defined password \n disp - display all user accounts \n ext -exit the contact list \n")

        short_code = input().lower()

        if short_code == 'acu':
            print("New User")
            print("-"*10)
            print("hello! What account do you want to create?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            first_name = input()

            print("Last name ...")
            last_name = input()

            print("Phone number ...")
            phone_number = input()

            print("Email address ...")
            email = input()

            print("Enter username ...")
            user_name = input()

            print("Enter Password ...")
            password = input()

            save_user(create_user(first_name,last_name,phone_number,email))
           
            print('\n')
            print(f" A new {site} account by {first_name} {last_name} has successfully been created")
            print(f" The username is {user_name} and the password is {password}")
            print('\n')

        elif short_code == 'disp':

            if display_user():
                print("Here is a list of all your user accounts")
                print('\n')

                for user in display_user():
                    print(f"{user.first_name} {user.last_name} has an account for {site}")

                print('\n')
            else:
                print('\n')
                print("there are no accounts at the moment")
                print('\n')

        elif short_code == "ext":
            print(":/ See you soon then...")
            break
        else:
            print(" :( Only key in the allowed actions !!")


if __name__ == '__main__':
    main()
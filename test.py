from user import User
from info import info
import random

    #creatingg a new usser
def create_user(firsn, lastn, phone, email):
    new_user = User(firsn, lastn, phone, email)
    return new_user
def save_cred(credential):
    
    credential.save_credential()
    
def save_user(user):
   
    user.save_user_details()
    
def del_cred(credential):
   
    credential.delete_credential()
    
def del_user(user):
   
    user.delete_user()
    
def display_user():
    
    return User.display_users()

def create_credential(name, word, email):
   
    new_credential = info(name, word, email)
    return new_credential

def display_cred():
    
    return info.display_credential()

def main():

    print("Welcome to your Password Locker, choose your path")

    while True:
        print("Allowed Actions: \n acu - create a new user account with a user-defined password\n acc - create a new user account with a auto-generated password\n disp - display all user accounts \n ext -exit the contact list \n")

        short_code = input().lower()

        if short_code == 'acu':
            print("New User")
            print("-"*10)
            print("hello! What account do you want to create?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ...")
            user_name = input()

            print("Enter Password ...")
            pword = input()

            save_user(create_user(f_name, l_name, p_number, e_address))
            save_cred(create_credential(user_name, pword, e_address))  
            print('\n')
            print(f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(f" The username is {user_name} and the password is {pword}")
            print('\n')

        elif short_code == 'acc':
            print("New User")
            print("-" * 10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()

            print("Last name ...", )
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ... NB: we will provide you with an encripted password ")
            user_name = input()

            s = "abcdefghijklmnopqrstuvwxyzABC!@#$%^&*()?DEFGHIJKLMNO01234567890PQRSTUVWXYZ"
            pword = "".join(random.sample(s, 8))

            save_user(create_user(f_name,l_name,p_number,e_address))  
            save_cred(create_credential(user_name, pword, e_address)) 
            print('\n')
            print(f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(f" The username is {user_name} and the password is {pword}")
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
                print("You don't seem to have any existing accounts")
                print('\n')

        elif short_code == "ext":
            print(":/ See you soon then...")
            break
        else:
            print(" :( Only key in the allowed actions !!")


if __name__ == '__main__':
    main()
import pyperclip

class User:
    
    pass

    user_list = []
    
    def __init__(self,first_name,last_name,phone_number,email):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
    user_list = [] #this is a usser list
    
    #saving user information into usser list
    def save_user(self):
        User.user_list.append(self)
        
    #deleting user information 
    
    def delete_user(self):
        User.user_list.remove(self)
    
    #using @classmethod  to find the corresponding date usser   
    @classmethod
    def find_by_number(cls,number):
        for user in cls.user_list:
            if user.phone_number == number:
                return user
            
    #checking if a user exists
    @classmethod
    def user_exists(cls,number):
        for user in cls.user_list:
            if user.phone_number == number:
                return True

        return False
    #returning the user list
    @classmethod
    def display_users(cls):
        return cls.user_list
    @classmethod
    def copy_email(cls,number):
        user_found = User.find_by_number(number)
        pyperclip.copy(user_found.email)
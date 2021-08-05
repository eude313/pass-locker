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

from user import User
from info import info
import random

    #creatingg a new usser
def create_user(firsn, lastn, phone, email):
    new_user = User(firsn, lastn, phone, email)
    return new_user
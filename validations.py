import re
import random

from modelUser import User
from tkinter import messagebox

PATTERN_USER = re.compile('^[a-zA-Z\d]{5,}$')
PATTERN_PASSWORD = re.compile('^([A-Z]+)([a-zA-Z\d]+)$')

def validation_data(user_response, password_response):
    if PATTERN_USER.search(user_response) == None or PATTERN_PASSWORD.search(password_response) == None:
        messagebox.showinfo('user',"Credenciales no válidas")    
    else:
        messagebox.showinfo('user',"Usuario registrado")    
        with open("./docs/nodes.txt","a+") as file:
            user = User(user_response, password_response)
            if not cache_users[:-1]:
                user.id = random.randrange(1000)
            else:
                user.id = cache_users[:-1].id + 1
            print(user_response)
            print(user)
            file.write("{}\n".format(user.username))


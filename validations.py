import re
from random import randrange
from modelUser import User
from tkinter import messagebox

# Constants
CACHE = list()
PATTERN_USER = re.compile('^[a-zA-Z\d]{5,}$')
PATTERN_PASSWORD = re.compile('^([A-Z]+)([a-zA-Z\d]+)$')

def validation_data(user_response, password_response):
    if PATTERN_USER.search(user_response) == None or PATTERN_PASSWORD.search(password_response) == None:
        messagebox.showinfo('user',"Credenciales no válidas")    
    else:
        messagebox.showinfo('user',"Usuario registrado")    
        with open("./docs/nodes.txt","a+") as file:
            user = User(user_response, password_response)
            num = randrange(1000)
            while num in CACHE:
                num = randrange(1000)
            user.id = num
            CACHE.append(num)
            print(user_response)
            print(user)
            file.write("{}\n".format(user.username))


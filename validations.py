import re
from tkinter import messagebox
PATTERN_USER = re.compile('^[a-zA-Z\d]{5,}$')
PATTERN_PASSWORD = re.compile('^([A-Z]+)([a-zA-Z\d]+)$') 


def validation_data(user_response,password_response):

    if PATTERN_USER.search(user_response) == None or PATTERN_PASSWORD.search(password_response) == None:
        messagebox.showinfo('user',"Credensiales no validas")    
    else:
        messagebox.showinfo('user',"Usuario registrado")    
        with open("nodes.txt","a+") as file:
            file.write("{}\n".format(user_response))
    

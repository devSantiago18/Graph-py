import re
from tkinter import messagebox

PATTERN_USER = re.compile('^[a-zA-Z\d]{5,}$')
PATTERN_PASSWORD = re.compile('^([A-Z]+)([a-zA-Z\d]+)$') 


def validation_data(user_response,password_response):
    if PATTERN_USER.search(user_response) == None :
        messagebox.showinfo('user',"Usuario  no valido")    
    if PATTERN_PASSWORD.search(password_response) == None:
        messagebox.showinfo('user',"Contraseña no valido")    
    else:
        messagebox.showinfo('user',"Usuario registrado")    
        file = open("nodes.txt","a+")
        file.write("{}\n".format(user_response))
        file.close()
    

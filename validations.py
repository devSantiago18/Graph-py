import re
import csv
from random import randrange, choice
from modelUser import User
from tkinter import messagebox

# Constants
PATH_CSV = "./docs/nodes.csv"
PATTERN_USER = re.compile('^[a-zA-Z\d]{5,}$')
PATTERN_PASSWORD = re.compile('^([A-Z]+)([a-zA-Z\d]+)$')


def init_cache() -> list:
    # Returns a list of saved ids
    cache = []
    try:
        with open(PATH_CSV, mode="r") as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            cache = [row[0] for row in reader]
        return cache
    except FileNotFoundError:
        print('file not found')
        return []
    except:
        print('No se fro bro')


def validation_data(user_response, password_response):
    if PATTERN_USER.search(user_response) == None or PATTERN_PASSWORD.search(password_response) == None:
        messagebox.showinfo('user', "Credenciales no válidas")
    else:
        messagebox.showinfo('user', "Usuario registrado")
        cache = init_cache()
        print(cache)
        with open(PATH_CSV, mode="a+", newline='') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=',')
            num_id = randrange(1000)
            while num_id in cache:
                num_id = randrange(1000)
            user = User(num_id, user_response, password_response)
            if len(cache) > 0:
                for _ in range(len(cache)):
                    user.adjacents.append(choice(cache))
            print(user)
            file_writer.writerow(user.to_list())

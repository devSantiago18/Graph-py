try:
    from Tkinter import *
except:
    from tkinter import *

from validations import validation_data
from graph import create_graph

# Constants
HEIGHT_W = 30
WIDTH_W = 200

class Window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.config(bd=15)
        self.resizable(0,0)
        self.title('User validations')

        frame = Frame(self , width=430 , height=280)
        frame.pack(fill='both' , expand=1)
        frame.config(bg='black')
        frame.config(bd=25)
        self.user_response = StringVar()
        self.password_response = StringVar()

        userlabel = Label(frame,text='Username')
        userlabel.place(x=15, y=10, width=WIDTH_W , height=HEIGHT_W)
        userlabel.config()

        user_entry = Entry(frame,textvariable=self.user_response)
        user_entry.place(x=15, y=50, width=WIDTH_W , height=HEIGHT_W)

        passwordlabel = Label(frame,text='Password',)
        passwordlabel.place(x=15, y=100, width=WIDTH_W , height=HEIGHT_W)
        passwordlabel.config()

        password_entry = Entry(frame,textvariable=self.password_response)
        password_entry.place(x=15, y=140, width=WIDTH_W , height=HEIGHT_W)
        password_entry.config(show="*")
        
        btn_submit = Button(frame, text='Submit' , command=self.submit_data )
        btn_submit.place(x=15, y=210,width=WIDTH_W , height=HEIGHT_W)


        btn_show = Button(frame,text="Show graph",command=create_graph)
        btn_show.place( x=225, y=210, width=170 , height=HEIGHT_W)

    def submit_data(self):
        validation_data(self.user_response.get(),self.password_response.get())
        self.user_response.set("")
        self.password_response.set("")
    
    
from tkinter import Tk , Frame , Label , Button , Entry , messagebox
from tkinter import DISABLED , StringVar
from validations import validation_data
from graph import create_graph

#vars

##################
# root-frame config
root = Tk()
root.config(bd=15)
root.resizable(0,0)
root.title('User validations')

frame = Frame(root , width=430 , height=280)
frame.pack(fill='both' , expand=1)
frame.config(bg='lightblue')
frame.config(bd=25)
#####################

#functions
def submit_data():
    validation_data(user_response.get(),password_response.get())
    user_response.set("")
    password_response.set("")
    
    
# entry
user_response = StringVar()
password_response = StringVar()

userlabel = Label(frame,text='Username')
userlabel.place(x=15, y=10, width=200 , height=30)
userlabel.config(bg='lightblue')

user_entry = Entry(frame,textvariable=user_response).place(x=15, y=50, width=200 , height=30)

passwordlabel = Label(frame,text='Password',)
passwordlabel.place(x=15, y=100, width=200 , height=30)
passwordlabel.config(bg='lightblue')

password_entry = Entry(frame,textvariable=password_response)
password_entry.place(x=15, y=140, width=200 , height=30)
password_entry.config(show="*")



# submit data
Button(frame, text='Submit' , command=submit_data ).place(x=15, y=210,width=200 , height=30)

# Button create graph
Button(frame,text="Show graph",command=create_graph).place( x=225, y=210, width=170 , height=30)
root.mainloop()
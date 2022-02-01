from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk
import mysql.connector
from Manage_Window import *
#from Manage_Users import *


# look into auth fns

def auth():
    global user
    # global cur
    # con = mysql.connector.connect(host="localhost", user="root", password="root", database="test76", port=3306)
    # cur = con.cursor()

    user = info1.get()
    passs = info2.get()

    Librarian = "Sowmesh Sharma"
    password = "sharmasowmesh123"

    if (user != Librarian) or (passs != password):
        messagebox.showerror("ERROR!","Incorrect Username/Password")
        return
        #UserId doesnt exist :
    else:
        ManageWindow(root)

    Submit.destroy()
    labelFrame.destroy()
    lb1.destroy()
    info1.destroy()
    info2.destroy()
    quitBtn.destroy()

def gui_auth(root1):
    root1.destroy()

    global Submit, labelFrame, lb1, info1, info2, quitBtn, root, Canvas1, status

    # declare the window
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="My Library", bg='black', fg='white', font=('times new roman', 50,'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Username
    lb1 = Label(labelFrame, text="Username", bg='black', fg='white',font=('courier',27))
    lb1.place(relx=0.07, rely=0.2)

    info1 = Entry(labelFrame,font=('times new roman',15,'bold'))
    info1.place(relx=0.3, rely=0.2, relwidth=0.62,relheight=0.12)

    # Password
    lb2 = Label(labelFrame, text="Password", bg='black', fg='white',font=('courier',27))
    lb2.place(relx=0.07, rely=0.4)

    info2 = Entry(labelFrame,font=('times new roman',15,'bold'),show='*')
    info2.place(relx=0.3, rely=0.4, relwidth=0.62,relheight=0.12)

    # Submit Button
    Submit = Button(root, text="Submit", bg='#d1ccc0', fg='black',font=('times new roman',20),command=auth)
    Submit.place(relx=0.28, rely=0.65, relwidth=0.18, relheight=0.08)

    #Quit Button
    quitBtn = Button(root, text="Quit", bg='#d1ccc0', fg='black', command=root.destroy,font=('times new roman',20))
    quitBtn.place(relx=0.53, rely=0.65, relwidth=0.18, relheight=0.08)

    root.mainloop()

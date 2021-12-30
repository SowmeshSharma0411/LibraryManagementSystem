
#import mysql.connector
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from main import *

def auth():
    #global cur
    #con = mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
    #cur = con.cursor()

    user=info1.get()
    passs=info2.get()

    Librarian="abc"
    password="abc"

    if (user != Librarian) or (passs != password):
        quit()
    else:
        root.destroy()
        myfunc()

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
    root.geometry("600x500")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Authentication Window", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Username
    lb1 = Label(labelFrame, text="Librarian : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    info1 = Entry(labelFrame)
    info1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Password
    lb2 = Label(labelFrame, text="Password : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    info2 = Entry(labelFrame)
    info2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Submit Button
    Submit = Button(root, text="Submit", bg='#d1ccc0', fg='black', command=auth)
    Submit.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #Quit Button
    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

#gui_auth()
#auth()






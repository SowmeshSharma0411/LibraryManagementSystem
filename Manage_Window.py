from tkinter import *
from tkinter import ttk
import tkinter.ttk
from Manage_Users import *
from tkinter import messagebox
from main import myfunc
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from functools import partial
import Auth
import webbrowser

global root


def ManageWindow(root1):
    root1.destroy()

    root = Tk()
    root.title("Dashboard")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="DASHBOARD", bg='black', fg='white', font=('baskerville old face', 50,'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Manage Users
    Users = Button(labelFrame, text="Manage Users", bg='black', fg='white', font=('baskerville old face', 25),command=partial(ManageUsers,root))
    Users.place(relx=0, rely=0, relwidth=1, relheight=1 / 3)

    # Manage Books
    Books = Button(labelFrame, text="Manage Books", bg='black', fg='white', font=('baskerville old face', 25),command=partial(ManageBooks,root))
    Books.place(relx=0, rely=1/3, relwidth=1, relheight=1 / 3)

    #Manage Borrowers
    Borrowers=Button(labelFrame, text='Manage Borrowers', bg='black', fg='white', font=('baskerville old face', 25),command=partial(myfunc,root))
    Borrowers.place(relx=0,rely=2/3,relwidth=1,relheight=1/3)

    adminframe = Frame(root, bg='black')
    adminframe.place(relx=0.78, rely=0.008, relwidth=0.2, relheight=0.05)
    adminlabel = Label(adminframe, text='User: '+str(Auth.user), font=('times new roman', 17, 'bold'), fg='white', bg='black')
    adminlabel.place(relx=0, rely=0, relheight=1, relwidth=1)

    logoutbtn = Button(root, bg='black', fg='white', text='LOG OUT', font=('baskerville old face', 20, 'bold'),
                       borderwidth=6, relief=RAISED,command=partial(Auth.gui_auth,root))
    logoutbtn.place(relx=0.78, rely=0.063, relheight=0.07, relwidth=0.15)

    def openhtml():
        #convert into pdf
        pdf="LMS_Project_Report_v0.2.pdf"
        webbrowser.open_new_tab("LMS_Project_Report_v0.2.pdf")
    helpbtn = Button(root, bg='black', fg='white', text='Help', font=('times new roman', 20, 'bold'), borderwidth=6,
                     relief=RAISED,command=openhtml)
    helpbtn.place(relx=0.05, rely=0.008, relwidth=0.15, relheight=0.07)




def ManageBooks(root1):
        root1.destroy()

        root = Tk()
        root.title("Manage Books")
        root.minsize(width=400, height=400)
        root.geometry("1600x800")

        Canvas3 = Canvas(root)

        Canvas3.config(bg="#ff6e40")
        Canvas3.pack(expand=True, fill=BOTH)

        headingFrame3 = Frame(root, bg="#FFBB00", bd=5)
        headingFrame3.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        headingLabel3 = Label(headingFrame3, text="Manage Books", bg='black', fg='white',
                              font=('times new roman', 30, 'bold'))
        headingLabel3.place(relx=0, rely=0, relwidth=1, relheight=1)

        labelFrame3 = Frame(root, bg='black')
        labelFrame3.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

        # Add Book
        AddB = Button(labelFrame3, text="Add Books", bg='black', fg='white', font=('baskerville old face', 25),command=partial(addBook,root))
        AddB.place(relx=0, rely=0, relwidth=1, relheight=1 / 3)

        # Delete Book
        DeleteB = Button(labelFrame3, text="Delete Books", bg='black', fg='white', font=('baskerville old face', 25),command=partial(delete,root)) # command by Suvan and Sowmesh
        DeleteB.place(relx=0, rely=1 / 4, relwidth=1, relheight=1 / 3)

        # View Books
        ViewB = Button(labelFrame3, text="View Books", bg='black', fg='white', font=('baskerville old face', 25),command=partial(View,root,1))#command by Suvan and Sowmesh
        ViewB.place(relx=0, rely=2 / 4, relwidth=1, relheight=1 / 3)

        #Quit Button :
        quitBtn = Button(labelFrame3, text="Quit", bg='black', fg='white', font=('baskerville old face', 25), command=partial(ManageWindow, root))
        quitBtn.place(relx=0, rely=3/4, relwidth=1, relheight=1/3)




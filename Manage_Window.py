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

global root


'''def ManageUsers(root1):
    root1.destroy()

    root = Tk()
    root.title("Manage Users")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    Canvas2 = Canvas(root)

    Canvas2.config(bg="#ff6e40")
    Canvas2.pack(expand=True, fill=BOTH)

    headingFrame2 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel2 = Label(headingFrame2, text="Manage Users", bg='black', fg='white',
                          font=('times new roman', 30, 'bold'))
    headingLabel2.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame2 = Frame(root, bg='black')
    labelFrame2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Display Current Users  # Need to display from database  # must be done by Sowmesh and Suvan
    Display = Button(labelFrame2, text="Display Current Users", bg='black', fg='white', font=('courier', 15))
    Display.place(relx=0, rely=0, relwidth=1, relheight=1 / 4)

    # Add Users
    Add = Button(labelFrame2, text="Add New User", bg='black', fg='white', font=('courier', 15), command=AddUser)
    Add.place(relx=0, rely=1 / 4, relwidth=1, relheight=1 / 4)

    # Update Details  # need to be done by Sowmesh and Suvan
    Update = Button(labelFrame2, text='Update Details', bg='black', fg='white', font=('courier', 15))
    Update.place(relx=0, rely=2 / 4, relwidth=1, relheight=1 / 4)

    # Delete Users # by Sowmesh and Suvan
    Delete = Button(labelFrame2, text='Delete User', bg='black', fg='white', font=('courier', 15))
    Delete.place(relx=0, rely=3 / 4, relwidth=1, relheight=1 / 4)'''

#Do we Really need to have : Update User Details and Delete User ? :


def ManageWindow():
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
    Users = Button(labelFrame, text="Manage Users", bg='black', fg='white', font=('courier', 15),command=partial(ManageUsers,root))
    Users.place(relx=0, rely=0, relwidth=1, relheight=1 / 3)

    # Manage Books
    Books = Button(labelFrame, text="Manage Books", bg='black', fg='white', font=('courier', 15),command=partial(ManageBooks,root))
    Books.place(relx=0, rely=1/3, relwidth=1, relheight=1 / 3)

    #Manage Borrowers
    Borrowers=Button(labelFrame, text='Manage Borrowers', bg='black', fg='white', font=('courier', 15),command=partial(myfunc,root))
    Borrowers.place(relx=0,rely=2/3,relwidth=1,relheight=1/3)




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
        AddB = Button(labelFrame3, text="Add Books", bg='black', fg='white', font=('courier', 15),command=partial(addBook,root))
        AddB.place(relx=0, rely=0, relwidth=1, relheight=1 / 3)

        # Delete Book
        DeleteB = Button(labelFrame3, text="Delete Books", bg='black', fg='white', font=('courier', 15),command=partial(delete,root)) # command by Suvan and Sowmesh
        DeleteB.place(relx=0, rely=1 / 3, relwidth=1, relheight=1 / 3)

        # View Books
        ViewB = Button(labelFrame3, text="View Books", bg='black', fg='white', font=('courier', 15),command=partial(View,root))#command by Suvan and Sowmesh
        ViewB.place(relx=0, rely=2 / 3, relwidth=1, relheight=1 / 3)


# def ManageBorrowers():
#     root = Tk()
#     root.title("Manage Borrowers")
#     root.minsize(width=400, height=400)
#     root.geometry("1600x800")
#
#     Canvas4 = Canvas(root)
#
#     Canvas4.config(bg="#ff6e40")
#     Canvas4.pack(expand=True, fill=BOTH)
#
#     headingFrame4 = Frame(root, bg="#FFBB00", bd=5)
#     headingFrame4.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)
#
#     headingLabel4 = Label(headingFrame4, text="Manage Borrow", bg='black', fg='white',
#                           font=('times new roman', 30, 'bold'))
#     headingLabel4.place(relx=0, rely=0, relwidth=1, relheight=1)
#
#     labelFrame4 = Frame(root, bg='black')
#     labelFrame4.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
#
#     # Issue Books
#     Issue = Button(labelFrame4, text="Issue Book", bg='black', fg='white', font=('courier', 15))
#     Issue.place(relx=0, rely=0, relwidth=1, relheight=1 / 2)
#
#     # Return Books
#     Return = Button(labelFrame4, text="Return Book", bg='black', fg='white', font=('courier', 15))
#     Return.place(relx=0, rely=1 / 2, relwidth=1, relheight=1 / 2)


'''def AddUser():
    root = Tk()
    root.title("Add User")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    Canvas5 = Canvas(root)

    Canvas5.config(bg="#ff6e40")
    Canvas5.pack(expand=True, fill=BOTH)

    headingFrame5 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame5.place(relx=0.2, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel5 = Label(headingFrame5, text="Add User", bg='black', fg='white',
                         font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel5.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame5 = Frame(root, bg='black')
    labelFrame5.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

    # labelFrame5b = Frame(root, bg='black')
    # labelFrame5b.place(relx=0.05, rely=0.25, relwidth=0.8, relheight=0.5)


    # Name
    lb5 = Label(labelFrame5, text="Name", bg='black', fg='white', font=('courier', 23))
    lb5.place(relx=0.07, rely=0.07)

    info5 = Entry(labelFrame5,font=('times new roman',15,'bold'))
    info5.place(relx=0.2, rely=0.07, relwidth=0.7,relheight=0.08)

    lb5b = Label(labelFrame5, text="SRN ", bg='black', fg='white', font=('courier', 23))
    lb5b.place(relx=0.07, rely=0.2)

    info5b = Entry(labelFrame5, font=('times new roman', 15, 'bold'))
    info5b.place(relx=0.2, rely=0.21, relwidth=0.7, relheight=0.08)

    lb5c = Label(labelFrame5, text="Branch ", bg='black', fg='white', font=('courier', 23))
    lb5c.place(relx=0.07, rely=0.34)

    comMemberc = tkinter.ttk.Combobox(labelFrame5, font=('times new roman', 15, 'bold'), width=18,
                                     state='readonly')  # adding drop down box
    comMemberc['value'] = ('CSE', 'ECE', 'EEE','Mechanical Engineering','Biotechnology')  # values in the drop down box
    comMemberc.place(relx=0.2, rely=0.35,relwidth=0.7,relheight=0.08)

    lb5d = Label(labelFrame5, text="Semester ", bg='black', fg='white', font=('courier', 23))
    lb5d.place(relx=0.05, rely=0.48)

    comMemberd = tkinter.ttk.Combobox(labelFrame5, font=('times new roman', 15, 'bold'), width=18,
                                      state='readonly')  # adding drop down box
    comMemberd['value'] = (1,2,3,4,5,6,7,8)  # values in the drop down box
    comMemberd.place(relx=0.2, rely=0.49, relwidth=0.7, relheight=0.08)

    def Submit_5():
         #UserAdd()  # need to define UserAdd fn which is the fn to add the user into database... must be done by sowmesh and suvan
         messagebox.showinfo('Success','User Added Successfully') # need to add fn to show error as well


    #Submit Button
    Submit5 = Button(labelFrame5, text="Submit", bg='#d1ccc0', fg='black',font=('times new roman',20),command=Submit_5)
    Submit5.place(relx=0.3, rely=0.7, relwidth=0.18, relheight=0.08)'''

    #root.mainloop() #after adding all option remove this call

#Why AddBooks ??

'''def AddBook():
    root = Tk()
    root.title("Add Book")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    Canvas6 = Canvas(root)

    Canvas6.config(bg="#ff6e40")
    Canvas6.pack(expand=True, fill=BOTH)

    headingFrame6 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame6.place(relx=0.2, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel6 = Label(headingFrame6, text="Add Book", bg='black', fg='white',
                         font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel6.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame6 = Frame(root, bg='black')
    labelFrame6.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

    # labelFrame5b = Frame(root, bg='black')
    # labelFrame5b.place(relx=0.05, rely=0.25, relwidth=0.8, relheight=0.5)


    # BID shouldnt be asked :
    lb6 = Label(labelFrame6, text="Book ID", bg='black', fg='white', font=('courier', 23))
    lb6.place(relx=0.07, rely=0.07)

    info6 = Entry(labelFrame6,font=('times new roman',15,'bold'))
    info6.place(relx=0.2, rely=0.07, relwidth=0.7,relheight=0.08)

    #If u guys want i can autofill the BID here using a SQL Query : BID=AutoIncrement :

    lb6b = Label(labelFrame6, text="Title ", bg='black', fg='white', font=('courier', 23))
    lb6b.place(relx=0.07, rely=0.2)

    info6b = Entry(labelFrame6, font=('times new roman', 15, 'bold'))
    info6b.place(relx=0.2, rely=0.21, relwidth=0.7, relheight=0.08)

    lb6c = Label(labelFrame6, text="Author ", bg='black', fg='white', font=('courier', 23))
    lb6c.place(relx=0.07, rely=0.34)

    info6c = Entry(labelFrame6, font=('times new roman', 15, 'bold'))
    info6c.place(relx=0.2, rely=0.35, relwidth=0.7, relheight=0.08)

    def Submit_6():
        #BookAdd()  # need to define BookAdd fn which is the fn to add the book into database... must be done by sowmesh and suvan
        messagebox.showinfo('Success','Book Added Successfully') # need to add fn to show error as well

    #Submit Button
    Submit6 = Button(labelFrame6, text="Submit", bg='#d1ccc0', fg='black',font=('times new roman',20),command=Submit_6)
    Submit6.place(relx=0.3, rely=0.7, relwidth=0.18, relheight=0.08)'''






























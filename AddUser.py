#Adding new user to users table :

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector


def userRegister():
    #SlNo=1,2,3......Maybe AutoGen Fr now
    srn = userInfo1.get()
    roll = userInfo2.get()
    first = userInfo3.get()
    last = userInfo4.get()
    address=userInfo5.get()
    mobile=userInfo6.get()
    mail=userInfo7.get()
    insertdata = "insert into " + userTable +" (SRN,RollNo,FirstName,LastName,Address,Mobile,Email) values('" + srn + "','" + roll + "','" + first + "','" + last + "','" + address + "','" + mobile + "','" + mail+" )"
    try:
        cur.execute(insertdata)
        con.commit()
        messagebox.showinfo('Success', "User added successfully")
    except:
        messagebox.showinfo("Error", "Can't add user into Database")

    root.destroy()


def adduser():
    global userInfo1, userInfo2, userInfo3, userInfo4,userInfo5,userInfo6,userInfo7, Canvas1, con, cur, userTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase = "db"

    con = mysql.connector.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here
    userTable = "users"
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Users", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # SRN
    lb1 = Label(labelFrame,text="SRN : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    userInfo1 = Entry(labelFrame)
    userInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)

    # RollNo
    lb2 = Label(labelFrame, text="RollNo : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.3, relheight=0.08)

    userInfo2 = Entry(labelFrame)
    userInfo2.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    # FirstName
    lb3 = Label(labelFrame, text="FirstName : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.40, relheight=0.08)

    userInfo3 = Entry(labelFrame)
    userInfo3.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # LastName
    lb4 = Label(labelFrame, text="LastName : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.5, relheight=0.08)

    userInfo4 = Entry(labelFrame)
    userInfo4.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    #Address
    lb5 = Label(labelFrame, text="Address : ", bg='black', fg='white')
    lb5.place(relx=0.05, rely=0.6, relheight=0.08)

    userInfo5 = Entry(labelFrame)
    userInfo5.place(relx=0.3, rely=0.6, relwidth=0.62, relheight=0.08)

    #Mobile
    lb6 = Label(labelFrame, text="Mobile No. : ", bg='black', fg='white')
    lb6.place(relx=0.05, rely=0.7, relheight=0.08)

    userInfo6 = Entry(labelFrame)
    userInfo6.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.08)

    #Email
    lb7 = Label(labelFrame, text="Email Id : ", bg='black', fg='white')
    lb7.place(relx=0.05, rely=0.8, relheight=0.08)

    userInfo7 = Entry(labelFrame)
    userInfo7.place(relx=0.3, rely=0.8, relwidth=0.62, relheight=0.08)


    # Submit Button
    SubmitBtn = Button(root, text="Submit", bg='#d1ccc0', fg='black', command=userRegister)
    SubmitBtn.place(relx=0.28, rely=0.95, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.95, relwidth=0.18, relheight=0.08)

    root.mainloop()

    #Instead of status : Copies : This will come when the borrow fnc comes intom pic
    #No duplicate book can be added :
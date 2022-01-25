import time
from tkinter import *
from tkinter import ttk
import tkinter.ttk
from functools import partial

from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from ReturnBook import *
from Auth import *
from fines import *
from ViewBorrowers import *
import Manage_Window
from Manage_Window import *
from searchfunc import *

import datetime

import mysql.connector

mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor(buffered=True)


def myfunc(root1):
   root1.destroy()

   global root,Entry1b,Entry2,Entry2b,Entry3,Entry3b,Entry4

   global member_var, srn_var, first_var, last_var, bookid_var, booktitle_var, author_var, dateborrowed_var, datedue_var, search_var
   root=Tk()
   root.title('Library Management System')
   root.geometry('1600x800')

   member_var=StringVar()
   srn_var=StringVar()
   first_var=StringVar()
   last_var = StringVar()
   bookid_var = StringVar()
   booktitle_var = StringVar()
   author_var = StringVar()
   dateborrowed_var = StringVar()
   datedue_var = StringVar()

   search_var=StringVar()




   l1=Label(text='LIBRARY MANAGEMENT SYSTEM',bg='#ff6e40',fg='red',borderwidth=10,relief=RIDGE,font=('Times New Roman',50,'bold',),padx=2,pady=6).place(x=0,y=0,width=1275,height=100)

   frame=Frame(root,bg='#ff6e40').place(x=0,y=102,width=1275,height=570)

   # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& FRONT END &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

   # =========================================================================DataFrameLeft====================================================

   DataFrameLeft=LabelFrame(frame,bg='#ff6e40',text='Library Member Information',fg='midnightblue',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=0,y=102,width=750,height=445)

   lbl1=Label(frame,text='Member Type',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl1.place(x=0.03,y=130)
   comMember=tkinter.ttk.Combobox(DataFrameLeft,font=('times new roman',18,'bold'),width=13,state='readonly',textvariable=member_var)  #adding drop down box
   comMember['value']=('Student','Lecturer')   #values in the drop down box
   comMember.place(relx=0.18, rely=0.19,relwidth=0.35)

   lbl1b=Label(DataFrameLeft,text='Book ID',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl1b.place(relx=0.02,rely=0.45)
   Entry1b=Entry(bg='white',width=30,font=('times new roman',18,'bold'),textvariable=bookid_var).place(relx=0.13,rely=0.45,height=30,relwidth=0.16)

   lbl2=Label(DataFrameLeft,text='SRN No',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl2.place(relx=0.03,rely=0.25)
   Entry2=Entry(bg='white',width=20,font=('times new roman',18,'bold'),textvariable=srn_var).place(relx=0.18,rely=0.25,height=30.5,relwidth=0.35)

   def autoUser():
      userid=srn_var.get()
      fetchuser = "SELECT * FROM users WHERE SRN = " + str(userid)
      cur.execute(fetchuser)
      info = []
      for i in cur:
         info.append(i)
      first_var.set(info[0][2])
      last_var.set(info[0][3])



   b1 = Button(root, bg='chocolate', fg='black', borderwidth=5, relief=RAISED, text='Fetch',
               font=('Times new roman', 10, 'bold'), command=autoUser).place(relx=0.53,rely=0.25,height=30.5,relwidth=0.07)

   lbl2b=Label(DataFrameLeft,text='Book Title',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl2b.place(relx=0.02,rely=0.53)
   Entry2b=Entry(bg='white',width=30,font=('times new roman',18,'bold'),textvariable=booktitle_var).place(relx=0.13,rely=0.53,height=30,relwidth=0.16)

   lbl3=Label(DataFrameLeft,text='First Name',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl3.place(relx=0.03,rely=0.31)
   Entry3=Entry(bg='white',width=20,font=('times new roman',18,'bold'),textvariable=first_var).place(relx=0.18,rely=0.31,height=30.5,relwidth=0.35)

   lbl3b=Label(DataFrameLeft,text='Author',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl3b.place(relx=0.02,rely=0.62)
   Entry3b=Entry(bg='white',width=30,font=('times new roman',18,'bold'),textvariable=author_var).place(relx=0.13,rely=0.62,height=30,relwidth=0.16)

   lbl4=Label(DataFrameLeft,text='Last Name',bg='#ff6e40',fg='black',font=('Times new roman',18,'bold'))
   lbl4.place(relx=0.03,rely=0.37)
   Entry4=Entry(bg='white',width=20,font=('times new roman',18,'bold'),textvariable=last_var).place(relx=0.18,rely=0.37,height=30.5,relwidth=0.35)

   '''lbl4b=Label(DataFrameLeft,text='Borrow Date',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl4b.place(x=340,y=235)
   Entry4b=Entry(bg='white',width=30,font=('times new roman',13,'bold'),textvariable=dateborrowed_var).place(x=460,y=235,height=30)'''

   '''lbl5=Label(DataFrameLeft,text='Address Line 1',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl5.place(x=10,y=270)
   Entry5=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=270,height=30)'''

   '''lbl5b=Label(DataFrameLeft,text='Due Date',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl5b.place(x=340,y=270)
   Entry5b=Entry(bg='white',width=30,font=('times new roman',13,'bold'),textvariable=datedue_var).place(x=460,y=270,height=30)'''

   '''lbl6=Label(DataFrameLeft,text='Address Line 2',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl6.place(x=10,y=305)
   Entry6=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=305,height=30)'''

   '''lbl6b=Label(DataFrameLeft,text='Overdue',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl6b.place(x=340,y=305)
   Entry6b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=305,height=30)'''

   '''lbl7=Label(DataFrameLeft,text='Postal code',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl7.place(x=10,y=340)
   Entry7=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=340,height=30)'''

   '''lbl7b=Label(DataFrameLeft,text='Overdue Fine',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl7b.place(x=340,y=340)
   Entry7b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=340,height=30)'''

   '''lbl8=Label(DataFrameLeft,text='Mobile',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl8.place(x=10,y=375)
   Entry8=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=375,height=30)'''

   '''lbl8b=Label(DataFrameLeft,text='Actual Price',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl8b.place(x=340,y=375)
   Entry8b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=375,height=30)'''

   # ===============================================================DataFrameRight=========================================================

   DataFrameRight=LabelFrame(frame,bg='#ff6e40',fg='midnightblue',text='Book Details',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=750,y=102,width=525,height=445)

   # Taking Books from the database into a list :
   b = []
   author = []

   s = "SELECT title FROM books"
   cur.execute(s)

   for x in cur:
      b.append(x)

   s = "SELECT author FROM books"
   cur.execute(s)

   for x in cur:
      author.append(x)

   def select(event=""):
      info=[]
      value=str(a.get(a.curselection()))
      x=value[2:-3]
      s = "SELECT bid, title, author FROM books WHERE title = '%s'" %x
      cur.execute(s)
      for i in cur:
         info.append(i)
         break
      bookid_var.set(info[0][0])
      booktitle_var.set(info[0][1])
      author_var.set(info[0][2])

   a=Listbox(DataFrameRight,font=('times new roman',12,'bold'),width=59,height=17)
   a.bind("<<ListboxSelect>>",select)
   a.place(x=765,y=180)

   lbl8b = Label(DataFrameRight, text='Search', bg='#ff6e40', fg='black', font=('Times new roman', 18, 'bold'))
   lbl8b.place(x=765, y=130)
   Entry8b = Entry(bg='white', width=30, font=('times new roman', 18, 'bold'),textvariable=search_var)
   Entry8b.place(x=850, y=130, height=35, relwidth=0.3)

   #Hafta add a Go Button to get the thing working.
   b1 = Button(root, bg='chocolate', fg='black', borderwidth=5, relief=RAISED, text='Go',
               font=('Times new roman',10, 'bold'), command=partial(search,"title","books")).place(x=1200, y=130, height=35,relwidth=0.07)
   '''cur.execute("SELECT * from books WHERE flag=1")
   for i in cur:
      print(i)'''
   #search_var = always str

   for item in b:
      a.insert(END,item)


   scrlbar=Scrollbar(DataFrameRight)
   scrlbar.place(x=1245,y=180,height=345)

   a.config(yscrollcommand=scrlbar.set)
   scrlbar.config(command=a.yview())

   scrlbar.config(command=a.yview)
   #txt=Text(DataFrameRight,font=('Times new roman',12,'bold'),width=30,height=17).place(x=1010,y=130)      #ListBox

   #extractBid = "select SRN, FirstName, LastName, Mobile, Email, Bookid, BookTitle, Author, DateBorrowed, datedue from borrowers where SRN = '" + str(srn_var) + "'"

   def autoRet():
      l=[]
      l.append(srn_var.get())
      l.append(first_var.get())
      l.append(last_var.get())
      extractBid = "SELECT Bookid, BookTitle, Author FROM borrowers WHERE SRN = '%s'" %l[0]
      cur.execute(extractBid)
      info = []
      for i in cur:
         info.append(i)
      bookid_var.set(info[0][0])
      booktitle_var.set(info[0][1])
      author_var.set(info[0][2])

      #time.sleep(5)
      returnn(l)

   def Exit():
      root.destroy()
      ManageUsers()

   def Reset():
      member_var.set(""),
      srn_var.set(""),
      first_var.set(""),
      last_var.set(""),


   # ====================================Buttons===========================================

   frameBtn=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=472,width=1275,height=57)

   b1=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Issue',font=('Times new roman',30,'bold'),command=issuebook).place(x=6.8,y=556.8,width=230,height=80)
   b2=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Return',font=('Times new roman',30,'bold'),command=autoRet).place(x=240,y=556.8,width=230,height=80)
   b3=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Display Borrowers',font=('Times new roman',30,'bold'),command=View).place(x=480,y=556.8,width=230,height=80)
   b4=Button(frameBtn,bg='chocolate',fg='black',borderwidth=5,relief=RAISED,text='Reset',font=('Times new roman',30,'bold'),command=Reset).place(x=720,y=556.8,width=230,height=80)
   b5=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Exit',font=('Times new roman',30,'bold'),command=partial(Manage_Window.ManageWindow,root)).place(x=950,y=556.8,width=230,height=80)


   # ===================================================Info Bar==================================

   #Info=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=530,width=1275,height=120)

def issuebook():

   input_bookid = str(bookid_var.get())
   title = str(booktitle_var.get())
   author = str(author_var.get())
   input_userid = int(srn_var.get())
   name = str(first_var.get())
   last_name = str(last_var.get())

   '''con = mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
   cur = con.cursor()'''

   root2 = Tk()
   root2.title("Library")
   # root2.minsize(width=300,height=300)
   root2.geometry("1920x1080")
   valid = False
   type = "student"
   flag = 0

   cur.execute(
      "SELECT bid FROM books")
   for k in cur:
      a = k[0]
      if (a == input_bookid): # checks if the book id inputed is valid by cross checking with the existing book ids in the book database
         valid = True
   '''if valid == False:
      headingLabel = Label(root2, text="book id entered invalid", bg='black', fg='white', font=('Courier', 15))
      headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
      quitBtn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
      quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)
      root2.mainloop()
      return  # exits the program once the quit button is pressed and returns to the main menu'''

   # checking valid user id code, have not done it yet since there is no user database
   # checking which type the user is, faculty or student, have not done yet since there is no user database yet

   cur.execute("select * from borrowers where SRN=%s", (input_userid,))
   #If the person has some book already : He first has to return that : He will not be allowed to borrow any other book :
   l = []

   for k in cur:
      l.append(k)

   if(len(l)!=0):
      messagebox.showwarning("ERROR","Return the Book which you already have")
      return

   else:

      '''for k in cur:
         if k[8] != None:
      
            duedate2 = datetime.strptime(k[8], "%Y-%m-%d")
            if datetime.now() > duedate2:  # checks whether the current date is after the due date, have figured out how to compare dates (but for now I have used ">")
               l.append(k + (((
                                         datetime.now() - duedate2).days) * 2,))  # prints due books details such as book name, borrowed date,etc. it calculates fine for the due books and prints it ---Fine comes during return book only : 
               flag = 1'''

      #if type == "student" :
      #print("these books have fines pending for them, please pay the fine at the earliest to borrow a new book")

      # gui code for a dailog box specifying the above message
      '''headingLabel = Label(root2,
                           text="these books have fines pending for them, please pay the fine at the earliest to borrow a new book",
                           bg='black', fg='white', font=('Courier', 15))
      headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
      Label(root2, text="%-30s%-30s%-75s%-60s%-30s%-50s%-50s" % (
      'sl_no', 'book id', 'title', 'author', "id", "name", "last name"), bg='black', fg='white').place(relx=0.07,
                                                                                                       rely=0.1)
      Label(root2, text="----------------------------------------------------------------------------", bg='black',
            fg='white').place(relx=0.05, rely=0.2)

      c = 1
      y = 0.3
      print(l)
      for i in l:
         Label(root2, text="%-30s%-30s%-60s%-60s%-30s%-50s%-50s" % (str(c), i[1], i[2], i[3], i[4], i[5], i[6]),
               bg='black', fg='white').place(relx=0.08, rely=y)
         c += 1
         y += 0.1

      quitBtn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
      quitBtn.place(relx=0.53, rely=0.6, relwidth=0.18, relheight=0.08)

      root2.mainloop()
      return  # exits the program once the quit button is pressed and returns to the main menu
      # exit button to exit program and return to main menu'''

      '''if type == "faculty":
         print("please return the book at the earliest to borrow a new book")
         # gui code for a dailog box specifying the above message
         # exit button to exit program and return to main menu'''

      fetchuser="SELECT * FROM users WHERE SRN = "+str(input_userid)
      cur.execute(fetchuser)

      l=[]
      for i in cur:
         l.append(i)

      borrow_date = datetime.date.today()
      duedate = borrow_date + datetime.timedelta(days=14)
      duedate = str(duedate)
      borrow_date = str(borrow_date)
      val = (input_userid,name,last_name,l[0][-2],l[0][-1],input_bookid,title,author,borrow_date,duedate)
      cur.execute(
         "INSERT INTO borrowers (SRN,FirstName,LastName,Mobile,Email,Bookid,BookTitle,Author,DateBorrowed,datedue) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
         val)
      # inserts details of the borrowed book with user details into issued books table
      con.commit()

      fetchbooks = "SELECT copies FROM books WHERE title = '" + title + "'"
      cur.execute(fetchbooks)

      for i in cur:
         cpy = int(i[0][0])
      cpy -= 1
      addSql = "UPDATE books \nSET copies = '%s' \nWHERE title = '%s';" %(str(cpy),str(title))
      cur.execute(addSql)
      con.commit()
      # basic gui code for a dialog box----A summary Box must be displayed too :
      #print("success, book has been issued")
      headingLabel = Label(root2, text="book issued successfully", bg='black', fg='white', font=('Courier', 15))
      headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
      Label(root2, text="%-30s%-30s%-75s%-60s%-30s%-50s%-50s%-50s%-50s%-50s" % (
         'SRN','FirstName','LastName','Mobile','Email','Bookid','BookTitle','Author','DateBorrowed','datedue'), bg='black', fg='white').place(relx=0.07,
                                                                                                          rely=0.1)
      Label(root2, text="----------------------------------------------------------------------------", bg='black',
            fg='white').place(relx=0.05, rely=0.2)

      c = 1
      y = 0.3
      l=[]
      cur.execute("SELECT SRN,FirstName,LastName,Mobile,Email,Bookid,BookTitle,Author,DateBorrowed,datedue FROM borrowers WHERE SRN = "+str(input_userid))
      for i in cur:
         l.append(i)
      l1=[]
      #print(l)
      for i in l:
         l1=[]
         l1=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
         Label(root2, text="%-30s%-30s%-60s%-60s%-30s%-50s%-50s%-50s%-50s%-50s" %(l1),
               bg='black', fg='white').place(relx=0.08, rely=y)
         #c += 1
         y += 0.1

      quitBtn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
      quitBtn.place(relx=0.53, rely=0.6, relwidth=0.18, relheight=0.08)

      root2.mainloop()
      return

   #"Fetch" button to autofill first and last name after SRN : Suhas Include this Pls :
   # Borrow summary proper display of table : Formatting of strs thats all :--Suhas Do the formatting : This is the old window :
   #Search Optn
   #Also : TextBoxes look little off : correct em :
   #For autoEmails : A window List of all PPl who havent submitted the books on time; -Later


   #Stitch the fncs proeprly : quit Btns :(HOME) --Done
   #Update Search to search by FirstName : Last name, Email ID -Trying
   #Returned Successfully in return screen : + lil error handling : like no user while borrowing : -Imp
   #Add a dynamic alert/Notif in dashboard(eg : "This book" due date is on "this date")
   #GUI : of everything : align everything first : + Borrow window : make fonts the same.


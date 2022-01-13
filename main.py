from tkinter import *
from tkinter import ttk
import tkinter.ttk
from functools import partial

from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
#from AddBook import *
#from DeleteBook import *
#from ViewBooks import *
from ReturnBook import *
from Auth import *
from fines import *

import datetime

import mysql.connector

mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor(buffered=True)

def myfunc():
   global root,Entry1b,Entry2,Entry2b,Entry3,Entry3b,Entry4

   global member_var, srn_var, first_var, last_var, bookid_var, booktitle_var, author_var, dateborrowed_var, datedue_var

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




   l1=Label(text='LIBRARY MANAGEMENT SYSTEM',bg='powder blue',fg='red',borderwidth=10,relief=RIDGE,font=('Times New Roman',50,'bold',),padx=2,pady=6).place(x=0,y=0,width=1275,height=100)

   frame=Frame(root,bg='powder blue').place(x=0,y=102,width=1275,height=370)

   # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& FRONT END &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

   # =========================================================================DataFrameLeft====================================================

   DataFrameLeft=LabelFrame(frame,bg='powder blue',text='Library Member Information',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=0,y=102,width=750,height=370)

   lbl1=Label(frame,text='Member Type',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl1.place(x=10,y=130)
   comMember=tkinter.ttk.Combobox(DataFrameLeft,font=('times new roman',13,'bold'),width=18,state='readonly',textvariable=member_var)  #adding drop down box
   comMember['value']=('Student','Lecturer')   #values in the drop down box
   comMember.place(x=150,y=135)

   lbl1b=Label(DataFrameLeft,text='Book ID',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl1b.place(x=340,y=135)
   Entry1b=Entry(bg='white',width=30,font=('times new roman',13,'bold'),textvariable=bookid_var).place(x=460,y=135,height=25)

   lbl2=Label(DataFrameLeft,text='SRN No',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl2.place(x=10,y=165)
   Entry2=Entry(bg='white',width=20,font=('times new roman',13,'bold'),textvariable=srn_var).place(x=150,y=165,height=30)

   lbl2b=Label(DataFrameLeft,text='Book Title',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl2b.place(x=340,y=165)
   Entry2b=Entry(bg='white',width=30,font=('times new roman',13,'bold'),textvariable=booktitle_var).place(x=460,y=165,height=30)

   lbl3=Label(DataFrameLeft,text='First Name',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl3.place(x=10,y=200)
   Entry3=Entry(bg='white',width=20,font=('times new roman',13,'bold'),textvariable=first_var).place(x=150,y=200,height=30)

   lbl3b=Label(DataFrameLeft,text='Author',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl3b.place(x=340,y=200)
   Entry3b=Entry(bg='white',width=30,font=('times new roman',13,'bold'),textvariable=author_var).place(x=460,y=200,height=30)

   lbl4=Label(DataFrameLeft,text='Last Name',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl4.place(x=10,y=235)
   Entry4=Entry(bg='white',width=20,font=('times new roman',13,'bold'),textvariable=last_var).place(x=150,y=235,height=30)

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

   DataFrameRight=LabelFrame(frame,bg='powder blue',text='Book Details',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=750,y=102,width=525,height=370)

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

   a=Listbox(DataFrameRight,font=('times new roman',12,'bold'),width=29,height=16)
   a.bind("<<ListboxSelect>>",select)
   a.place(x=765,y=130)

   for item in b:
      a.insert(END,item)


   scrlbar=Scrollbar(DataFrameRight)
   scrlbar.place(x=985,y=130,height=322)

   a.config(yscrollcommand=scrlbar.set)
   scrlbar.config(command=a.yview())

   scrlbar.config(command=a.yview)
   txt=Text(DataFrameRight,font=('Times new roman',12,'bold'),width=30,height=17).place(x=1010,y=130)      #ListBox

   # ====================================Buttons===========================================

   l=[
   srn_var,
   first_var,
   last_var,
   ]

   frameBtn=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=472,width=1275,height=57)

   b1=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Borrow',font=('Times new roman',15,'bold'),command=issuebook).place(x=6.8,y=480,width=200,height=40)
   b2=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Return',font=('Times new roman',15,'bold'),command=partial(returnn,l)).place(x=205,y=480,width=200,height=40)
   b3=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Display Borrowers',font=('Times new roman',15,'bold')).place(x=404,y=480,width=200,height=40)#Should be Display Borrowers
   b4=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Reset',font=('Times new roman',15,'bold')).place(x=603,y=480,width=200,height=40)#Should be Reset
   b5=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Exit',font=('Times new roman',15,'bold'),command=root.destroy).place(x=802,y=480,width=230,height=40)


   # ===================================================Info Bar==================================

   Info=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=530,width=1275,height=120)


   #Fine=Box Should be removed : Instead a small Msg Box.

   #For autoEmails : A window List of all PPl who havent submitted the books on time;

#BorrowBook Fnc :

def issuebook():
   #global Entry1b, Entry2b, Entry3b, Entry2, Entry3, Entry4

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

      borrow_date = datetime.date.today()
      duedate = borrow_date + datetime.timedelta(days=14)
      duedate = str(duedate)
      borrow_date = str(borrow_date)
      val = (input_userid,name,last_name,input_bookid,title,author,borrow_date,duedate)
      cur.execute(
         "INSERT INTO borrowers (SRN,FirstName,LastName,Bookid,BookTitle,Author,DateBorrowed,datedue) values(%s,%s,%s,%s,%s,%s,%s,%s)",
         val)
      # inserts details of the borrowed book with user details into issued books table
      con.commit()
      # basic gui code for a dialog box----A summary Box must be displayed too :
      print("success, book has been issued")
      headingLabel = Label(root2, text="book issued successfully", bg='black', fg='white', font=('Courier', 15))
      headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)
      Label(root2, text="%-30s%-30s%-75s%-60s%-30s%-50s%-50s%-50s" % (
         'SRN','FirstName','LastName','Bookid','BookTitle','Author','DateBorrowed','datedue'), bg='black', fg='white').place(relx=0.07,
                                                                                                          rely=0.1)
      Label(root2, text="----------------------------------------------------------------------------", bg='black',
            fg='white').place(relx=0.05, rely=0.2)

      c = 1
      y = 0.3
      cur.execute("SELECT SRN,FirstName,LastName,Bookid,BookTitle,Author,DateBorrowed,datedue FROM borrowers WHERE SRN = "+str(input_userid))
      for i in cur:
         l.append(i)
      print(l)
      for i in l:
         Label(root2, text="%-30s%-30s%-60s%-60s%-30s%-50s%-50s%-50s" % (val),
               bg='black', fg='white').place(relx=0.08, rely=y)
         #c += 1
         y += 0.1

      quitBtn = Button(root2, text="Quit", bg='#f7f1e3', fg='black', command=root2.destroy)
      quitBtn.place(relx=0.53, rely=0.6, relwidth=0.18, relheight=0.08)

      root2.mainloop()
      return  # exits the program once the quit button is pressed and returns to the main menu
      # exit button to exit program and return to main menu


   #Also : 'copies' column in books must be updated once a book is borrowed.
   # Borrow summary proper display of table : Formatting of strs thats all :--Suhas Do the formatting : This is the old window :


   #-------------Return Fnc :-----------#

from tkinter import *
from tkinter import ttk
import tkinter.ttk

from PIL import ImageTk, Image
import mysql.connector
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from Auth import *

import mysql.connector

mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor()

def myfunc():

   root=Tk()
   root.title('Library Management System')
   root.geometry('1600x800')

   l1=Label(text='LIBRARY MANAGEMENT SYSTEM',bg='powder blue',fg='red',borderwidth=10,relief=RIDGE,font=('Times New Roman',50,'bold',),padx=2,pady=6).place(x=0,y=0,width=1275,height=100)

   frame=Frame(root,bg='powder blue').place(x=0,y=102,width=1275,height=370)

   # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& FRONT END &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

   # =========================================================================DataFrameLeft====================================================

   DataFrameLeft=LabelFrame(frame,bg='powder blue',text='Library Member Information',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=0,y=102,width=750,height=370)

   lbl1=Label(frame,text='Member Type',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl1.place(x=10,y=130)
   comMember=tkinter.ttk.Combobox(DataFrameLeft,font=('times new roman',13,'bold'),width=18,state='readonly')  #adding drop down box
   comMember['value']=('Admin Staff','Student','Lecturer')   #values in the drop down box
   comMember.place(x=150,y=135)

   lbl1b=Label(DataFrameLeft,text='Book ID',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl1b.place(x=340,y=135)
   Entry1b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=135,height=25)

   lbl2=Label(DataFrameLeft,text='SRN No',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl2.place(x=10,y=165)
   Entry2=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=165,height=30)

   lbl2b=Label(DataFrameLeft,text='Book Title',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl2b.place(x=340,y=165)
   Entry2b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=165,height=30)

   lbl3=Label(DataFrameLeft,text='First Name',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl3.place(x=10,y=200)
   Entry3=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=200,height=30)

   lbl3b=Label(DataFrameLeft,text='Author',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl3b.place(x=340,y=200)
   Entry3b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=200,height=30)

   lbl4=Label(DataFrameLeft,text='Last Name',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl4.place(x=10,y=235)
   Entry4=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=235,height=30)

   lbl4b=Label(DataFrameLeft,text='Borrow Date',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl4b.place(x=340,y=235)
   Entry4b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=235,height=30)

   lbl5=Label(DataFrameLeft,text='Address Line 1',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl5.place(x=10,y=270)
   Entry5=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=270,height=30)

   lbl5b=Label(DataFrameLeft,text='Due Date',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl5b.place(x=340,y=270)
   Entry5b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=270,height=30)

   lbl6=Label(DataFrameLeft,text='Address Line 2',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl6.place(x=10,y=305)
   Entry6=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=305,height=30)

   lbl6b=Label(DataFrameLeft,text='Overdue',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl6b.place(x=340,y=305)
   Entry6b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=305,height=30)

   lbl7=Label(DataFrameLeft,text='Postal code',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl7.place(x=10,y=340)
   Entry7=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=340,height=30)

   lbl7b=Label(DataFrameLeft,text='Overdue Fine',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl7b.place(x=340,y=340)
   Entry7b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=340,height=30)

   lbl8=Label(DataFrameLeft,text='Mobile',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl8.place(x=10,y=375)
   Entry8=Entry(bg='white',width=20,font=('times new roman',13,'bold')).place(x=150,y=375,height=30)

   lbl8b=Label(DataFrameLeft,text='Actual Price',bg='powder blue',font=('Times new roman',15,'bold'))
   lbl8b.place(x=340,y=375)
   Entry8b=Entry(bg='white',width=30,font=('times new roman',13,'bold')).place(x=460,y=375,height=30)

   # ===============================================================DataFrameRight=========================================================

   DataFrameRight=LabelFrame(frame,bg='powder blue',text='Book Details',font=('algerian',15,'bold'),borderwidth='10',relief=RIDGE,padx=0,pady=0).place(x=750,y=102,width=525,height=370)

   a=Listbox(DataFrameRight,font=('times new roman',12,'bold'),width=29,height=16)
   a.place(x=765,y=130)

   b=[]
   author=[]

   s="SELECT title FROM books"
   cur.execute(s)

   for x in cur:
      b.append(x)

   print(b)

   s="SELECT author FROM books"
   cur.execute(s)

   for x in cur:
      author.append(x)

   print(author)

   for item in b:
      a.insert(END,item)


   scrlbar=Scrollbar(DataFrameRight)
   scrlbar.place(x=985,y=130,height=322)

   a.config(yscrollcommand=scrlbar.set)
   scrlbar.config(command=a.yview())

   scrlbar.config(command=a.yview)
   txt=Text(DataFrameRight,font=('Times new roman',12,'bold'),width=30,height=17).place(x=1010,y=130)      #ListBox

   # ====================================Buttons===========================================

   frameBtn=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=472,width=1275,height=57)

   b1=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Add Data',font=('Times new roman',15,'bold'),command=addBook).place(x=6.8,y=480,width=200,height=40)
   b2=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Show Data',font=('Times new roman',15,'bold'),command=View).place(x=205,y=480,width=200,height=40)
   b3=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Update',font=('Times new roman',15,'bold')).place(x=404,y=480,width=200,height=40)
   b4=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Delete',font=('Times new roman',15,'bold'),command=delete).place(x=603,y=480,width=200,height=40)
   b5=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Reset',font=('Times new roman',15,'bold')).place(x=802,y=480,width=230,height=40)
   b6=Button(frameBtn,bg='navy',fg='yellow',borderwidth=5,relief=RAISED,text='Exit',font=('Times new roman',15,'bold'),command=root.destroy).place(x=1030.8,y=480,width=235,height=40)


   # ===================================================Info Bar==================================

   Info=Frame(root,bg='powder blue',borderwidth=10,relief=RIDGE,padx=20).place(x=0,y=530,width=1275,height=120)

   library_table=ttk.Treeview(Info,columns=('memtype','srn','firname','lastname','add1','add2','postcode','mobile','bid','btitle','author',
                                            'borrowdate','duedate','overdue','overdue_fine','price'))



   library_table.heading('memtype',text='Member Type')
   library_table.heading('srn',text='SRN No.')
   library_table.heading('firname',text='First Name')
   library_table.heading('lastname',text='Last Name')
   library_table.heading('add1',text='Address Line 1')
   library_table.heading('add2',text='Address Line 2')
   library_table.heading('postcode',text='Postal Code')
   library_table.heading('mobile',text='Mobile No.')
   library_table.heading('bid',text='Book ID')
   library_table.heading('btitle',text='Book Title')
   library_table.heading('author',text='Author')
   library_table.heading('borrowdate',text='Borrowed Date')
   library_table.heading('duedate',text='Due Date')
   library_table.heading('overdue',text='Overdue')
   library_table.heading('overdue_fine',text='Overdue Fine')
   library_table.heading('price',text='Price')

   library_table['show']='headings'
   library_table.place(x=0,y=530,width=1275,height=120)

   library_table.column('memtype',width=200)
   library_table.column('srn',width=150)
   library_table.column('firname',width=200)
   library_table.column('lastname',width=200)
   library_table.column('add1',width=300)
   library_table.column('add2',width=300)
   library_table.column('postcode',width=100)
   library_table.column('mobile',width=100)
   library_table.column('bid',width=150)
   library_table.column('btitle',width=200)
   library_table.column('author',width=200)
   library_table.column('borrowdate',width=100)
   library_table.column('duedate',width=100)
   library_table.column('overdue',width=100)
   library_table.column('overdue_fine',width=100)
   library_table.column('price',width=100)

   scrollbary=ttk.Scrollbar(Info,orient=VERTICAL,command=library_table.yview)
   scrollbary.place(x=1260,y=530,height=120)

   scrollbarx=ttk.Scrollbar(Info,orient=HORIZONTAL,command=library_table.xview)
   scrollbarx.place(x=0,y=630,width=1260)

   library_table.configure(yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)


   #Fine=Box Should be removed : Instead a small Msg Box.

   #For autoEmails : A window List of all PPl who havent submitted the books on time;
   #No lost books.

   #3Menus : Manage User : The new GUI Window + Manage Books + Manage Borrowers.

   #As soon as u login : Dashboard: (old proj) :

   #Add User : Another Fnc :
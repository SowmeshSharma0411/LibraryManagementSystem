import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from functools import partial
from tkinter import ttk

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table

b=[]
author=[]

s = "SELECT title FROM books"
cur.execute(s)

for x in cur:
    b.append(x)

s = "SELECT author FROM books"
cur.execute(s)

for x in cur:
    author.append(x)

def select(e):

    title = bookInfo1.get()

    s=""
    for i in title:
        if(i.isalnum())or (i.isspace()):
            s+=i
    title=s
    for i in range(len(b)):
        if(b[i][0]==title):
            break
    authors=[]
    authors.append(author[i])
    bookInfo2.config(value=authors)

    au=author[i]

    DeleteBtn = Button(root, text="Delete", bg='#d1ccc0', fg='black', command=partial(deleteBook,title))
    DeleteBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
    
def delete(root1):
    root1.destroy()
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root,title
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    # creating DropBox
    lb2 = Label(labelFrame, text="Book Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35)

    bookInfo1 = ttk.Combobox(root,value=b)
    #bookinfo1.current(0)
    bookInfo1.pack()
    bookInfo1.place(relx=0.3,rely=0.35, relwidth=0.30)

    #DropBox 2 :
    lb3 = Label(labelFrame, text="Book Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.5)

    bookInfo2 = ttk.Combobox(root, value=author)
    # bookinfo2.current(0)
    bookInfo2.pack()
    bookInfo2.place(relx=0.3, rely=0.5, relwidth=0.30)

    bookInfo1.bind("<<ComboboxSelected>>", select)

    
    #Delete Button
    '''DeleteBtn = Button(root,text="Delete",bg='#d1ccc0', fg='black',command=deleteBook)
    DeleteBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)'''
    
    root.mainloop()

    #Hafta Add Drop Down list : in delete :with a scroll bar.

def deleteBook(title):

    deleteSql = "delete from " + bookTable + " where title = '" + title + "'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please enter the correct title of the book")

    bookInfo1.delete(0, END)
    root.destroy()

#Suhas Align the Drop down box n all : make the screen look neater :

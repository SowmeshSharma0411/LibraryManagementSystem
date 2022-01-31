import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from functools import partial
from tkinter import ttk
import Manage_Window

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor()

# Enter Table Names here
bookTable = "books" #Book Table

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

    DeleteBtn = Button(root, text="Delete", bg='#f7f1e3', fg='black',font=('times new roman', 20), command=partial(deleteBook,title))
    DeleteBtn.place(relx=0.28, rely=0.83, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black',font=('times new roman', 20), command=partial(Manage_Window.ManageBooks,root))
    quitBtn.place(relx=0.53, rely=0.83, relwidth=0.18, relheight=0.08)

    root.mainloop()
    
def delete(root1):
    root1.destroy()
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root,title
    global b,author
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("1600x800")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

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

    # creating DropBox
    lb2 = Label(labelFrame, text="Book Title : ", bg='black', fg='white',font=('courier', 15))
    lb2.place(relx=0.07, rely=0.2)

    bookInfo1 = ttk.Combobox(labelFrame,value=b,font=('times new roman',18,'bold'),state='readonly')
    #bookinfo1.current(0)
    bookInfo1.pack()
    bookInfo1.place(relx=0.2, rely=0.21, relwidth=0.7, relheight=0.08)

    #DropBox 2 :
    lb3 = Label(labelFrame, text="Author", bg='black', fg='white',font=('courier', 15))
    lb3.place(relx=0.07, rely=0.4)

    bookInfo2 = ttk.Combobox(labelFrame, value=author,font=('times new roman',18,'bold'),state='readonly')
    # bookinfo2.current(0)
    bookInfo2.pack()
    bookInfo2.place(relx=0.2, rely=0.41, relwidth=0.7, relheight=0.08)

    bookInfo1.bind("<<ComboboxSelected>>", select)
    
    root.mainloop()

def deleteBook(title):
    deleteSql = "delete from " + bookTable + " where title = '" + title + "'"
    print(deleteSql)
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success', "Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please enter the correct title of the book")

    bookInfo1.delete(0, END)
#Some Problem here : colon isnt acccpeted as a valid symbol
#What if a person wants to delete a book from entry evnthough another person has borrowed it :

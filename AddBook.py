from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from functools import partial
import Manage_Window


def bookRegister():
    # bid = 1,2,3....
    title = bookInfo2.get()
    author = bookInfo3.get()
    #To check if a book already exists in the database :
    check="SELECT bid, title, author FROM books WHERE title = '%s' and author = '%s' " %(title,author)
    cur.execute(check)
    l=[]
    for i in cur:
        l.append(i)
    if(len(l)!=0):
        messagebox.showerror("Error!!", "Book Already Exists")
        return
    else:

        insertBooks = "insert into " + bookTable +" (title,author,copies) values('" + title + "','" + author + "',5)"
        try:
            cur.execute(insertBooks)
            con.commit()
            messagebox.showinfo('Success', "Book added successfully")
        except:
            messagebox.showinfo("Error", "Can't add data into Database")

def addBook(root1):
    root1.destroy()

    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase = "db"

    con = mysql.connector.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor(buffered=True)

    # Enter Table Names here
    bookTable = "books"
    Canvas1 = Canvas(root)

    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.7)

    # Title
    lb2 = Label(labelFrame, text="Title ", bg='black', fg='white',font=('courier', 23))
    lb2.place(relx=0.07, rely=0.2)

    bookInfo2 = Entry(labelFrame,font=('times new roman', 18, 'bold'))
    bookInfo2.place(relx=0.2, rely=0.21, relwidth=0.7, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author ", bg='black', fg='white',font=('courier', 23))
    lb3.place(relx=0.07, rely=0.34)

    bookInfo3 = Entry(labelFrame,font=('times new roman', 18, 'bold'))
    bookInfo3.place(relx=0.2, rely=0.35, relwidth=0.7, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="Submit", bg='#f7f1e3', fg='black',font=('times new roman',20), command=bookRegister)
    SubmitBtn.place(relx=0.3, rely=0.7, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', font=('times new roman',20),command=partial(Manage_Window.ManageBooks,root))
    quitBtn.place(relx=0.5, rely=0.7, relwidth=0.18, relheight=0.08)

    root.mainloop()

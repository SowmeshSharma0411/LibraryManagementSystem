from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = mysql.connector.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

# Enter Table Names here
bookTable = "borrowers"


def View():
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-30s%-60s%-40s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-10s" % ('SRN', 'FirstName', 'LastName', 'Mobile','Email','Bookid','BookTitle','Author','DateBorrowed','datedue','DateReturned','DaysBorrowed','Fine'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    getBooks = "select * from " + bookTable
    #try:
    cur.execute(getBooks)
    #con.commit()
    for i in cur:
        Label(labelFrame, text="%-30s%-60s%-40s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-50s%-10s" % (i[0],i[1], i[2], i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12]), bg='black',
              fg='white').place(relx=0.07, rely=y)
        y += 0.1
    '''except:
        messagebox.showinfo("Failed to fetch files from database")'''

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

    #Alignment of things :   Add Pagination/Scroll Bar + Search optn like suvan's view users

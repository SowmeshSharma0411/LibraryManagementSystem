from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector
from fines import *
import datetime

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor()

# Enter Table Names here
bookTable = "borrowers"
bookTable2="books"

global info,srn
info=[]

def returnn(l):

    srn=l[0]
    first=l[1]
    last=l[2]
    
    #global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,root,Canvas1,status

    extractBid = "select ID, FirstName, LastName, Mobile, Email, Bookid, BookTitle, Author, DateBorrowed, datedue from "+bookTable+" where SRN = '"+srn+"'"
    deleteSql = "delete from " + bookTable + " where SRN = '" + srn + "'"
    fetchbooks="SELECT copies from "+bookTable2+" where SRN = '" + srn + "'"
    cpy=0
    fine=0
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            info.append(i)
            #If i can ill return some of the book details back to the main func : so that it can be autofilled in those textBoxes
            cur.execute(fetchbooks)
            con.commit()
            for i in cur:
                cpy=int(i[0])
            cpy-=1
            addSql = "UPDATE " + bookTable2 + "/n" + "SET copies =",cpy,"where SRN = '" + srn + "'"
            cur.execute(addSql)
            con.commit()
            fine = fines(info[7], info[8])
            #Now ill have to show a window of the ReturnBook Summary
            returnBook()

            cur.execute(deleteSql)
            con.commit()

    except:
        messagebox.showinfo("Error", "SRN Entered isnt registered in the 'Borrowers List'")
    root.destroy()
    
def returnBook():
    
    global quitBtn,Canvas1,con,cur,root,labelFrame
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Summary", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    Label(labelFrame, text="%-30s%-60s%-40s%-10s" % ('SRN', 'FirstName', 'LastName', 'BID', 'Title', 'Author'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)

    Label(labelFrame, text="%-30s%-60s%-40s%-10s" % (srn,info[1], info[2], info[5],info[6],info[7]), bg='black',
            fg='white').place(relx=0.07, rely=0.3)

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()


#Im assuming issuebook takes in borrowed and calculates due date : and updates it in the borrowers table.
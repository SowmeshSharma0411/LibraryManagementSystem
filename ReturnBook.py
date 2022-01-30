from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox, ttk
import mysql.connector
from fines import *
import datetime

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor(buffered=True)

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

    extractBid = "SELECT SRN, FirstName, LastName, Bookid, BookTitle, Author, DateBorrowed, datedue FROM "+bookTable+" WHERE SRN = '"+str(srn)+"'"
    #Ive removed Mobile and email for now
    deleteSql = "DELETE FROM borrowers WHERE SRN = "+str(srn)
    cpy=0
    fine=0
    #try:
    cur.execute(extractBid)
    #con.commit()
    for i in cur:
        info.append(i)

    if(len(info)==0):
        messagebox.showwarning("ERROR!!","No Book Borrowed!")
        return

    fetchbooks = "SELECT copies FROM books WHERE title = '" + info[0][4] + "'"
    cur.execute(fetchbooks)

    for i in cur:
        cpy = int(i[0][0])
    cpy += 1
    addSql = "UPDATE books \nSET copies = '%s' \nWHERE title = '%s';" % (str(cpy), str(info[0][4]))
    cur.execute(addSql)
    con.commit()
    fine = fines(info[0][6], info[0][7])
    #Now ill have to show a window of the ReturnBook Summary

    cur.execute(deleteSql)
    con.commit()
    info[0]=list(info[0])
    info[0].append(fine)
    info[0]=tuple(info[0])

    returnBook()

    '''except:
        messagebox.showinfo("Error", "SRN Entered isnt registered in the 'Borrowers List'")'''
    return
    
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

    game_scroll = Scrollbar(labelFrame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(labelFrame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(labelFrame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack(fill=BOTH, expand=True)

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    my_game['columns'] = (
    'SRN', 'FirstName', 'LastName', 'Bookid', 'BookTitle', 'Author', 'Fine')

    my_game.column("#0", width=0, stretch=NO)
    my_game.column("SRN", anchor=CENTER, width=160)
    my_game.column("FirstName", anchor=CENTER, width=160)
    my_game.column("LastName", anchor=CENTER, width=80)
    my_game.column("Bookid", anchor=CENTER, width=80)
    my_game.column("BookTitle", anchor=CENTER, width=80)
    my_game.column("Author", anchor=CENTER, width=80)
    my_game.column("Fine", anchor=CENTER, width=80)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("SRN", text="SRN", anchor=CENTER)
    my_game.heading("FirstName", text="FirstName", anchor=CENTER)
    my_game.heading("LastName", text="LastName", anchor=CENTER)
    my_game.heading("Bookid", text="BookID", anchor=CENTER)
    my_game.heading("BookTitle", text="BookTitle", anchor=CENTER)
    my_game.heading("Author", text="Author", anchor=CENTER)
    my_game.heading("Fine", text="Fine", anchor=CENTER)
    for i in range(len(info[0])-2):
        my_game.insert(parent='', index='end', text='', values=info[0][i])
    my_game.insert(parent='', index='end', text='', values=info[0][-1])

    '''Label(labelFrame, text="%-30s%-60s%-40s%-50s%-50s%-50s%-50s" % (
    'SRN', 'FirstName', 'LastName', 'BID', 'Title', 'Author', 'Fine'), bg='black',
          fg='white').place(relx=0.07, rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------", bg='black',
          fg='white').place(relx=0.05, rely=0.2)
    Label(labelFrame, text="%-30s%-60s%-40s%-50s%-50s%-50s%-50s" % (
    info[0][0], info[0][1], info[0][2], info[0][3], info[0][4], info[0][5], info[1]), bg='black',
          fg='white').place(relx=0.07, rely=0.3)'''

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
#For Custom Error msg if user cant borrow : cuz he is not registered in the users database :
#Dont run in loop
from functools import partial
from tkinter import *
from tkinter import ttk
import tkinter.ttk
import main

import mysql.connector

import searchfunc

# Enter Table Names here
bookTable = "borrowers"


def View(root1,val):
    root1.destroy()

    global search
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
    cur = con.cursor(buffered=True)
    cur4 = con.cursor(buffered=True)

    if (val == 2):
        cur.execute("SELECT SRN,FirstName,LastName,Email,Bookid,BookTitle,Author,DateBorrowed,datedue FROM borrowers WHERE flag=1")
    if (val == 1):
        cur.execute("SELECT SRN,FirstName,LastName,Email,Bookid,BookTitle,Author,DateBorrowed,datedue FROM borrowers")

    ws = Tk()
    ws.title('PythonGuides')

    ws['bg'] = '#ff6e40'

    width = ws.winfo_screenwidth()
    height = ws.winfo_screenheight()
    # setting tkinter window size
    ws.geometry("%dx%d+0+0" % (1600, 800))

    headingFrame5 = Frame(ws, bg="#FFBB00", bd=5)
    headingFrame5.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel5 = Label(headingFrame5, text="View Borrowers", bg='black', fg='white',
                          font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel5.place(relx=0, rely=0, relwidth=1, relheight=1)

    game_frame = Frame(ws, height=800, width=800, bg="black")
    game_frame.place(relx=0.03, rely=0.3, relwidth=0.95, relheight=0.55)

    # scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(game_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack(fill=BOTH, expand=True)

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('SRN','FirstName','LastName','Email','Bookid','BookTitle','Author','DateBorrowed','datedue')

    # format our column
    my_game.column("#0", width=0, stretch=NO)
    my_game.column("SRN", anchor=CENTER, width=30)
    my_game.column("FirstName", anchor=CENTER, width=80)
    my_game.column("LastName", anchor=CENTER, width=80)
    my_game.column("Email", anchor=CENTER, width=120)
    my_game.column("Bookid", anchor=CENTER, width=20)
    my_game.column("BookTitle", anchor=CENTER, width=120)
    my_game.column("Author", anchor=CENTER, width=80)
    my_game.column("DateBorrowed", anchor=CENTER, width=80)
    my_game.column("datedue", anchor=CENTER, width=80)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("SRN", text="SRN", anchor=CENTER)
    my_game.heading("FirstName", text="FirstName", anchor=CENTER)
    my_game.heading("LastName", text="LastName", anchor=CENTER)
    my_game.heading("Email", text="Email", anchor=CENTER)
    my_game.heading("Bookid", text="BookID", anchor=CENTER)
    my_game.heading("BookTitle", text="BookTitle", anchor=CENTER)
    my_game.heading("Author", text="Author", anchor=CENTER)
    my_game.heading("DateBorrowed", text="DateBorrowed", anchor=CENTER)
    my_game.heading("datedue", text="datedue", anchor=CENTER)
    # button command=searchfunc

    global searchtype, searchentry

    lbl1 = Label(ws, text='Search Type', bg='#ff6e40', fg='black', font=('Times new roman', 15, 'bold'))
    lbl1.place(x=2, rely=0.19, relwidth=0.4, relheight=0.03)
    searchtype = tkinter.ttk.Combobox(ws, font=('times new roman', 18, 'bold'), width=13,
                                      state='readonly')  # adding drop down box
    searchtype['value'] = ('SRN','FirstName','LastName','BookTitle','Author','DateBorrowed','datedue')  # values in the drop down box
    searchtype.place(relx=0.06, rely=0.23, relwidth=0.18, relheight=0.05)

    def searching():
        searchfunc.search("borrowers", 4)
        con.commit()
        View(ws, 2)

    searchentry = Entry(ws, font=('times new roman', 18, 'bold'))
    searchentry.place(relx=0.25, rely=0.23, relwidth=0.55, relheight=0.05)
    searchbutton = Button(ws, text="Search", bg='#d1ccc0', fg='black', font=('times new roman', 20), command=searching)
    searchbutton.place(relx=0.82, rely=0.23, relwidth=0.14, relheight=0.05)
    quitbutton = Button(ws, text="Quit", bg='#d1ccc0', fg='black', font=('times new roman', 20),
                        command=partial(main.myfunc,ws))
    quitbutton.place(relx=0.36, rely=0.87, relwidth=0.18, relheight=0.05)

    m = 0
    for k in cur:
        my_game.insert(parent='', index='end', text='', values= k)
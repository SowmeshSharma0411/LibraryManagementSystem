from functools import partial
from tkinter import *
from tkinter import ttk
import tkinter.ttk
import Manage_Window

import mysql.connector

import searchfunc

# Enter Table Names here
bookTable = "books"


def View(root1,val):
    root1.destroy()

    global search
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
    cur = con.cursor(buffered=True)
    cur4 = con.cursor(buffered=True)

    # if search!=None and search!="":
    if (val == 2):
        cur.execute("SELECT bid,title,author FROM books WHERE flag=1")
    if (val == 1):
        cur.execute("SELECT bid,title,author FROM books")

    ws = Tk()
    ws.title('PythonGuides')

    ws['bg'] = '#ff6e40'

    width = ws.winfo_screenwidth()
    height = ws.winfo_screenheight()
    # setting tkinter window size
    ws.geometry("%dx%d+0+0" % (1600, 800))

    headingFrame5 = Frame(ws, bg="#FFBB00", bd=5)
    headingFrame5.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel5 = Label(headingFrame5, text="View Books", bg='black', fg='white',
                          font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel5.place(relx=0, rely=0, relwidth=1, relheight=1)

    game_frame = Frame(ws, height=800, width=800, bg="black")
    game_frame.place(relx=0.03, rely=0.3, relwidth=0.95, relheight=0.55)

    # scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    my_game = ttk.Treeview(game_frame, yscrollcommand=game_scroll.set)

    my_game.pack(fill=BOTH, expand=True)

    game_scroll.config(command=my_game.yview)

    # define our column

    my_game['columns'] = ('bid', 'title', 'author')

    # format our column
    my_game.column("#0", width=0, stretch=NO)
    my_game.column("bid", anchor=CENTER, width=160)
    my_game.column("title", anchor=CENTER, width=160)
    my_game.column("author", anchor=CENTER, width=160)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("bid", text="BID", anchor=CENTER)
    my_game.heading("title", text="Title", anchor=CENTER)
    my_game.heading("author", text="Author", anchor=CENTER)
    # button command=searchfunc

    global searchtype, searchentry

    lbl1 = Label(ws, text='Search Type', bg='#ff6e40', fg='black', font=('Times new roman', 15, 'bold'))
    lbl1.place(x=2, rely=0.19, relwidth=0.4, relheight=0.03)
    searchtype = tkinter.ttk.Combobox(ws, font=('times new roman', 18, 'bold'), width=13,
                                      state='readonly')  # adding drop down box
    searchtype['value'] = ('title','author')  # values in the drop down box
    searchtype.place(relx=0.06, rely=0.23, relwidth=0.18, relheight=0.05)

    def searching():
        searchfunc.search("books", 3)
        con.commit()
        View(ws, 2)

    searchentry = Entry(ws, font=('times new roman', 18, 'bold'))
    searchentry.place(relx=0.25, rely=0.23, relwidth=0.55, relheight=0.05)
    searchbutton = Button(ws, text="search", bg='#d1ccc0', fg='black', font=('times new roman', 20), command=searching)
    searchbutton.place(relx=0.82, rely=0.23, relwidth=0.14, relheight=0.05)
    quitbutton = Button(ws, text="Quit", bg='#d1ccc0', fg='black', font=('times new roman', 20),
                        command=partial(Manage_Window.ManageBooks, ws))
    quitbutton.place(relx=0.36, rely=0.87, relwidth=0.18, relheight=0.05)

    m = 0
    for k in cur:
        my_game.insert(parent='', index='end', text='', values= k)
#Enter column : msgbox if none selected :

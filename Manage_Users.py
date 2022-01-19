from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.ttk
import mysql.connector
search=None


def ManageUsers(root1):
    root1.destroy()

    global root
    root = Tk()
    root.title("Manage Users")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    Canvas2 = Canvas(root)

    Canvas2.config(bg="#ff6e40")
    Canvas2.pack(expand=True, fill=BOTH)

    headingFrame2 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame2.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel2 = Label(headingFrame2, text="Manage Users", bg='black', fg='white',
                          font=('times new roman', 30, 'bold'))
    headingLabel2.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame2 = Frame(root, bg='black')
    labelFrame2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Display Current Users  # Need to display from database  # must be done by Sowmesh and Suvan
    Display = Button(labelFrame2, text="Display Current Users", bg='black', fg='white', font=('courier', 15),command=viewusers)
    Display.place(relx=0, rely=0, relwidth=1, relheight=1 / 4)

    # Add Users
    Add = Button(labelFrame2, text="Add New User", bg='black', fg='white', font=('courier', 15), command=AddUserGUI)
    Add.place(relx=0, rely=1 / 4, relwidth=1, relheight=1 / 4)

    # Update Details  # need to be done by Sowmesh and Suvan
    '''Update = Button(labelFrame2, text='Update Details', bg='black', fg='white', font=('courier', 15))
    Update.place(relx=0, rely=2 / 4, relwidth=1, relheight=1 / 4)''' #No update

    # Delete Users # by Sowmesh and Suvan
    Delete = Button(labelFrame2, text='Delete User', bg='black', fg='white', font=('courier', 15))
    Delete.place(relx=0, rely=3 / 4, relwidth=1, relheight=1 / 4)
    
    quit = Button(labelFrame2, text='Delete User', bg='black', fg='white', font=('courier', 15),command=root.destroy)
    quit.place(relx=0, rely=4 / 4, relwidth=1, relheight=1 / 4)

    #root.mainloop()

def viewusers():
    
    global search
    def searchfunc():
        global search
        nonlocal cur,cur4
        #if searchentry.get()!="":
        search=searchentry.get()
        #code for flag
        try:
         cur.execute("ALTER TABLE users ADD COLUMN flag int")
        except:
              pas=1
              cur.execute("ALTER TABLE users DROP flag ")
              cur.execute("ALTER TABLE users ADD COLUMN flag int")
        cur.execute("SELECT * FROM users")
        for k in cur:
                 try:
                   if k[1]==int(search):
                        searchint=int(search)
                        cur4.execute("UPDATE users SET flag=1 WHERE srn=%s",(searchint,))
                 except:
                    print("int value conversion invalid")
                    #ErrorBox has to be displayed :

                 if k[2].upper()==search.upper():
                    cur4.execute("UPDATE users SET flag=1 WHERE name=%s",(search,))
        #print(search)
        con.commit()
        ws.destroy()
        viewusers()



    
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
    cur = con.cursor(buffered=True)
    cur4=con.cursor(buffered=True)
    
    if search!=None and search!="":
        try:

           cur.execute("SELECT SRN,name,Last_name,Branch,semester,mobile_no,email_id FROM users WHERE flag=1")
        except:
            cur.execute("SELECT SRN,name,Last_name,Branch,semester,mobile_no,email_id FROM users")
        

    else :
        cur.execute("SELECT SRN,name,Last_name,Branch,semester,mobile_no,email_id FROM users")


    ws  = Tk()
    ws.title('PythonGuides')
    
    ws['bg'] = '#ff6e40'
    #ws.pack(fill=BOTH,expand=True)

    width= ws.winfo_screenwidth() 
    height= ws.winfo_screenheight()
    #setting tkinter window size
    ws.geometry("%dx%d+0+0" % (1600, 800))

    headingFrame5 = Frame(ws, bg="#FFBB00", bd=5)
    headingFrame5.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel5 = Label(headingFrame5, text="View User", bg='black', fg='white',
                         font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel5.place(relx=0, rely=0, relwidth=1, relheight=1)


    game_frame = Frame(ws,height=800,width=800,bg="black")
    game_frame.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.40)
  
    #Canvas1.pack(expand=True, fill=BOTH)
    #game_frame.pack(fill=BOTH,expand=True)

    #scrollbar
    game_scroll = Scrollbar(game_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(game_frame,orient='horizontal')
    game_scroll.pack(side= BOTTOM,fill=X)

    my_game = ttk.Treeview(game_frame,yscrollcommand=game_scroll.set, xscrollcommand =game_scroll.set)


    my_game.pack(fill=BOTH,expand=True)

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    #define our column
     
    my_game['columns'] = ('sl_no', 'Srn', 'name', 'last_name', 'branch','Semester','phone_number','emailid')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("sl_no",anchor=CENTER, width=160)
    my_game.column("Srn",anchor=CENTER,width=160)
    my_game.column("name",anchor=CENTER,width=80)
    my_game.column("last_name",anchor=CENTER,width=80)
    my_game.column("branch",anchor=CENTER,width=80)
    my_game.column("Semester",anchor=CENTER, width=80)
    my_game.column("phone_number",anchor=CENTER, width=80)
    my_game.column("emailid",anchor=CENTER, width=80)

    #Create Headings 
    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("sl_no",text="Sl no",anchor=CENTER)
    my_game.heading("Srn",text="srn",anchor=CENTER)
    my_game.heading("name",text="name",anchor=CENTER)
    my_game.heading("last_name",text="last name",anchor=CENTER)
    my_game.heading("branch",text="branch",anchor=CENTER)
    my_game.heading("Semester",text="Semester",anchor=CENTER)
    my_game.heading("phone_number",text="Phone Number",anchor=CENTER)
    my_game.heading("emailid",text="Email ID",anchor=CENTER)
    #button command=searchfunc
    searchentry= Entry(ws, font=('times new roman', 15, 'bold'))
    searchentry.place(relx=0.15, rely=0.73, relwidth=0.7, relheight=0.03)
    searchbutton= Button(ws, text="search", bg='#d1ccc0', fg='black',font=('times new roman',20),command=searchfunc)
    searchbutton.place(relx=0.3, rely=0.84, relwidth=0.18, relheight=0.05)
    quitbutton= Button(ws, text="Quit", bg='#d1ccc0', fg='black',font=('times new roman',20),command=ws.destroy)
    quitbutton.place(relx=0.3, rely=0.92, relwidth=0.18, relheight=0.05)
    

    
    m=0
    for k in cur:
        m+=1
        my_game.insert(parent='',index='end',iid=m,text='',values=(m,)+k)
        
    
    try:
       cur.execute("ALTER TABLE users DROP flag")
    except:
        print("flag already dropped")
        #Eroor box has to be displayed :

    #print("exit loop tkinter")
    #print(b)



def adduser():
    srn=SRN.get()
    emailid=email.get()
    mobile_no2=mobile_no.get()
    a=info5.get()
    b=info5b.get()
    #print(a,b)
    c=comMemberc.get()
    d=comMemberd.get()
    #print(type(c),type(d))
    #print(c,d)
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
    cur = con.cursor()
    if emailid!=""  and mobile_no2.isdigit() and a!="" and b!="" and c!="" and d.isdigit():
     try:

       cur.execute("INSERT INTO users (srn,name,Last_name,Branch,semester,mobile_no,email_id) values(%s,%s,%s,%s,%s,%s,%s)",(srn,a,b,c,d,mobile_no2,emailid))
       con.commit()
       root.destroy()
     except:
        #print("invalid")
        messagebox.showinfo('Error', 'Values entered invalid, Please enter them again:')
        root.destroy()
        #print("pass")
        AddUserGUI()
    else:
        #print("invalid")
        messagebox.showinfo('Error', 'Values entered invalid, Please enter them again:')
        root.destroy()
        #print("pass")
        AddUserGUI()

    
    

    


def AddUserGUI():
    #print("enter")
    global info5,info5b,comMemberc,comMemberd,email,mobile_no,SRN,root
    
    '''root = Tk()
    root.title("Add User")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")
    print("enter 2")

    Canvas5 = Canvas(root)

    Canvas5.config(bg="#ff6e40")
    Canvas5.pack(expand=True, fill=BOTH)
    print("enter 3")

    headingFrame5 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame5.place(relx=0.2, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel5 = Label(headingFrame5, text="Add User", bg='black', fg='white',
                         font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel5.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame5 = Frame(root, bg='black')
    labelFrame5.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

    # labelFrame5b = Frame(root, bg='black')
    # labelFrame5b.place(relx=0.05, rely=0.25, relwidth=0.8, relheight=0.5)


    # Name
    lb5 = Label(labelFrame5, text="Name", bg='black', fg='white', font=('courier', 23))
    lb5.place(relx=0.04, rely=0.07)

    info5 = Entry(labelFrame5,font=('times new roman',15,'bold'))
    info5.place(relx=0.2, rely=0.07, relwidth=0.7,relheight=0.08)

    lb5b = Label(labelFrame5, text="Last name", bg='black', fg='white', font=('courier', 23))
    lb5b.place(relx=0.04, rely=0.2)

    info5b = Entry(labelFrame5, font=('times new roman', 15, 'bold'))
    info5b.place(relx=0.2, rely=0.21, relwidth=0.7, relheight=0.08)

    lb6b = Label(labelFrame5, text="SRN", bg='black', fg='white', font=('courier', 23))
    lb6b.place(relx=0.04, rely=0.34)

    SRN = Entry(labelFrame5, font=('times new roman', 15, 'bold'))
    SRN.place(relx=0.2, rely=0.35, relwidth=0.7, relheight=0.08)

    lb5c = Label(labelFrame5, text="Branch ", bg='black', fg='white', font=('courier', 23))
    lb5c.place(relx=0.04, rely=0.48)

    comMemberc = tkinter.ttk.Combobox(labelFrame5, font=('times new roman', 15, 'bold'), width=18,
                                     state='readonly')  # adding drop down box
    comMemberc['value'] = ('CSE', 'ECE', 'EEE','Mechanical Engineering','Biotechnology')  # values in the drop down box
    comMemberc.place(relx=0.2, rely=0.49,relwidth=0.7,relheight=0.08)

    lb5d = Label(labelFrame5, text="Semester ", bg='black', fg='white', font=('courier', 23))
    lb5d.place(relx=0.04, rely=0.62)

    comMemberd = tkinter.ttk.Combobox(labelFrame5, font=('times new roman', 15, 'bold'), width=18,
                                      state='readonly')  # adding drop down box
    comMemberd['value'] = (1,2,3,4,5,6,7,8)  # values in the drop down box
    comMemberd.place(relx=0.2, rely=0.63, relwidth=0.7, relheight=0.08)

    lb7 = Label(labelFrame5, text="mobile No", bg='black', fg='white', font=('courier', 23))
    lb7.place(relx=0.04, rely=0.75)

    mobile_no= Entry(labelFrame5, font=('times new roman', 15, 'bold'))
    mobile_no.place(relx=0.2, rely=0.76, relwidth=0.7, relheight=0.08)

    lb8 = Label(labelFrame5, text="email id", bg='black', fg='white', font=('courier', 23))
    lb8.place(relx=0.04, rely=0.87)

    email = Entry(labelFrame5, font=('times new roman', 15, 'bold'))
    email.place(relx=0.2, rely=0.88, relwidth=0.7, relheight=0.08)



    '''
    '''def Submit_5():
         #UserAdd()  # need to define UserAdd fn which is the fn to add the user into database... must be done by sowmesh and suvan
         messagebox.showinfo('Success','User Added Successfully') # need to add fn to show error as well


    #Submit Button
    Submit5 = Button(labelFrame5, text="Submit", bg='#d1ccc0', fg='black',font=('times new roman',20),command=adduser)
    Submit5.place(relx=0.3, rely=0.97, relwidth=0.18, relheight=0.08)'''
    root = Tk()
    root.title("Add User")
    root.minsize(width=400, height=400)
    root.geometry("1600x800")

    Canvas5 = Canvas(root)

    Canvas5.config(bg="#ff6e40")
    Canvas5.pack(expand=True, fill=BOTH)

    headingFrame5 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame5.place(relx=0.2, rely=0.05, relwidth=0.7, relheight=0.13)

    headingLabel5 = Label(headingFrame5, text="Add User", bg='black', fg='white',
                         font=('TIMES NEW ROMAN', 30, 'bold'))
    headingLabel5.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame5 = Frame(root, bg='black')
    labelFrame5.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

    # labelFrame5b = Frame(root, bg='black')
    # labelFrame5b.place(relx=0.05, rely=0.25, relwidth=0.8, relheight=0.5)


    # Name
    lb5 = Label(labelFrame5, text="First Name", bg='black', fg='white', font=('courier', 23))
    lb5.place(relx=0.04, rely=0.045)

    info5 = Entry(labelFrame5,font=('times new roman',18,'bold'))
    info5.place(relx=0.23, rely=0.045, relwidth=0.7,relheight=0.08)

    lb5b = Label(labelFrame5, text="Last Name", bg='black', fg='white', font=('courier', 23))
    lb5b.place(relx=0.04, rely=0.15)

    info5b = Entry(labelFrame5, font=('times new roman', 18, 'bold'))
    info5b.place(relx=0.23, rely=0.15, relwidth=0.7, relheight=0.08)

    lb6b = Label(labelFrame5, text="SRN", bg='black', fg='white', font=('courier', 23))
    lb6b.place(relx=0.04, rely=0.255)

    SRN = Entry(labelFrame5, font=('times new roman', 18, 'bold'))
    SRN.place(relx=0.23, rely=0.255, relwidth=0.7, relheight=0.08)

    lb5c = Label(labelFrame5, text="Branch ", bg='black', fg='white', font=('courier', 23))
    lb5c.place(relx=0.04, rely=0.36)

    comMemberc = tkinter.ttk.Combobox(labelFrame5, font=('times new roman', 18, 'bold'), width=18,
                                     state='readonly')  # adding drop down box
    comMemberc['value'] = ('CSE', 'ECE', 'EEE','Mechanical Engineering','Biotechnology')  # values in the drop down box
    comMemberc.place(relx=0.23, rely=0.36,relwidth=0.7,relheight=0.08)

    lb5d = Label(labelFrame5, text="Semester ", bg='black', fg='white', font=('courier', 23))
    lb5d.place(relx=0.04, rely=0.465)

    comMemberd = tkinter.ttk.Combobox(labelFrame5, font=('times new roman', 18, 'bold'), width=18,
                                      state='readonly')  # adding drop down box
    comMemberd['value'] = ( 1, 2, 3, 4, 5, 6, 7, 8)  # values in the drop down box
    comMemberd.place(relx=0.23, rely=0.465, relwidth=0.7, relheight=0.08)

    lb7 = Label(labelFrame5, text="Mobile No", bg='black', fg='white', font=('courier', 23))
    lb7.place(relx=0.04, rely=0.57)

    mobile_no= Entry(labelFrame5, font=('times new roman', 18, 'bold'))
    mobile_no.place(relx=0.23, rely=0.57, relwidth=0.7, relheight=0.08)

    lb8 = Label(labelFrame5, text="Email ID", bg='black', fg='white', font=('courier', 23))
    lb8.place(relx=0.04, rely=0.675)

    email = Entry(labelFrame5, font=('times new roman', 18, 'bold'))
    email.place(relx=0.23, rely=0.675, relwidth=0.7, relheight=0.08)

    Submit5 = Button(labelFrame5, text="Submit", bg='#d1ccc0', fg='black',font=('times new roman',20),command=adduser)
    Submit5.place(relx=0.4, rely=0.8, relwidth=0.18, relheight=0.13)
    #print("leaving")




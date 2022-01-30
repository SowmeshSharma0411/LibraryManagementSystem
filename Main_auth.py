from functools import partial
from tkinter import *
from PIL import ImageTk,Image
from Auth import *
from tkinter import messagebox

# declare the window
root = Tk()
root.title("Login Page")
root.minsize(width=400, height=400)
root.geometry("1600x800")

Canvas1 = Canvas(root)

Canvas1.config(bg="#ff6e40")
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.17,rely=0.1,relwidth=0.7,relheight=0.16)

headingLabel = Label(headingFrame1, text="WELCOME TO MY LIBRARY", bg='black', fg='white', font=('TIMES NEW ROMAN',40,'bold'))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn0 = Button(root, text="Login", bg='black', fg='white',font=('baskerville old face',25,'bold'),borderwidth=3,relief=RAISED, command=partial(gui_auth,root))
btn0.place(relx=0.20, rely=0.5, relwidth=0.20, relheight=0.1)

btn1 = Button(root, text="Quit", bg='black', fg='white',font=('baskerville old face',25,'bold'),borderwidth=3,relief=RAISED, command=root.destroy)
btn1.place(relx=0.60, rely=0.5, relwidth=0.20, relheight=0.1)

root.mainloop()

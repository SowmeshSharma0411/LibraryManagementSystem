#Fine System written down in the PESU Elec assignment book :
#date=(yr,month,day,hr,min)
#As the person borrows the book : Suvan send me the borrow details as a tuple 'date' : As he borrows also display a msg box : Details of borrow :
#As the person returns a book another date is returned :

from tkinter import *
from tkinter import messagebox
import datetime

def fines(Bor,Ret):
    dateB=datetime.datetime(Bor)
    dateR=datetime.datetime(Ret)

    days=dateR.date()-dateB.date()

    fine=0
    Lost=0
    if(days>14):
        fine+=1*days
        if(days>24):
            fine+=10*(days-10)
            if(days>39):
                Lost=1

    if(Lost==1):
        fine+=2000 #2k Extra Fine : Fr the book + inconvenience caused :
        #If this fine is not paid within the next 15 days : Library Membership Revoked : The student is Excommunicado : A bounty of 10000INR on his head :

    #For now no lost books
    '''if(days>54):
        #Membership Revoked : Remove User from Users table :
        #Hafta Add GUI Pop up box :
        messagebox.showwarning("Goodbye!!","Library User Membership Revoked/nYou are Excommunicado")'''

    return fine
#The fine will still be present : Maybe if the person doesnt pay it : he will not get the Hall Ticket fr Exams :



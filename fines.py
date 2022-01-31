#14days = borrow period
#10 days post borrow : 1rs/day = fine
#Next 15 days : 1rs/day + 10rs/day + fine(compounded)
#If days b/w borrow and returned >39 : Fine+=2000 (book=lost : we will implement this later)


from tkinter import *
from tkinter import messagebox
import datetime

def fines(Bor,Ret):
    l1=Bor.split('-')
    dateB=datetime.date(int(l1[0]),int(l1[1]),int(l1[2]))
    dateR=datetime.date.today()

    days=dateR-dateB
    days=str(days)
    if(days=="0:00:00"):
        return 0
    days=str(days[0:days.index(" ")])
    days=int(days)

    fine=0
    Lost=0
    if(days>14):
        fine+=1*(days-14)
        if(days>24):
            fine+=10*(days-14-10)
            if(days>39):
                Lost=1

    if(Lost==1):
        fine+=2000 #2k Extra Fine : Fr the book + inconvenience caused :
        #If this fine is not paid within the next 15 days : Library Membership Revoked :
    print(fine)
    #For now no lost books

    return fine

#The fine will still be present : Maybe if the person doesnt pay it : he will not get the Hall Ticket fr Exams : LATER IF TIME :



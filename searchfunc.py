#Hafta DryRun this :
import mysql.connector
import main
def search(column,table):

    searchquery=main.search_var.get()
    print("hello")

    '''con=mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
    cur=con.cursor(buffered=True)
    curm=con.cursor(buffered=True)
    try:
        cur.execute("SELECT * FROM "+table)
    except:
        print("searchfunc: table does not exist. table names are case sensitive")
        return 1
    try:
       cur.execute("ALTER TABLE "+table+" ADD COLUMN flag int")
    except:
        cur.execute("ALTER TABLE "+table+" DROP COLUMN flag")
        print("searchfunc: table column flag already exists")
        cur.execute("ALTER TABLE "+table+" ADD COLUMN flag int")

    try:
       cur.execute("SELECT "+column+" from "+table)
    except:
        print("searchfunc: column in the table does not exist. column names are case sensitive")
        return 2
    
    try:
     if type(searchquery)==str:
        searchquery=searchquery.split()
        for k in cur:
            if type(k[0])!=str and k[0]!=None:
                print("searchfunc: searchquery data type and column data type are not the same")
                return
            try:
               s=k[0].split()
            except:
                print("None data type")
            for m in s:
                for l in searchquery:
                    if l.upper()==m.upper():
                      curm.execute("UPDATE "+table+" SET flag=1 WHERE "+column+" =%s",(k[0],))                                                                    
     if type(searchquery)==int:
        for k in cur:
            s=k[0]
            print(type(s))
            if type(s)!=int and s!=None:
                print("searchfunc: searchquery data type and column data type are not the same")
                return 5 #searchquery data type and column data type not the same
            if searchquery==s:
                curm.execute("UPDATE "+table+" SET flag=1 WHERE "+column+" =%s",(s,))

    except:
        print("searchfunc: searchquery data type and column data type are not the same 2")
        return 5 #searchquery data type and column data type not the same
    con.commit()'''

#I am A lil doubtful about this fnc :



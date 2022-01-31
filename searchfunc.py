import mysql.connector
import main
import Manage_Users
import ViewBooks
import ViewBorrowers
def search(table,val):
    global searchquery
    if(val==1):
        searchquery = main.search_var.get()
        column="title"
    if(val==2):
        column=Manage_Users.searchtype.get()
        searchquery=Manage_Users.searchentry.get()
        if(column=="SRN")or(column=="semester"):
            '''if(searchquery==""):
                return'''
            searchquery=int(searchquery)
    if(val==3):
        column=ViewBooks.searchtype.get()
        searchquery=ViewBooks.searchentry.get()
        '''if (searchquery == ""):
            return'''
    if(val==4):
        column=ViewBorrowers.searchtype.get()
        searchquery = ViewBorrowers.searchentry.get()


    con=mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
    cur=con.cursor(buffered=True)
    cur_update=con.cursor(buffered=True)
    cur_ColumnCheck=con.cursor(buffered=True)

    try:
        cur.execute("SELECT * FROM "+table)
    except:
        print("searchfunc: table does not exist. table names are case sensitive")
        return
    cur.execute("Update "+table+" SET flag=0")
    con.commit()

    if (searchquery == ""):
        return

    try:
        cur.execute("SELECT "+column+" from "+table)
    except:
        print("searchfunc: column in the table does not exist. column names are case sensitive")
        return
    try:
        if type(searchquery)==str:
           
           cur_ColumnCheck.execute("SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name =%s AND COLUMN_NAME =%s",(table,column))
           for k in cur_ColumnCheck:
               if k[0]!="varchar":
                  print("searchfunc: searchquery data type and column data type are not the same")
                  return
                  # checking if column data type is str. if column data type is not str, program wll exit the function.

           searchquery=searchquery.split()
           for k in cur:
              try:
                  s=k[0].split()            
              except:
                  print("searchfunc: None data type found. skipping this iteration") 
                  continue
                  # None.split() causes error therefore, handling error by skipping iteration. this may not even happen but just in case if it happens, The program will handle it and not crash instead 

              for m in s:
                 for l in searchquery:
                    if (m.upper()).startswith(l.upper()):
                       cur_update.execute("UPDATE "+table+" SET flag=1 WHERE "+column+" =%s",(k[0],))
                       con.commit()

        elif type(searchquery)==int:

           cur_ColumnCheck.execute("SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = %s AND COLUMN_NAME = %s",(table,column))
           for k in cur_ColumnCheck:
               if k[0]!="int":
                  print("searchfunc: searchquery data type and column data type are not the same")
                  return
                  # checking if column data type is int. if column data type is not int, program wll exit the function.

           for k in cur:
               s=k[0]
               if searchquery==s:
                   cur_update.execute("UPDATE "+table+" SET flag=1 WHERE "+column+" =%s",(s,))
                   con.commit()

        else:
              print("searchfunc: search query data type not int or string. only str and int supported")
              return
    except:
           print("searchfunc: error when performing search")
           return

#if no book records exists :



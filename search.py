import mysql.connector

con=mysql.connector.connect(host="localhost", user="root", password="root", database="db", port=3306)
cur=con.cursor(buffered=True)
curm=con.cursor(buffered=True)
searchm=input("Enter the book/author name you want to search for :\n")
cur.execute("ALTER TABLE BookTable ADD COLUMN flag2315 int")
cur.execute("SELECT book_name from BookTable")
search3=searchm.split()
cur.execute("SELECT book_name from BookTable")
for x in cur:
 s=x[0]
 a=s.split()
 for k in a:
    for m in search3:
        if m==k:
        
          curm.execute("UPDATE BookTable SET flag2315=1 WHERE book_name=%s",(s,))

cur.execute("SELECT author_name from BookTable")
for x in cur:
 s=x[0]
 a=s.split()
 for k in a:
    for m in search3:
        if m==k:
        
          curm.execute("UPDATE BookTable SET flag2315=1 WHERE author_name=%s",(s,))

cur.execute("SELECT * from BookTable where flag2315=1")
for x in cur:
    print(x)
cur.execute("ALTER TABLE BookTable drop flag2315")
print('--------\"end of list\"--------')
x=input()

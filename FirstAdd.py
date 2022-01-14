# Reading Books and authors into b and author From a file : BOOKS & AUTHORS.txt

import mysql.connector

mypass = "root"
mydatabase="db"

con = mysql.connector.connect(host="localhost",user="root",password="root",database="db")
cur = con.cursor()

bookTable="books"
def ret():
    f = open("BOOKS & AUTHORS.txt", "r")
    z = []
    b = []
    for i in f:
        z = f.readlines()

    s1 = ""
    s2 = ""
    author = []
    for i in z:
        s1 = i[3:(i.index('-'))]
        s2 = i[(i.index('>') + 1):(len(i))]
        b.append(s1)
        author.append(s2)

    print(b)
    print(author)

    for i in range(len(b)):
        insertBooks = "insert into " + bookTable + " (title,author,copies) values('" + b[i] + "','" + author[i] + "',5)"
        cur.execute(insertBooks)
        con.commit()
#ret()
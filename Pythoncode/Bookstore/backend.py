import sqlite3

def connect():
    con = sqlite3.connect("books.db")
    cur =con.cursor()
    cur.execute("Create Table if not exists book(id INTEGER PRIMARY KEY,title text,authur text,year integer,isbn integer)")
    con.commit()
    con.close()

def insert(title,authur,year,isbn):
    con = sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("INSERT INTO book  (title, authur, year, isbn) VALUES (?,?,?,?)",(title,authur,year,isbn))
              #(INSERT INTO book2 (title, authur, year, isbn) VALUES (?,?,?,?)",(title,authur,year,isbn))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("select * from book")
    rows=cur.fetchall()
    con.close()
    return rows

def search(title="",authur="",year="",isbn=""):
    con = sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("select * from book where title = ? or authur = ? or year = ? or isbn = ?",(title,authur,year,isbn))
    rows=cur.fetchall()
    con.close()  
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()


def update(id,title,authur,year,isbn):
    con = sqlite3.connect("books.db")
    cur=con.cursor()
    cur.execute("update book set title = ? , authur = ? , year = ? , isbn = ? where id = ?",(title,authur,year,isbn,id))
    con.commit()
    con.close()

connect()
#delete(98700054321)
#insert("Daily Trust","Musa Adbul",2019,98700054321)
#print(view(),"\n")
#print("\n\n Search Output\n",search(title="Daily Trust"))
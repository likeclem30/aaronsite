import sqlite3
class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur =self.con.cursor()
        self.cur.execute("Create Table if not exists book(id INTEGER PRIMARY KEY,title text,authur text,year integer,isbn integer)")
        self.con.commit()

    def insert(self,title,authur,year,isbn):
        self.cur.execute("INSERT INTO book  (title, authur, year, isbn) VALUES (?,?,?,?)",(title,authur,year,isbn))
                #(INSERT INTO book2 (title, authur, year, isbn) VALUES (?,?,?,?)",(title,authur,year,isbn))
        self.con.commit()

    def view(self):
        self.cur.execute("select * from book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",authur="",year="",isbn=""):
        self.cur.execute("select * from book where title = ? or authur = ? or year = ? or isbn = ?",(title,authur,year,isbn))
        rows=self.cur.fetchall()  
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        self.con.commit()
        
    def update(self,id,title,authur,year,isbn):
        self.cur.execute("update book set title = ? , authur = ? , year = ? , isbn = ? where id = ?",(title,authur,year,isbn,id))
        self.con.commit()
    
    def __del_(self):
        self.con.close()
    #connect()
    #delete(98700054321)
    #insert("Daily Trust","Musa Adbul",2019,98700054321)
    #print(view(),"\n")
    #print("\n\n Search Output\n",search(title="Daily Trust"))
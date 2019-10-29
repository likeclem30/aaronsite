import sqlite3

def create_table():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute('CREATE TABLE if not exist store(item text,quantity integer,price real)')
    con.commit()
    con.close()

def insert(item,qty,price):
    con = sqlite3.connect("lite")
    cur = con.cursor()
    cur.execute("Insert into store values(?,?,?)",(item,qty,price))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("lite")
    cur = con.cursor()
    cur.execute("Select * from store")
    rows=cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = sqlite3.connect("lite")
    cur = con.cursor()
    cur.execute("delete from store where item = ?",(item,))
    con.commit()
    con.close()
    
def update(qty,price,item):
    con = sqlite3.connect("lite")
    cur = con.cursor()
    cur.execute("update store set quantity = ?, price = ? where item = ?",(qty,price,item))
    con.commit()
    con.close()
    
update(30000,56600,'Gova Cup')

print(view())
delete('Ginger Cup')
print('\n\n after delete rows')
print(view())
import psycopg2

def create_table():
    con = psycopg2.connect("dbname = 'postgres' user='postgres'  password = 'postgres123' host= 'localhost' port='5432'")
    cur = con.cursor()
    cur.execute('CREATE TABLE if not exists store(item text,quantity integer,price real)')
    con.commit()
    con.close()

def insert(item,qty,price):
    con = psycopg2.connect("dbname = 'postgres' user='postgres'  password = 'postgres123' host= 'localhost' port='5432'")
    cur = con.cursor()
    cur.execute("Insert into store values(%s,%s,%s)",(item,qty,price))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect("dbname = 'postgres' user='postgres'  password = 'postgres123' host= 'localhost' port='5432'")
    cur = con.cursor()
    cur.execute("Select * from store")
    rows=cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = psycopg2.connect("dbname = 'postgres' user='postgres'  password = 'postgres123' host= 'localhost' port='5432'")
    cur = con.cursor()
    cur.execute("delete from store where item = %s",(item,))
    con.commit()
    con.close()
    
def update(qty,price,item):
    con = psycopg2.connect("dbname = 'postgres' user='postgres'  password = 'postgres123' host= 'localhost' port='5432'")
    cur = con.cursor()
    cur.execute("update store set quantity = %s, price = %s where item = %s",(qty,price,item))
    con.commit()
    con.close()
    
update(30000,56600,'Galic')

print(view())
delete('Oracnge')
print('\n\n after delete rows')
print(view())
create_table()
insert('Orange',890,321)
print(view())
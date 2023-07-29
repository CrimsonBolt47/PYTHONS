import psycopg2


def create_table():

    con=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)") #sql code

    con.commit()
    con.close()

def update(quantity,price,item):
    con=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=con.cursor()

    cur.execute("UPDATE store SET quantity=%s,price=%s WHERE item=%s",(quantity,price,item))

    con.commit()
    con.close()

def insert(item,quantity,price):
    con=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=con.cursor()

    cur.execute("INSERT INTO store VALUES (%s,%s,%s)" , (item,quantity,price))


    con.commit()
    con.close()

def view():
    con=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=con.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    con.close()
    return rows

def delete(item):
    con=psycopg2.connect("dbname='database1' user='postgres' password='postgres' host='localhost' port='5432'")
    cur=con.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    con.commit()
    con.close()

create_table()
#insert("orange",5,19)
#delete("orange")
update(20,15,"apple")

print(view())
#update(11,6,"WIne Glass")
#delete("coffee")

#print(view())
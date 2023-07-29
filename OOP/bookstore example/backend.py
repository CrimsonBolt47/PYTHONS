import sqlite3


class Database:  #class based on OOP


    def __init__(self,db):  #constructor
        global cur
        global conn
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()


    def insert(self,title,author,year,isbn):
        cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
    

    def view(self):
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        return rows

    def delete(self,id):
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()

    def update(self,id,title,author,year,isbn):
        cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        conn.commit()

    def __del__(self):  #destructor
        conn.close()



#insert("cool book","peter",1921,97557)
#delete(2)
#update(3,"moon","jack",1456,985739)
#print(view())
#print(search(author="peter"))
    
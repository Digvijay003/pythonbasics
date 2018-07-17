""" a simple example of database"""
import sqlite3
import time
import random
import matplotlib.pyplot as plt

conn = sqlite3.connect('mytut.db')

c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS MyyyyTable(keyword TEXT, Value INT, unix REAL)')
	
def data_entry():
    c.execute("INSERT INTO MyyyyTable VALUES('python', 1, 125698749)")
    
create_table()
data_entry()

def dynamic_data():
    unix = time.time()
    keyword ="python again"
    value = random.randrange(1,10)
    c.execute('INSERT INTO MyyyyTable (unix,keyword,value) VALUES(?,?,?)',(unix,keyword,value))# ? is used in sqlite whereas %s is used in mysql 

for i in range(1,10):
    dynamic_data()


def read_db():
    c.execute("SELECT * FROM MyyyTable WHERE Value=1")
    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute("SELECT Value FROM MyyyTable")
    Value = []
    for row in c.fetchall():
        print(row[0])
    plt.plot(Value,'-')
    plt.show()

def del_and_update():
    c.execute("SELECT * FROM MyyyTable")
    for row in c.fetchall():
              print(row)

    c.execute("UPDATE MyyyTable SET Value = 99 WHERE Value=1")
    conn.commit()
    for row in c.fetchall():
        print(row)

    c.execute("DELETE FROM MyyyTable WHERE Value=99")#if u delete then it is permananet in sqlite it cant be undo 
    conn.commit()
    for row in c.fetchall():
        print(row)
        
    

graph_data()
read_db()
del_and_update()
conn.commit()
c.close()




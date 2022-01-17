import sqlite3
 
def creaConn():
    con = sqlite3.connect('data.sqlite')
    return con

def creaCursor(con):
    cur = con.cursor()
    return cur

def executeSQL(sql, cur):
    cur.execute(sql)
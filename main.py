from database import *

con = creaConn()
cur = creaCursor(con)

#executeSQL("INSERT INTO flyState VALUES(1, 'Boarding')", cur)


for row in cur.execute('SELECT * from Company'):
    print(row)

con.commit()
cur.close()
con.close()

'''
IDDatiVolo
Data Partenza
Ora Partenza
Partenza
Destinazione
Numero Volo
Aereo
Stato
AreaCheckIn
AreaGate
Gate
Note
Compagnia
'''


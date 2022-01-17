from database import *

con = creaConn()
cur = creaCursor(con)

executeSQL("INSERT INTO AirplanesData VALUES(1, 'AIRBUS', 'A320neo', 'I-MLBC', 1)", cur)
executeSQL("INSERT INTO AirplanesData VALUES(2, 'AIRBUS', 'A320neo', 'I-MB01', 2)", cur)

print("Dati Aerei -----------")
for row in cur.execute('SELECT * from AirplanesData'):
    print(row)

print("Aeroporti -----------")
for row in cur.execute('SELECT * from Airports'):
    print(row)

print("Compagnie -----------")
for row in cur.execute('SELECT * from Company'):
    print(row)

print("Voli -----------")
for row in cur.execute('SELECT * from FlyDates'):
    print(row)

print("Stati -----------")
for row in cur.execute('SELECT * from FlyState'):
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


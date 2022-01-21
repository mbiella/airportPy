from database import *

con = creaConn()
cur = creaCursor(con)

#executeSQL("INSERT INTO FlyDates VALUES(1, '20220120', '1255', 1, 3, 2, 'AA238', 2, 7, 'B', 'B', 12, 'Nessuna')", cur)

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


print("VOLO -----------")
#SELECT * FROM FlyDates as F join Airports as AS ON 


con.commit()
cur.close()
con.close()

'''
IDFlyData, 
flyDate, 
flyTime, 
flyDepartureID, 
flyDestinationID, 
flyIDCompany, 
flyNumber, 
flyAirplaneID, 
flyStateID, 
flyCheckInArea, 
flyGateArea, 
flyGate, 
FlyNote
'''


from database import *

con = creaConn()
cur = creaCursor(con)

#executeSQL("INSERT INTO FlyDates VALUES(1, '20220120', '1255', 1, 3, 2, 'AA238', 2, 7, 'B', 'B', 12, 'Nessuna')", cur)

def printInfo():
    print('****************** AIRPORT v. 1.0 ******************')
    '''print("Dati Aerei -----------")
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
        print(row)'''

    print("Stati -----------")
    for row in cur.execute('SELECT * from FlyState'):
        print(row)
    print('****************** AIRPORT v. 1.0 ******************')
    PRINT()
    print("VOLO -----------")
    for row in cur.execute('select F.flyDate as Date, F.flyTime as Time, A.airportName as Departure,A2.airportName as Destination, F.flyNumber as Fly_Number, P.airplaneModel,FS.flyState,flyCheckInArea,flyGateArea,flyGate, C.companyName from FlyDates as F join Airports as A on F.flyDepartureID = A.IDAirport join Airports as A2 on F.flyDestinationID = A2.IDAirport join AirplanesData as P on F.flyAirplaneID = P.IDAirplane join FlyState FS on F.flyStateID = IDFlyState join Company as C on P.IDCompany = C.IDCompany'):
        print(row)
 
printInfo()

while(1):
    res=input("Vuoi cambiare lo stato (y/n)?: ")
    if(res=='y'):
        fly=input("Numero del volo?: ")
        st=input("Nuovo stato (1-9)?")
        cur.execute("UPDATE flyDates set flyStateID=" + st + " WHERE flyNumber='" + fly + "'")
        con.commit()
        printInfo()
    else:
        print("Program is shutting down...")
        exit()


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


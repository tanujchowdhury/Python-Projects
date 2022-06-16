#databases challenge
import sqlite3
tableValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100),('Ak\'not', 'Mangalore', -5))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", tableValues)

    c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?", ('Human', 'Korben Dallas', 100))
    

    c.execute("SELECT Name, IQ FROM Roster WHERE Species == 'Human'")
    for row in c.fetchall():
        print(row)

#range challenge
for i in range(4):
    print(i)

for i in range(3, -1, -1):
    print(i)

for i in range(8, 0 , -2):
    print(i)

#datetime challenge
import datetime

timeNow = datetime.datetime.now()
portlandTime = timeNow
nycTime = 
londonTime = 

print(timeNow)
print(portlandTime)


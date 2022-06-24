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


now = datetime.datetime.now()
today9am = now.replace(hour=9, minute=0, second=0, microsecond=0)
today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)


if now >= today9am and now <= today5pm:
    print("Portland store is open")
else:
    print("Portland store is closed")

nyc9am = now.replace(hour=6, minute=0, second=0, microsecond=0)
nyc5pm = now.replace(hour=14, minute=0, second=0, microsecond=0)

if now >= nyc9am and now <= nyc5pm:
    print("NYC store is open")
else:
    print("NYC store is closed")

london9am = now.replace(hour=1, minute=0, second=0, microsecond=0)
london5pm = now.replace(hour=9, minute=0, second=0, microsecond=0)

if now >= london9am and now <= london5pm:
    print("London store is open")
else:
    print("London store is closed")


#gui challenge
from tkinter import *

win = Tk()

win.title("Check files")

b1 = Button(win, text="Browse...")
b1.grid(row=0, column=0, padx=(20,20), pady=(50,0), ipadx=27)

b2 = Button(win, text="Browse...")
b2.grid(row=1, column=0, padx=(20,20), pady=(10,0), ipadx=27)

b3 = Button(win, text="Check for files...")
b3.grid(row=2, column=0, padx=(20,20), pady=(10,20), ipady=10)

b4 = Button(win, text="Close Program")
b4.grid(row=2, column=2, padx=(20,20), pady=(10,20), sticky=SE, ipady=10)

e1 = Entry(win)
e1.grid(row=0, column=1, padx=(20,20), pady=(50,0), columnspan=2, sticky=N, ipadx=150)

e2 = Entry(win)
e2.grid(row=1, column=1, padx=(20,20), pady=(10,0), columnspan=2, sticky=N, ipadx=150)

#widget challenge
from tkinter import *
import tkinter.filedialog

win = Tk()
fd = tkinter.filedialog

def open():
    name = fd.askdirectory()
    print(name)
    e1.config(text="{}".format(name))

def cancel():
    win.destroy()

win.title("Check files")

b1 = Button(win, text="Browse...")
b1.grid(row=0, column=0, padx=(20,20), pady=(50,0), ipadx=27)

b2 = Button(win, text="Browse...")
b2.grid(row=1, column=0, padx=(20,20), pady=(10,0), ipadx=27)

b3 = Button(win, text="Check for files...", command=open)
b3.grid(row=2, column=0, padx=(20,20), pady=(10,20), ipady=10)

b4 = Button(win, text="Close Program", command=cancel)
b4.grid(row=2, column=2, padx=(20,20), pady=(10,20), sticky=SE, ipady=10)

e1 = Label(win)
e1.grid(row=0, column=1, padx=(20,20), pady=(50,0), columnspan=2, sticky=N, ipadx=150)

e2 = Entry(win)
e2.grid(row=1, column=1, padx=(20,20), pady=(10,0), columnspan=2, sticky=N, ipadx=150)


from tkinter import *
import tkinter.filedialog
import shutil
import os
import datetime

win = Tk()

win.title("File Transfer")


def choose_source():
    #Opens up the file directory for the user to choose a folder
    name = tkinter.filedialog.askdirectory()
    #The selected folder's file path is put into a label
    l1.config(text="{}".format(name))

def choose_destination():
    name = tkinter.filedialog.askdirectory()
    #The selected folder's file path is put into another label
    l2.config(text="{}".format(name))

#This method moves all files modified less than 1 day ago from the source folder to the destination folder
def transfer():
    #Gets the file path from the first label
    source = l1.cget("text")+"/"
    #Gets the file path from the second label
    destination = l2.cget("text")
    files = os.listdir(source)
    for i in files:
        now = datetime.datetime.now()
        m_time = datetime.datetime.fromtimestamp(os.path.getmtime(source+i))
        diff = now - m_time
        days = diff.days
        #Moves files from the source to the destination, if they were modified less than 1 day ago
        if days < 1:
            shutil.move(source+i, destination)

def cancel():
    win.destroy()

b1 = Button(win, text="Choose source", command=choose_source)
b1.grid(row=0, column=0, padx=(20,20), pady=(50,0), ipadx=19)

b2 = Button(win, text="Choose destination", command=choose_destination)
b2.grid(row=1, column=0, padx=(20,20), pady=(10,0), ipadx=0)

b3 = Button(win, text="Transfer files...", command=transfer) 
b3.grid(row=2, column=0, padx=(20,20), pady=(10,20), ipadx=21, ipady=10)

b4 = Button(win, text="Close Program", command=cancel)
b4.grid(row=2, column=2, padx=(20,20), pady=(10,20), sticky=SE, ipady=10)

l1 = Label(win, bg="white")
l1.grid(row=0, column=1, padx=(20,20), pady=(50,0), columnspan=2, sticky=N, ipadx=100)

l2 = Label(win, bg="white")
l2.grid(row=1, column=1, padx=(20,20), pady=(10,0), columnspan=2, sticky=N, ipadx=100)

win.mainloop()
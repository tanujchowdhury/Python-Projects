import sqlite3

#Establishing the connection
conn = sqlite3.connect('test_database.db')

with conn:
    
    #Creating a cursor object
    cur = conn.cursor()

    #Creating a table
    cur.execute(" CREATE TABLE IF NOT EXISTS files ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                Name VARCHAR(50) \
                )")
    conn.commit()
conn.close()


fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#Puts all the .txt files in a list
files_txt = []
for i in fileList:
    if i.endswith('.txt'):
        files_txt.append(i)


conn = sqlite3.connect('test_database.db')

with conn:
    
   
    cur = conn.cursor()
    
    #Prepare an SQL query to INSERT
    cur.execute("INSERT INTO files(Name) VALUES (?)", \
                (files_txt[0],))
    cur.execute("INSERT INTO files(Name) VALUES (?)", \
                (files_txt[1],))
    conn.commit()
conn.close()

#Print file names to console
print("File 1: {}\nFile 2: {}".format(files_txt[0], files_txt[1]))

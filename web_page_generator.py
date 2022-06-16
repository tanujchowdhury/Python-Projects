# Tkinter module for the gui
from tkinter import *

# Webbrowser to open the webpage
import webbrowser

# Opens a tkinter window
win = Tk()

# To store user input as a string
inputText = StringVar()

# A method to create a webpage with the user's input as the content
def create():

    # Creates a new html file
    f = open("index.html", "w")
    
    # Get the user's input from the entry field
    varText = entry.get()

    # The html file with the heading as the user's input
    f.write("<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>".format(varText))
    f.close()

    # Displays the html file content in the console (just to check easily)
    f = open("index.html", "r")
    print(f.read())

    # Opens the generated html file in a new tab
    webbrowser.open("index.html", new=0, autoraise=True)

# Label text
label = Label(text="Enter text here: ")
label.pack()

# Entry field for the user to type in
entry = Entry(text=inputText)
entry.pack()

# Button to call create()
button = Button(text="Create webpage", command=create)
button.pack()
from tkinter import filedialog
from tkinter import *

while True:
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "C:/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))

    with open(root.filename) as document:
        try:
            lines = document.read()
            line = lines.split()
            break
        except:
            print("Please select a text file")
            continue
print('The number of words in the document is:',len(line))

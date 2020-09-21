from tkinter import *
from tkinter.filedialog import *

filename = None


#The first step is to define the four main functions of a notepad, save, save as, new file and openfile.

def newfile():

    global filename #Gets the new filename variable, instead of defining this variable inside each function, we're just gonna use a global variable.
    filename = "Untitled"
    text.delete(0.0, END) #The 0.0 stands for row 0, column 0, which is the very first line on the top-left, where we usually start writing.

def saveFile():

    global filename
    t = text.get(0.0, END) #It will get the text from 0.0 till the end
    f = open(filename, 'w') #Open a file in write mode
    f.write(t) #It'll write
    f.close() #It'll close, can be written using "with"

def saveAs():
    
    f = asksaveasfile(mode="w", defaultextension='.txt') #Asks to save the file, defines in which format
    t = text.get(0.0, END) #Gets the text from 0.0 till the end
    try:
        f.write(t.rstrip()) #I didn't understand this, even watching the tutorial :(
    except:
        print('Some shit happened')

def openFile():
    f = askopenfile(mode="r") #Makes a query for you to search the file
    t = f.read() #Reads the file you oppened
    text.delete(0.0, END) #Deletes the previous text
    text.insert(0.0, t) #Adds new text

#This part is about making the GUI and the interactive menu

root = Tk()
root.title('Tesuto Editoru')
root.minsize(width=400, height=400)
root.maxsize(width=700, height=600)

text= Text(root, width=400, height=400, bg='black', fg='green') #Makes a textbox appear, also defines the collor of the text and the background
text.pack()

menubar = Menu(root) #Makes a menu on root
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New', command=newfile) #The next four lines just define the labels for the buttons corresponding to each function you defined
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label='Quit', command=root.quit) #If, by any chance, you need to recreate the "X" exit button, this line will do!
menubar.add_cascade(label='test', menu=menubar)

root.config(menu=filemenu)
root.mainloop()
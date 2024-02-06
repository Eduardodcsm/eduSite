from tkinter import *

root = Tk()
root.title('MY BUTTON')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

e = Entry(root, width=30, fg='red')
e.grid(row=0, column=1)
e.delete(0, END)

ee = Entry(root, width=30, fg='red')
ee.grid(row=0, column=2)
ee.delete(0, END)

def clickme():
    mylabel = Label(root, text='Hello' + ' ' + e.get(), fg="#33171FFFF")
    mylabel.grid(row=2, column=1)
    
def clickme2():
    mylabel = Label(root, text='Your age is:' + ' ' + ee.get(), fg="#33171FFFF")
    mylabel.grid(row=2, column=2)

mybutton = Button(root, text="Enter a name", command=clickme, fg="black", padx=30, pady=10)
mybutton.grid(row=1, column=1)

mybutton2 = Button(root, text="Enter your age", command=clickme2, fg="black", padx=30, pady=10)
mybutton2.grid(row=1, column=2)

root.mainloop()

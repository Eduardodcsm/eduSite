from tkinter import *
from tkinter import messagebox
root = Tk()

root.title('FIRST WINDOW')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

l1 = Label(root, text="WARNING POPUP")
l1.grid(row=0, column=0)

def warn1():
    messagebox.askokcancel("Warning", "ASK OK CANCEL")
def warn2():
    messagebox.askquestion("Warning", "ASK QUESTION")
def warn3():
    messagebox.askretrycancel("Warning", "ASK TRY CANCEL")
def warn4():
    messagebox.askyesno("Warning", "ASK YES NO")
def warn5():
    messagebox.askyesnocancel("Warning", "ASK YES NO CANCEL")
    

B1 = Button(root, text="FIRST BUTTON", command=warn1)
B1.grid(row=1, column=0)

B2 = Button(root, text="SECOND BUTTON", command=warn2)
B2.grid(row=2, column=0)

B3 = Button(root, text="THIRD BUTTON", command=warn3)
B3.grid(row=3, column=0)

B4 = Button(root, text="FORTH BUTTON", command=warn4)
B4.grid(row=4, column=0)

B5 = Button(root, text="FITH BUTTON", command=warn5)
B5.grid(row=5, column=0)

root.mainloop()
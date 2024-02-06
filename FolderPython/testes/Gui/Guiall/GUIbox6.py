from tkinter import *
root = Tk()

root.title('MY APP')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

q = IntVar()
q.get()
q.set('2')

def clickme(value):
    mylabel = Label(root, text= value)
    mylabel.pack()

Radiobutton(root, text= "Option 1", variable=q, value=1).pack(anchor='w')
Radiobutton(root, text= "Option 2", variable=q, value=2).pack(anchor='w')
Radiobutton(root, text= "Option 3", variable=q, value=3).pack(anchor='w')
Radiobutton(root, text= "Option 4", variable=q, value=4).pack(anchor='w')

mylabel = Label(root, text= q.get())
mylabel.pack()

mybutton = Button(root, text= "SUBMIT", command=lambda:clickme(q.get()))
mybutton.pack(anchor='w')

root.mainloop()

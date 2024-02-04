from tkinter import *
root = Tk()

root.title('CHECK BOX APPLICATION')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

a = StringVar()

c = Checkbutton(root, text= "Python", variable=a, onvalue="OK", offvalue="No")
c.deselect()
c.pack()

def click():
    my_label = Label(root, text=a.get())
    my_label.pack()

b1 = Button(root, text="Show Value", command=click)
b1.pack()

root.mainloop()
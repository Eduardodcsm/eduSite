from tkinter import *

root = Tk()
root.title('MY BUTTON')

root.iconbitmap(r'c:\Users\du57\Desktop\Eduardo\Portfolio\eduSite\Folder\Gui\star.ico')
root.geometry('500x500')

def my_click():
    my_label = Label(root, text="IVANKA OF CORSE, ARE YOU DURAK?",fg="#33171FFFF")
    my_label.pack()

mybutton = Button(root, text="WHO IS THE WOMAN OF YOUR LIFE?", command=my_click,fg="black",padx=30,pady=10)
mybutton.pack()

root.mainloop()

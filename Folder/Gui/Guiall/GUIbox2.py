from tkinter import * 

root = Tk() 
root.title('MY BOX GUI')

root.iconbitmap(r'c:\Users\du57\Desktop\Eduardo\Portfolio\eduSite\Folder\Gui\apple.ico')
root.geometry('500x500')

my_label = Label(root, text="Hello World")
my_label2 = Label(root, text="I'm under the water")

#my_label.pack()
#my_label2.pack()

root.mainloop()

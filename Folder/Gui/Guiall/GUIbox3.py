from tkinter import * 

root = Tk() 
root.title('MY GUI APP')

root.iconbitmap(r'c:\Users\du57\Desktop\Eduardo\Portfolio\eduSite\Folder\Gui\star.ico')
root.geometry('500x500')

my_label = Label(root, text="My new GUI app")
my_label2 = Label(root, text="This is line 2")

my_label.grid(row=0, column=1)
my_label2.grid(row=2, column=2)

root.mainloop()

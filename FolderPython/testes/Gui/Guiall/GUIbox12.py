from tkinter import *
root = Tk()

root.title('FIRST WINDOW')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

def clickme():
    click = Toplevel() 
    click.title('SECOND WINDOW')
    click.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
    click.geometry('800x500')
    
    l2 = LabelFrame(click, text="Second Window", padx=50, pady=50)
    l2.pack(padx=50, pady=50)

    B2 = Button(l2, text="Click Me To Quit The Program", command=root.quit)
    B2.pack()
    

l1 = LabelFrame(root, text="First Window", padx=50, pady=50)
l1.pack(padx=50, pady=50)

B1 = Button(l1, text="Click Me To The Second Window!", command=clickme)
B1.pack()

root.mainloop()
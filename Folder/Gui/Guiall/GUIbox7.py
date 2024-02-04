from tkinter import *
root = Tk()

root.title('MY APP')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

def open():
    my_label = Label(root,text=clicked.get())
    my_label.grid(row=2,column=2,padx=10,ipadx=30)


options = [
    
    'Iphone1',
    'Iphone2',
    'Iphone3',
    'Iphone4',
    'Iphone5',
    'Iphone6',
    'Iphone7',
    'Iphone8'
      
]

clicked = StringVar()

clicked.set(options[0])


drop = OptionMenu(root,clicked,*options)
drop.grid(row=0,column=1,padx=10,pady=10)

mybutton = Button(root, text="SUBMIT", command=open)
mybutton.grid(row=0,column=2,padx=10,pady=10)

root.mainloop()
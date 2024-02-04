from tkinter import *
root = Tk()

root.title('MY APP')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

frame = LabelFrame(root, text="This is the Frame !", padx=100,pady=100)
frame.grid(padx=20,pady=20)

def myclick():
    label1 = Label(frame, text="HELLO USER", fg='blue')
    label1.grid(row=10, column=10)


b1 = Button(frame, text="CLIKE ME", command=myclick)
b1.grid(row=0,column=1)

c = Button(frame, text="EXIT", command=root.quit)
c.grid(row=0,column=3)

root.mainloop()

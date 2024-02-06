from tkinter import *
root = Tk()

root.title('MY APP')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

vertical_slider = Scale(root, from_= 0, to = 250, orient = VERTICAL)
vertical_slider.pack(anchor="w")

horizontal_slider = Scale(root, from_= 0, to = 300, orient = HORIZONTAL)
horizontal_slider.pack(anchor="w")

def slider():
    ver_label = Label(root, text=vertical_slider.get()).pack()
    horizontal_label = Label(root, text=horizontal_slider.get()).pack()
    
ver_button = Button(root, text="CLICK FOR VALUES!", command=slider)
ver_button.pack()
root.mainloop()




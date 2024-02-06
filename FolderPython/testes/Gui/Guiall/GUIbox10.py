from tkinter import *
root = Tk()

root.title('Slider Application')
root.iconbitmap(r'eduSite\Folder\Gui\Guiall\star.ico')
root.geometry('800x500')

vertical_slider = Scale(root, from_= 0, to = 300, orient = VERTICAL)
vertical_slider.grid(row=0, column=0)

vertical_slider2 = Scale(root, from_= 0, to = 300, orient = VERTICAL)
vertical_slider2.grid(row=0, column=1)

vertical_slider3 = Scale(root, from_= 0, to = 300, orient = VERTICAL)
vertical_slider3.grid(row=0, column=2)

vertical_slider4 = Scale(root, from_= 0, to = 300, orient = VERTICAL)
vertical_slider4.grid(row=0, column=3)

vertical_slider5 = Scale(root, from_= 0, to = 300, orient = VERTICAL)
vertical_slider5.grid(row=0, column=4)


def value():
    ver_label = Label(root, text=vertical_slider.get())
    ver_label.grid(row=0, column=5)
    ver_label = Label(root, text=vertical_slider2.get())
    ver_label.grid(row=0, column=6)
    ver_label = Label(root, text=vertical_slider3.get())
    ver_label.grid(row=0, column=7)
    ver_label = Label(root, text=vertical_slider4.get())
    ver_label.grid(row=0, column=8)
    ver_label = Label(root, text=vertical_slider5.get())
    ver_label.grid(row=0, column=9)
    
ver_button = Button(root, text="CLICK FOR VALUES!", command=value)
ver_button.grid(row=2, column=10)
    
root.mainloop()



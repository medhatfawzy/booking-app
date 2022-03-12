#!/usr/bin/python

try:
    from tkinter import *
except:
    from Tkinter import *

from addReservation import *
from blacklist import *
from searchReservation import *

from PIL import Image, ImageTk
from awesometkinter.bidirender import add_bidi_support, render_text

root = Tk()
root.title("الحجوزات")


# Padding Variables
padx = 50
pady = 10

btn_add         = Button(root, text="Add Guest", command=add, padx=padx, pady=pady)
btn_check       = Button(root, text="Check Guest", command=search, padx=padx, pady=pady)
btn_blacklist   = Button(root, text="Blacklist", command=block, padx=padx, pady=pady)

logo_img    = ImageTk.PhotoImage(Image.open("alfayrouz.png"))
logo_label  = Label(image=logo_img)

# Putting things on screen
btn_add.grid(row=1, column=0)
btn_check.grid(row=1, column=1)
btn_blacklist.grid(row=1, column=2)

logo_label.grid(row=0, columnspan=3)




root.mainloop()
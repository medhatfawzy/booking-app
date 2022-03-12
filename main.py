#!/usr/bin/python
try:
    from tkinter import *
except:
    from Tkinter import *

from addReservation import *
from searchReservation import *
from blacklist import *

from PIL import Image, ImageTk
from awesometkinter.bidirender import add_bidi_support, render_text

root = Tk()
root.title("الحجوزات")

width = int(root.winfo_screenwidth() / 2)
height = int(root.winfo_screenheight() / 2)
x_left = int(root.winfo_screenwidth() / 2 - width / 2)
y_top = int(root.winfo_screenheight() / 2 - height / 2)

try:
    root.geometry(f"{width}x{height}+{x_left}+{y_top}")
except:
    root.geometry("{0}x{1}+{2}+{3}".format(width, height, x_left, y_top))

def add_local():
    add(root)
def search_local():
    search(root)
def block_local():
    block(root)

# The resort image
logo_img    = ImageTk.PhotoImage(Image.open("alfayrouz.png"))
logo_label  = Label(image=logo_img)

# Padding Variables
padx = 50
pady = 10
# Creating the Buttons
btn_add         = Button(root, text="Add Guest", command=add_local, padx=padx, pady=pady)
btn_search      = Button(root, text="Check Guest", command=search_local, padx=padx, pady=pady)
btn_blacklist   = Button(root, text="Blacklist", command=block_local, padx=padx, pady=pady)

# Putting things on screen
logo_label.place(relx=.5, rely=.4, anchor= CENTER)
btn_add.place(relx=.2, rely=.7, anchor= CENTER)
btn_search.place(relx=.5, rely=.7, anchor= CENTER)
btn_blacklist.place(relx=.8, rely=.7, anchor= CENTER)

root.mainloop()
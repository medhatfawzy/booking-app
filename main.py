#!/usr/bin/python
# Mimum python version required is 3.6
from tkinter import Tk, Label, Button, CENTER
# importing the classes from the other files
from addReservation import add
from searchReservation import search
from blacklist import block
# library for the images
from PIL import Image, ImageTk
# library for the rendering of Arabic in the widgets
from awesometkinter.bidirender import add_bidi_support, render_text

root = Tk()
root.title("الحجوزات")

# Centering the window
width = int(root.winfo_screenwidth() / 2)
height = int(root.winfo_screenheight() / 2)
x_left = int(root.winfo_screenwidth() / 2 - width / 2)
y_top = int(root.winfo_screenheight() / 2 - height / 2)
root.geometry(f"{width}x{height}+{x_left}+{y_top}")

# Defined local functions to be able to call the classes and pass the root to it
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
padx = 80
pady = 20
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
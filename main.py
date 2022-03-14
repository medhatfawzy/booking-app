#!/usr/bin/python
# Minimum python version required is 3.6
from tkinter import Tk, Label, Button, CENTER, PhotoImage, ttk
# importing the classes from the other files
from addReservation import add
from searchReservation import search
from blacklist import block
# library for the images
from PIL import Image, ImageTk
# library for rendering Arabic in the widgets
from awesometkinter.bidirender import add_bidi_support, render_text

# Creating the main window
root = Tk()
root.title("الحجوزات")

# root.iconbitmap(r"logo.xbm")

# style = ttk.Style()
# style.theme_use('breeze')

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

app_name_label = Label(root, text="Reservation App")
name_label = Label(root, text="AlFayrouz Beach Resort")

# The resort image
logo_img    = ImageTk.PhotoImage(Image.open("logo.png"))
logo_label  = Label(image=logo_img)

# Padding Variables
padx = 80
pady = 20
# Creating the Buttons
btn_add         = Button(root, text="Add Guest", command=add_local, padx=padx, pady=pady)
btn_search      = Button(root, text="Check Guest", command=search_local, padx=padx, pady=pady)
btn_blacklist   = Button(root, text="Blacklist", command=block_local, padx=padx, pady=pady)

# Putting things on screen
app_name_label.place(relx=0.5, rely=0.1, anchor=CENTER)
logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)
name_label.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_add.place(relx=0.2, rely=0.7, anchor= CENTER)
btn_search.place(relx=0.5, rely=0.7, anchor= CENTER)
btn_blacklist.place(relx=0.8, rely=0.7, anchor= CENTER)

root.mainloop()
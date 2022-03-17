#!/usr/bin/python3
# Minimum python version required is 3.6
from tkinter import Tk, CENTER, PhotoImage, ttk, RIGHT
from tkinter.ttk import Label, Button
from os import path

# importing the classes from the other files
from addReservation import add
from searchReservation import search
from blacklist import block
# library for rendering Arabic in the widgets
from awesometkinter.bidirender import add_bidi_support, render_text

# Creating the main window
root = Tk()
root.title("الحجوزات")

s=ttk.Style()
s.theme_use('clam')

# Centering the window
width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())
x_left = int(root.winfo_screenwidth() / 2 - width / 2)
y_top = int(root.winfo_screenheight() / 2 - height / 2)
root.geometry(f"{width}x{height}+{x_left}+{y_top}")
icon_img = PhotoImage(path.join("imgs","logo.png"))
root.iconphoto(True, icon_img)

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
logo_img    = PhotoImage(file=path.join("imgs", "logo.png"))
logo_label  = Label(image=logo_img)

# Padding Variables
padx = 80
pady = 20
# Creating the Buttons
add_img = PhotoImage(file=path.join("imgs","add.png"))
search_img = PhotoImage(file=path.join("imgs","block.png"))
block_img = PhotoImage(file=path.join("imgs","block16.png"))
btn_add         = Button(root, text=render_text("إضافة حجز"), image=add_img, compound=RIGHT, command=add_local)
btn_search      = Button(root, text=render_text("بحث عن نزيل"), image=search_img,compound=RIGHT, command=search_local)
btn_blacklist   = Button(root, text=render_text("قائمة الحظر"), image=block_img,compound=RIGHT, command=block_local)

# Putting things on screen
app_name_label.place(relx=0.5, rely=0.1, anchor=CENTER)
logo_label.place(relx=0.5, rely=0.3, anchor=CENTER)
name_label.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_add.place(relx=0.2, rely=0.7, anchor=CENTER)
btn_search.place(relx=0.5, rely=0.7, anchor=CENTER)
btn_blacklist.place(relx=0.8, rely=0.7, anchor=CENTER)

root.mainloop()
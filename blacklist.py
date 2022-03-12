#!/usr/bin/python

try:
    from tkinter import *
except:
    from Tkinter import *
from awesometkinter.bidirender import add_bidi_support

def block():
    blacklist_window = Toplevel()
    blacklist_window.title("الممنوعين من الدخول")

    width = int(blacklist_window.winfo_screenwidth() /3)
    height = int(blacklist_window.winfo_screenheight() /3)
    x_left = int(blacklist_window.winfo_screenwidth()/2 - width / 2)
    y_top = int(blacklist_window.winfo_screenheight()/2 - height / 2)

    try:
        blacklist_window.geometry(f"{width}x{height}+{x_left}+{y_top}")
    except:
        blacklist_window.geometry("{0}x{1}+{2}+{3}".format(width, height, x_left, y_top))


    name_entry = Entry(blacklist_window)
    name_label = Label(blacklist_window)
    add_bidi_support(name_entry)
    add_bidi_support(name_label)
    name_label.set(":الإسم")

    phone_number_entry = Entry(blacklist_window)
    phone_number_label = Label(blacklist_window)
    add_bidi_support(phone_number_entry)
    add_bidi_support(phone_number_label)
    phone_number_label.set(":الرقم")

    btn_save = Button(blacklist_window, text="save", command=blockGuest)

    rely_label = 0.4
    rely_entry = 0.5

    name_label.place(relx=.3, rely=rely_label, anchor= CENTER)
    name_entry.place(relx=.3, rely=rely_entry, anchor= CENTER)

    phone_number_label.place(relx=.7, rely=rely_label, anchor= CENTER)
    phone_number_entry.place(relx=.7, rely=rely_entry, anchor= CENTER)

    btn_save.place(relx=.5, rely=.8, anchor= CENTER)

def blockGuest():
    pass
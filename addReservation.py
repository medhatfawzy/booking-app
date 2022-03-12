#!/usr/bin/python

try:
    from tkinter import *
except:
    from Tkinter import *
# import awesometkinter as atk
from awesometkinter.bidirender import add_bidi_support


def add():
    add_window = Toplevel()
    add_window.title("إضافة نزيل")

    width = int(add_window.winfo_screenwidth() /3)
    height = int(add_window.winfo_screenheight() /3)
    x_left = int(add_window.winfo_screenwidth()/2 - width / 2)
    y_top = int(add_window.winfo_screenheight()/2 - height / 2)

    try:
        add_window.geometry(f"{width}x{height}+{x_left}+{y_top}")
    except:
        add_window.geometry("{0}x{1}+{2}+{3}".format(width, height, x_left, y_top))

    name_entry = Entry(add_window)
    name_label = Label(add_window)
    add_bidi_support(name_entry)
    add_bidi_support(name_label)
    name_label.set(":الإسم")

    phone_number_entry = Entry(add_window)
    phone_number_label = Label(add_window)
    add_bidi_support(phone_number_entry)
    add_bidi_support(phone_number_label)
    phone_number_label.set(":الرقم")

    arrival_date_entry = Entry(add_window)
    arrival_date_label = Label(add_window)
    add_bidi_support(arrival_date_entry)
    add_bidi_support(arrival_date_label)
    arrival_date_label.set(":معاد الوصول")

    btn_save = Button(add_window, text="save", command=saveGuest)

    rely_label = 0.4
    rely_entry = 0.5

    name_label.place(relx=.8, rely=rely_label, anchor= CENTER)
    name_entry.place(relx=.8, rely=rely_entry, anchor= CENTER)

    phone_number_label.place(relx=.5, rely=rely_label, anchor= CENTER)
    phone_number_entry.place(relx=.5, rely=rely_entry, anchor= CENTER)

    arrival_date_label.place(relx=.2, rely=rely_label, anchor= CENTER)
    arrival_date_entry.place(relx=.2, rely=rely_entry, anchor= CENTER)

    btn_save.place(relx=.5, rely=.8, anchor= CENTER)

def saveGuest():
    pass

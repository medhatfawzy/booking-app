#!/usr/bin/python

try:
    from tkinter import *
except:
    from Tkinter import *
from awesometkinter.bidirender import add_bidi_support

def search():
    search_window = Toplevel()
    search_window.title("البحث عن نزيل")

    width = int(search_window.winfo_screenwidth() /3)
    height = int(search_window.winfo_screenheight() /3)
    x_left = int(search_window.winfo_screenwidth()/2 - width / 2)
    y_top = int(search_window.winfo_screenheight()/2 - height / 2)

    try:
        search_window.geometry(f"{width}x{height}+{x_left}+{y_top}")
    except:
        search_window.geometry("{0}x{1}+{2}+{3}".format(width, height, x_left, y_top))

    name_entry = Entry(search_window)
    name_label = Label(search_window)
    add_bidi_support(name_entry)
    add_bidi_support(name_label)
    name_label.set(":الإسم")

    phone_number_entry = Entry(search_window)
    phone_number_label = Label(search_window)
    add_bidi_support(phone_number_entry)
    add_bidi_support(phone_number_label)
    phone_number_label.set(":الرقم")

    arrival_date_entry = Entry(search_window)
    arrival_date_label = Label(search_window)
    add_bidi_support(arrival_date_entry)
    add_bidi_support(arrival_date_label)
    arrival_date_label.set(":معاد الوصول")

    btn_search = Button(search_window, text="search", command=searchGuest)

    rely_label = 0.4
    rely_entry = 0.5

    name_label.place(relx=.2, rely=rely_label, anchor= CENTER)
    name_entry.place(relx=.2, rely=rely_entry, anchor= CENTER)

    phone_number_label.place(relx=.5, rely=rely_label, anchor= CENTER)
    phone_number_entry.place(relx=.5, rely=rely_entry, anchor= CENTER)

    arrival_date_label.place(relx=.8, rely=rely_label, anchor= CENTER)
    arrival_date_entry.place(relx=.8, rely=rely_entry, anchor= CENTER)

    btn_search.place(relx=.5, rely=.8, anchor= CENTER)

def searchGuest():
    pass
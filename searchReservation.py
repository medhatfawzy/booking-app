#!/usr/bin/python

try:
    from tkinter import *
except:
    from Tkinter import *
from awesometkinter.bidirender import add_bidi_support

def search():
    search_window = Toplevel()
    search_window.title("البحث عن نزيل")

    name_input = Entry(search_window)
    name_label = Label(search_window)
    add_bidi_support(name_input)
    add_bidi_support(name_label)
    name_label.set("الإسم")

    phone_number_input = Entry(search_window)
    phone_number_label = Label(search_window)
    add_bidi_support(phone_number_input)
    add_bidi_support(phone_number_label)
    phone_number_label.set("الرقم")

    arrival_date_entry = Entry(search_window)
    arrival_date_label = Label(search_window)
    add_bidi_support(arrival_date_entry)
    add_bidi_support(arrival_date_label)
    arrival_date_label.set("معاد الوصول")

    btn_search = Button(search_window, text="search", command=searchGuest)

    name_label.grid(row=0, column=1)
    name_input.grid(row=0, column=0)

    phone_number_label.grid(row=1, column=1)
    phone_number_input.grid(row=1, column=0)

    arrival_date_label.grid(row=2, column=1)
    arrival_date_entry.grid(row=2, column=0)

    btn_search.grid(row=3, column=0)

def searchGuest():
    pass
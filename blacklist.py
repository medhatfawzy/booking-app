#!/usr/bin/python

try:
    from tkinter import *
except:
    from Tkinter import *
from awesometkinter.bidirender import add_bidi_support

def block():
    blacklist_window = Toplevel()
    blacklist_window.title("الممنوعين من الدخول")


    name_input = Entry(blacklist_window)
    name_label = Label(blacklist_window)
    add_bidi_support(name_input)
    add_bidi_support(name_label)
    name_label.set("الإسم")

    phone_number_input = Entry(blacklist_window)
    phone_number_label = Label(blacklist_window)
    add_bidi_support(phone_number_input)
    add_bidi_support(phone_number_label)
    phone_number_label.set("الرقم")

    btn_save = Button(blacklist_window, text="save", command=blockGuest)


    name_label.grid(row=0, column=1)
    name_input.grid(row=0, column=0)

    phone_number_label.grid(row=1, column=1)
    phone_number_input.grid(row=1, column=0)

    btn_save.grid(row=3, column=0)

def blockGuest():
    pass
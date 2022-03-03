#!/usr/bin/python3
try:
    from tkinter import *
except:
    from Tkinter import *
import awesometkinter as atk
from awesometkinter.bidirender import add_bidi_support
import pandas as pd


def blacklist():
    blacklist_window = Toplevel()
    blacklist_window.title("الممنوعين من الدخول")

def add():
    add_window = Toplevel()
    add_window.title("إضافة نزيل")
    
    name_input = Entry(add_window)
    name_label = Label(add_window)
    add_bidi_support(name_input)
    add_bidi_support(name_label)
    name_label.set("الإسم")
    
    number_input = Entry(add_window)
    number_label = Label(add_window)
    add_bidi_support(number_input)
    add_bidi_support(number_label)
    number_label.set("الرقم")

    last_visit_input = Entry(add_window)
    last_visit_label = Label(add_window)
    add_bidi_support(last_visit_input)
    add_bidi_support(last_visit_label)
    last_visit_label.set("معاد الوصول")
    
    btn_save = Button(add_window, text="حفظ", command=saveGuest)
    add_bidi_support(btn_save)
    # btn_save.set("حفظ")

    name_label.grid(row=0, column=1)
    name_input.grid(row=0, column=0)

    number_label.grid(row=1, column=1)
    number_input.grid(row=1, column=0)
    
    last_visit_label.grid(row=2, column=1)
    last_visit_input.grid(row=2, column=0)
    
    btn_save.grid(row=3, column=0)

def check():
    check_window = Toplevel()
    check_window.title("بحث عن إسم")

def saveGuest():
    pass

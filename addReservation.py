#!/usr/bin/python3
from tkinter import Toplevel, CENTER, RIGHT, messagebox, Entry, PhotoImage
from tkinter.ttk import Button, Label
from awesometkinter.bidirender import add_bidi_support, render_text
from tkcalendar import DateEntry
from datetime import date
from os import path
from re import compile

from databaseAPI import DataBaseAPI

class Add(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("إضافة حجز")
        self.transient(root)
        # Centering the widget
        width = int(self.winfo_screenwidth() / 2)
        height = int(self.winfo_screenheight() / 1.5)
        x_left = int(self.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f"{width}x{height}+{x_left}+{y_top}")

        # creating the entry width for all the entries
        entry_width:int = 40
        # creating the name entry and label
        self.name_label = Label(self, text=render_text("الأسم:"))
        self.name_entry = Entry(self, width=entry_width)
        add_bidi_support(self.name_entry)
        # creating the phone number entry and label
        self.phone_number_label = Label(self, text=render_text("رقم الهاتف:"))
        self.phone_number_entry = Entry(self, width=entry_width)
        add_bidi_support(self.phone_number_entry)
        # creating the arrival date entry and label
        self.arrival_date_label = Label(self, text=render_text("تاريخ الوصول:"))
        self.arrival_date_entry = DateEntry(self, width=entry_width)
        add_bidi_support(self.arrival_date_entry)
        # creating the departure date entry and label
        self.departure_date_label = Label(self, text=render_text("تاريخ المغادرة:"))
        self.departure_date_entry = DateEntry(self,width=entry_width)
        add_bidi_support(self.departure_date_entry)
        # creating the unit name entry and label

        # creating the save button
        self.save_icon = PhotoImage(file=path.join("imgs","add16.png"))
        self.save_btn = Button(self, text=render_text("حفظ"),
                                image=self.save_icon, compound=RIGHT, command=self.saveGuest)

        # the distance from the left for the label and the entry
        relx_label:float = 0.7
        relx_entry:float = 0.4
        # putting things on the screen
        self.name_label.place(relx=relx_label, rely=0.1, anchor="w")
        self.name_entry.place(relx=relx_entry, rely=0.1, anchor=CENTER)
        self.phone_number_label.place(relx=relx_label, rely=0.3, anchor="w")
        self.phone_number_entry.place(relx=relx_entry, rely=0.3, anchor=CENTER)
        self.arrival_date_label.place(relx=relx_label, rely=0.5, anchor="w")
        self.arrival_date_entry.place(relx=relx_entry, rely=0.5, anchor=CENTER)
        self.departure_date_label.place(relx=relx_label, rely=0.7, anchor="w")
        self.departure_date_entry.place(relx=relx_entry, rely=0.7, anchor=CENTER)
        self.save_btn.place(relx=0.5, rely=0.9, anchor=CENTER)

    def saveGuest(self) -> None:
        '''
        This is the function that is activated when the user click the save button
        '''
        reservation_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
            'arrival_date': self.arrival_date_entry.get_date(),
            'departure_date': self.departure_date_entry.get_date()
        }
        if self.invalidDates(reservation_data): return
        if not DataBaseAPI.addReservation(self, reservation_data): return
        # These two line are used to close the Toplevel()
        self.destroy()
        self.update()


    def invalidDates(self, reservation_data:dict) -> bool:
        '''
        This is a helper function to check if there is wrong inputs
        '''
        arrival_date:date = reservation_data["arrival_date"]
        departure_date:date = reservation_data["departure_date"]
        # checking the validity of the dates
        if arrival_date == departure_date:
            messagebox.showwarning("خطأ في مواعيد الحجز",
                                    render_text("يوم الوصول هو نفس يوم المغادرة!"),
                                    parent=self)
            return True
        if arrival_date > departure_date:
            messagebox.showwarning("خطأ في مواعيد الحجز",
                                    render_text("يوم الوصول يسبق يوم المغادرة!"),
                                    parent=self)
            return True
        if arrival_date < date.today():
            messagebox.showwarning("خطأ في مواعيد الحجز",
                                    render_text("يوم الوصول هو يوم في الماضي!"),
                                    parent=self)
            return True
        return False


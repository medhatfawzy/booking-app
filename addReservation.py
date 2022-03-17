#!/usr/bin/python3
# Minimum python version required is 3.6
from tkinter import Toplevel, CENTER, RIGHT, messagebox, Entry, PhotoImage
from tkinter.ttk import Button, Label
from awesometkinter.bidirender import add_bidi_support, render_text
from tkcalendar import DateEntry
import datetime as dt
from os import path
from databaseAPI import DataBase
import csv

reservation_file = path.join("data", "reservations.csv")
blacklist_file = path.join("data", "blacklist.csv")

class add:
    def __init__(self, root):
        self.root = root
        self.add_window = Toplevel(self.root)
        self.add_window.title("إضافة نزيل")
        self.add_window.transient(root)

        # Centering the widget
        width = int(self.add_window.winfo_screenwidth() / 2)
        height = int(self.add_window.winfo_screenheight() / 2)
        x_left = int(self.add_window.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.add_window.winfo_screenheight() / 2 - height / 2)
        self.add_window.geometry(f"{width}x{height}+{x_left}+{y_top}")

        # creating the entry width for all the entries
        entry_width = 40
        # creating the name entry and label
        self.name_entry = Entry(self.add_window, width=entry_width)
        self.name_label = Label(self.add_window, text=render_text("الأسم:"))
        add_bidi_support(self.name_entry)
        # creating the phone number entry and label
        self.phone_number_entry = Entry(self.add_window, width=entry_width)
        self.phone_number_label = Label(self.add_window, text=render_text("رقم الهاتف:"))
        add_bidi_support(self.phone_number_entry)
        # creating the arrival date entry and label
        self.arrival_date_entry = DateEntry(self.add_window, width=entry_width, fg="white")
        self.arrival_date_label = Label(self.add_window, text=render_text("تاريخ الوصول:"))
        add_bidi_support(self.arrival_date_entry)
        # creating the departure date entry and label
        self.departure_date_entry = DateEntry(self.add_window,width=entry_width, fg="white")
        self.departure_date_label = Label(self.add_window, text=render_text("تاريخ المغادرة:"))
        add_bidi_support(self.departure_date_entry)

        # creating the unit name entry and label

        # creating the save button
        self.save_icon = PhotoImage(file=path.join("imgs","add16.png"))
        self.save_btn = Button(self.add_window, text=render_text("حفظ"),
                                image=self.save_icon, compound=RIGHT, command=self.saveGuest)

        # the distance from the left for the label and the entry
        relx_label = 0.7
        relx_entry = 0.4
        # putting things on the screen
        self.name_label.place(relx=relx_label, rely=0.1, anchor=CENTER)
        self.name_entry.place(relx=relx_entry, rely=0.1, anchor=CENTER)

        self.phone_number_label.place(relx=relx_label, rely=0.3, anchor=CENTER)
        self.phone_number_entry.place(relx=relx_entry, rely=0.3, anchor=CENTER)

        self.arrival_date_label.place(relx=relx_label, rely=0.5, anchor=CENTER)
        self.arrival_date_entry.place(relx=relx_entry, rely=0.5, anchor=CENTER)

        self.departure_date_label.place(relx=relx_label, rely=0.7, anchor=CENTER)
        self.departure_date_entry.place(relx=relx_entry, rely=0.7, anchor=CENTER)

        self.save_btn.place(relx=0.5, rely=0.9, anchor=CENTER)

    def saveGuest(self):
        '''
        This is the function that is activated when the user click the save button
        '''
        reservation_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
            'arrival_date': self.arrival_date_entry.get_date(),
            'departure_date': self.departure_date_entry.get_date()
        }
        if self.emptyFields(reservation_data): return
        if self.invalidInputs(reservation_data): return
        if self.nameBlacklisted(reservation_data): return
        if self.duplicateReservation(reservation_data): return
        db = DataBase()
        db.add_reservation(reservation_data.values())

        # These two line are used to close the Toplevel()
        self.add_window.destroy()
        self.add_window.update()

    def emptyFields(self, reservation_data):
        '''
        This is a helper function to check if there is an empty input field
        '''
        if '' in list(reservation_data.values()):
            messagebox.showinfo( "البيانات ناقصة",
                                    render_text("برجاء إكمال كافة البيانات"),
                                    parent=self.add_window)
            return True

    def nameBlacklisted(self, reservation_data):
        '''
        This helper function checks if the name we are trying to create a reservation for
        exists in the blacklist or not.
        '''
        with open(blacklist_file, 'r') as blacklist:
            blacklist_reader = csv.reader(blacklist)
            guest_data = list(reservation_data.values())[0:2]
            for line in blacklist_reader:
                if line == guest_data:
                    messagebox.showwarning("الإسم محظور",
                                    render_text("الأسم الذي تحاول إضافته في قائمة الحظر!"),

                                    parent=self.add_window)
                    return True

    def duplicateReservation(self, reservation_data):
        '''
        This helper function checks if the reservation is already added
        '''
        with open(reservation_file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                if line == list(reservation_data.values()):
                    messagebox.showinfo("الحجز مكرر",
                                    render_text("هذا الحجز موجود بالفعل!"),
                                    parent=self.add_window)
                    return True

    def invalidInputs(self, reservation_data):
        arrival_date = reservation_data["arrival_date"]
        departure_date = reservation_data["departure_date"]

        if arrival_date == departure_date:
            messagebox.showwarning("خطأ في مواعيد الحجز",
                                    render_text("يوم الوصول هو نفس يوم المغادرة!"),
                                    parent=self.add_window)
            return True
        if arrival_date > departure_date:
            messagebox.showwarning("خطأ في مواعيد الحجز",
                                    render_text("يوم الوصول يسبق يوم المغادرة!"),
                                    parent=self.add_window)
            return True
        if arrival_date < dt.date.today():
            messagebox.showwarning("خطأ في مواعيد الحجز",
            render_text("يوم الوصول هو يوم في الماضي!"),
            parent=self.add_window)
            return True

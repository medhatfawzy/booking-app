#!/usr/bin/python3
from tkinter import Toplevel, CENTER, RIGHT, messagebox, Entry, PhotoImage
from tkinter.ttk import Button, Label
from awesometkinter.bidirender import add_bidi_support, render_text
from os import path
from re import compile

from databaseAPI import DataBase
import csv

reservation_file = path.join("data", "reservations.csv")
blacklist_file = path.join("data", "blacklist.csv")

class Search(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("البحث عن نزيل")
        self.transient(root)
        # Centering the widget
        width = int(self.winfo_screenwidth() / 2)
        height = int(self.winfo_screenheight() / 2)
        x_left = int(self.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f"{width}x{height}+{x_left}+{y_top}")
        # creating the entry width for all the entries
        entry_width:int = 40
        # creating the name entry and label
        self.name_entry = Entry(self, width=entry_width)
        self.name_label = Label(self, text=render_text("الأسم:"))
        add_bidi_support(self.name_entry)
        # creating the phone number entry and label
        self.phone_number_entry = Entry(self, width=entry_width)
        self.phone_number_label = Label(self, text=render_text("رقم الهاتف:"))
        add_bidi_support(self.phone_number_entry)
        # creating the search button
        self.search_icon = PhotoImage(file=path.join("imgs","search16.png"))
        self.search_btn = Button(self, text=render_text("بحث"),
                                image=self.search_icon, compound=RIGHT, command=self.searchGuest)
        # the distance from the left for the label and the entry
        relx_label:float = 0.7
        relx_entry:float = 0.4
        # putting things on the screen
        self.name_label.place(relx=relx_label, rely=0.2, anchor="w")
        self.name_entry.place(relx=relx_entry, rely=0.2, anchor=CENTER)
        self.phone_number_label.place(relx=relx_label, rely=0.4, anchor="w")
        self.phone_number_entry.place(relx=relx_entry, rely=0.4, anchor=CENTER)
        self.search_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    def searchGuest(self) -> None:
        '''
        This is the function that is activated when the user click the search button
        '''
        guest_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get()
        }
        if self.invalidInputs(guest_data): return
        if self.nameBlacklisted(guest_data): return
        guest_reservations = []
        with open(reservation_file, 'r') as reservations:
            filereader = csv.reader(reservations)
            for line in filereader:
                if line[0:2] == list(guest_data.values()):
                    guest_reservations.append(line)
        self.showResults(guest_reservations)
        # These two line are used to close the Toplevel()
        self.destroy()
        self.update()

    def invalidInputs(self, guest_data:dict) -> bool:
        '''
        This is a helper function to check if there is an empty input field or wrong inputs
        '''
        # checking for empty fields
        if '' in list(guest_data.values()):
            messagebox.showwarning("البيانات ناقصة",
                                render_text("برجاء إكمال كافة البيانات"),
                                parent=self)
            return True
        # checking the validity of the phone number field, the number must be an egyptian phone number
        phone_number = guest_data["phone_number"]
        number_re = compile(r"^01[0-2,5]\d{8}")
        if number_re.match(phone_number) is None:
            messagebox.showwarning("خطأ في رقم الهاتف",
                                    render_text("الرجاء إدخال رقم هاتف صحيح!"),
                                    parent=self)
            return True
        return False

    def nameBlacklisted(self, guest_data:dict) -> bool:
        '''
        This helper function checks if the name we are searching for
        exists in the blacklist or not.
        '''
        with open(blacklist_file, 'r') as blacklist:
            filereader = csv.reader(blacklist)
            for line in filereader:
                if line == list(guest_data.values()):
                    messagebox.showwarning( "الأسم في قائمة الحظر",
                                            render_text("الإسم الذي تبحث عنه في قائمة الحظر"),
                                            parent=self)
                    return True
        return False

    def showResults(self, guest_reservations:list) -> None:
        if len(guest_reservations) == 0: return
        for reservation in guest_reservations:
            messagebox.showinfo("حجوزات النزيل",
                                render_text(f"""
                                الأسم : {reservation[0]}
                                رقم الهاتف : {reservation[1]}
                                تاريخ الوصول : {reservation[2]}
                                تاريخ المغادرة : {reservation[3]}
                                """),
                                parent=self)
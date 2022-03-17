#!/usr/bin/python3
# Minimum python version required is 3.6
from tkinter import Toplevel, CENTER, RIGHT, messagebox, Entry, PhotoImage
from tkinter.ttk import Button, Label
from awesometkinter.bidirender import add_bidi_support, render_text
from os import path

from databaseAPI import DataBase as db
import csv

blacklist_file = path.join("data", "blacklist.csv")

class block:
    def __init__(self, root):
        self.root = root
        self.blacklist_window = Toplevel(self.root)
        self.blacklist_window.title("إضافة إسم لقائمة الممنوعين من الدخول")
        self.blacklist_window.transient(root)
        width = int(self.blacklist_window.winfo_screenwidth() / 2)
        height = int(self.blacklist_window.winfo_screenheight() / 2)
        x_left = int(self.blacklist_window.winfo_screenwidth() / 2 - width / 2)
        y_top = int(self.blacklist_window.winfo_screenheight() / 2 - height / 2)

        self.blacklist_window.geometry(f"{width}x{height}+{x_left}+{y_top}")

        entry_width = 40

        self.name_entry = Entry(self.blacklist_window, width=entry_width)
        self.name_label = Label(self.blacklist_window, text=render_text("الأسم:"))
        add_bidi_support(self.name_entry)

        self.phone_number_entry = Entry(self.blacklist_window, width=entry_width)
        self.phone_number_label = Label(self.blacklist_window, text=render_text("رقم الهاتف:"))
        add_bidi_support(self.phone_number_entry)

        self.blocking_reason_entry = Entry(self.blacklist_window, width=entry_width)
        self.blocking_reason_label = Label(self.blacklist_window, text=render_text("سبب الحظر:"))
        add_bidi_support(self.blocking_reason_entry)
        # Creating the block button
        self.block_icon = PhotoImage(file=path.join("imgs","block16.png"))
        self.block_btn = Button(self.blacklist_window, text=render_text("حظر"),
                                image=self.block_icon, compound=RIGHT, command=self.blockGuest)

        # Putting things on the screen
        relx_label = 0.8
        relx_entry = 0.4

        self.name_label.place(relx=relx_label, rely=0.2, anchor=CENTER)
        self.name_entry.place(relx=relx_entry, rely=0.2, anchor=CENTER)

        self.phone_number_label.place(relx=relx_label, rely=0.4, anchor=CENTER)
        self.phone_number_entry.place(relx=relx_entry, rely=0.4, anchor=CENTER)

        self.blocking_reason_label.place(relx=relx_label, rely=0.6, anchor=CENTER)
        self.blocking_reason_entry.place(relx=relx_entry, rely=0.6, anchor=CENTER)

        self.block_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    def blockGuest(self):
        guest_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
            'blocking_reason': self.blocking_reason_entry.get()
        }

        if self.emptyFields(guest_data): return
        if self.duplicateName(guest_data): return

        if self.confirmationMssg():
            with open(blacklist_file, 'a') as blacklist:
                wrtiter = csv.DictWriter(blacklist, fieldnames=guest_data.keys())
                wrtiter.writerows([guest_data])
                print("data written")

        # These two line are used to close the Toplevel()
        self.blacklist_window.destroy()
        self.blacklist_window.update()

    def confirmationMssg(self):
        return messagebox.askyesno( "هل تريد إضافة الإسم فعلاً",
                                f"Are you sure about adding \"{self.name_entry.get()}\" to the blacklist?",
                                parent=self.blacklist_window)

    def duplicateName(self, guest_data):
        '''
        This helper function checks if the name we are trying to add to the blacklist
        exists in the blacklist already or not.
        '''
        with open(blacklist_file, 'r') as blacklist:
            reader = csv.reader(blacklist)
            for line in reader:
                if line == list(guest_data.values()):
                    messagebox.showinfo( "الإسم موجود بالفعل",
                            f"The name \"{self.name_entry.get()}\" is already in the blacklist!",
                            parent=self.blacklist_window)
                    return True

    def emptyFields(self, guest_data):
        '''
        This is a helper function to check if there is an empty input field
        '''
        if '' in list(guest_data.values()):
            messagebox.showinfo( "البيانات ناقصة",
                                    render_text("برجاء إكمال كافة البيانات"),
                                    parent=self.blacklist_window)
            return True
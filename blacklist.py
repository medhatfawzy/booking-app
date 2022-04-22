#!/usr/bin/python3
from tkinter import Toplevel, CENTER, RIGHT, Entry, PhotoImage
from tkinter.ttk import Button, Label
from awesometkinter.bidirender import add_bidi_support, render_text
from os import path
from re import compile

from databaseAPI import DataBaseAPI

class Block(Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("إضافة إسم لقائمة الممنوعين من الدخول")
        self.transient(root)
        # centering the widget
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
        # creating the blocking reason entry and label
        self.blocking_reason_entry = Entry(self, width=entry_width)
        self.blocking_reason_label = Label(self, text=render_text("سبب الحظر:"))
        add_bidi_support(self.blocking_reason_entry)
        # Creating the block button
        self.block_icon = PhotoImage(file=path.join("imgs","block16.png"))
        self.block_btn = Button(self, text=render_text("حظر"),
                                image=self.block_icon, compound=RIGHT, command=self.blockGuest)
        # the distance from the left for the label and the entry
        relx_label:float = 0.6
        relx_entry:float = 0.4
        # putting things on the screen
        self.name_label.place(relx=relx_label, rely=0.2, anchor="w")
        self.name_entry.place(relx=relx_entry, rely=0.2, anchor=CENTER)
        self.phone_number_label.place(relx=relx_label, rely=0.4, anchor="w")
        self.phone_number_entry.place(relx=relx_entry, rely=0.4, anchor=CENTER)
        self.blocking_reason_label.place(relx=relx_label, rely=0.6, anchor="w")
        self.blocking_reason_entry.place(relx=relx_entry, rely=0.6, anchor=CENTER)
        self.block_btn.place(relx=0.5, rely=0.8, anchor=CENTER)

    def blockGuest(self) -> None:
        guest_data = {
            'name': self.name_entry.get(),
            'phone_number': self.phone_number_entry.get(),
            'blocking_reason': self.blocking_reason_entry.get()
        }
        if not DataBaseAPI.blockGuest(self, guest_data): return
        # These two line are used to close the Toplevel()
        self.destroy()
        self.update()

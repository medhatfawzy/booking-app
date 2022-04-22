#!/usr/bin/python3
from tkinter import Tk, CENTER, PhotoImage, RIGHT
from tkinter.ttk import Label, Button, Style
from os import path
# library for rendering Arabic in the widgets
from awesometkinter.bidirender import render_text
# importing the classes from the other files
from addReservation import Add
from searchReservation import Search
from blacklist import Block
from removeReservation import Remove

class MainWindow(Tk):
    # Creating the main window
    def __init__(self):
        super().__init__()
        self.title("الحجوزات")
        # styling
        s = Style()
        s.theme_use('clam')
        s.configure("TLabel", font=("KacstOffice", 20))
        s.configure("TButton", font=("KacstOffice", 15))
        # setting the main window size (fullscreen)
        self.width   = self.winfo_screenwidth()
        self.height  = self.winfo_screenheight()
        self.geometry(f"{self.width}x{self.height}")
        self.icon_img = PhotoImage(file=path.join("imgs","logo.png"))
        self.iconphoto(True, self.icon_img)
        # initialize the GUI
        self.initUI()

    # Defined local functions to be able to call the classes and pass the self to it
    def add_local(self) -> None:
        Add(self)
    def search_local(self) -> None:
        Search(self)
    def block_local(self) -> None:
        Block(self)
    def remove_local(self) -> None:
        Remove(self)

    def initUI(self):
        # main window labels
        self.app_name_label      = Label(self, text=render_text("برنامج الحجوزات"))
        self.resort_name_label   = Label(self, text=render_text("قرية الفيروز بيتش"))
        # The resort image
        self.logo_img    = PhotoImage(file=path.join("imgs", "logo.png"))
        self.logo_label  = Label(self, image=self.logo_img)
        # Creating the Buttons
        self.add_img     = PhotoImage(file=path.join("imgs","add.png"))
        self.search_img  = PhotoImage(file=path.join("imgs","search.png"))
        self.block_img   = PhotoImage(file=path.join("imgs","block.png"))
        self.remove_img = PhotoImage(file=path.join("imgs", "remove.png"))
        self.btn_add         = Button(self, text=render_text("إضافة حجز"), image=self.add_img, compound=RIGHT, command=self.add_local)
        self.btn_search      = Button(self, text=render_text("بحث عن نزيل"), image=self.search_img,compound=RIGHT, command=self.search_local)
        self.btn_blacklist   = Button(self, text=render_text("قائمة الحظر"), image=self.block_img,compound=RIGHT, command=self.block_local)
        self.btn_remove      = Button(self, text=render_text("حذف حجز"), image=self.remove_img, compound=RIGHT, command=self.remove_local)
        # Putting things on screen on the center
        self.app_name_label.place    (relx=0.5, rely=0.05, anchor=CENTER)
        self.logo_label.place        (relx=0.5, rely=0.35, anchor=CENTER)
        self.resort_name_label.place (relx=0.5, rely=0.6, anchor=CENTER)
        self.btn_add.place           (relx=0.2, rely=0.8, anchor=CENTER)
        self.btn_search.place        (relx=0.4, rely=0.8, anchor=CENTER)
        self.btn_remove.place        (relx=0.6, rely=0.8, anchor=CENTER)
        self.btn_blacklist.place     (relx=0.8, rely=0.8, anchor=CENTER)

if __name__ == "__main__":
    App = MainWindow()
    App.mainloop()
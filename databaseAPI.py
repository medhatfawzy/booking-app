import sqlite3
from os import path

class DataBase:
    def __init__(self):
        # Connecting to the database and creating it if it dosen't exist
        self.database = sqlite3.connect(path.join("data", "database.db"))
        # Database cursor
        self.cursor = self.database.cursor()
        # self.cursor.execute("""
        #                 CREATE TABLE blacklist(
        #                     name text,
        #                     phone_number integer,
        #                     blocking_reason text
        #                 )
        # """)
    def add_reservation(self, reservation):
        name, phone_number, arrival_date, departure_date = reservation
        self.cursor.execute(f"""
                        INSERT INTO reservations VALUES('{name}',
                                                        '{phone_number}',
                                                        '{arrival_date}',
                                                        '{departure_date}')
        """)
        # cursor.executemany("INSERT INTO reservations VALUES (?,?,?,?)", reservations)
        # commit changes
        self.database.commit()
        # close the connection
        self.database.close()

    def search_guest(guest_data):
        name, phone_number = guest_data
        self.cursor.execute(f"")
        # commit changes
        self.database.commit()
        # close the connection
        self.database.close()

    def block_guest(guest_data):
        name, phone_number, blocking_reason = guest_data
        self.cursor.execute(f"")
        # commit changes
        self.database.commit()
        # close the connection
        self.database.close()

DataBase()
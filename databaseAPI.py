from os import path
from validatingInputs import *
import sqlite3


class DataBaseAPI:
    def __init__(self):
        # Connecting to the database or creating it if it dosen't exist
        self.database = sqlite3.connect(path.join("data", "database.db"))
        # Database cursor
        self.cursor = self.database.cursor()
        # Create the tables we will work with if not existing
        # Creating the guests table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS guests
                            (guestID INT NOT NULL UNIQUE PRIMARY KEY,
                            name TEXT NOT NULL,
                            phone_number TEXT NOT NULL,
                            city TEXT)
                            """)
        # Creating the Reservations table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS reservations
                            (reservationID INT NOT NULL UNIQUE PRIMARY KEY,
                            guestID INT NOT NULL,
                            unitID INT NOT NULL,
                            arrival_date TEXT NOT NULL,
                            departure_date TEXT NOT NULL,
                            numberOfPeople INT,
                            FOREIGN KEY (guestID)
                            REFERENCES guests(guestID)
                            ON DELETE RESTRICT)
                            """)
        # Creating the Rental Units table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS units
                            (unitID INT NOT NULL UNIQUE PRIMARY KEY,
                            unitType TEXT NOT NULL,
                            unitName TEXT NOT NULL)
                            """)
        # Creating the Blacklist table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS blacklist
                            (guestID INT NOT NULL UNIQUE,
                            blocking_reason TEXT,
                            FOREIGN KEY (guestID)
                            REFERENCES guests(guestID)
                            ON DELETE RESTRICT)
                            """)

        # self.cursor.execute("DROP TABLE reservations")
        # self.cursor.execute("DROP TABLE blacklist")
        # self.cursor.execute("DROP TABLE units")
        # self.cursor.execute("DROP TABLE guests")

    def searchReservation(self, root, guest_data:dict) -> tuple:
        if invalidInputs(root, guest_data): raise ValueError()
        is_blacklisted = isInBlacklist(root, guest_data)
        self.cursor.execute(""" SELECT  guests.name, guests.phone_number, guests.city,
                                        reservations.arrival_date, reservations.departure_date,
                                        units.unitName
                                FROM reservations
                                LEFT JOIN guests ON reservations.guestID = guests.guestID
                                LEFT JOIN units ON reservations.unitID = units.unitID
                                WHERE guests.name LIKE ?
                                AND guests.phone_number = ?""",
                                list(guest_data.values()))
        reservations = self.cursor.fetchall()
        return (reservations, is_blacklisted)

    def addReservation(self, root, reservation:dict) -> bool:
        """
        returns true if successful or false if not
        """
        # name, phone_number, arrival_date, departure_date = list(reservation.values())
        if ((emptyFields(root, reservation)
            or wrongPhoneNumber(root, reservation)
            or invalidDates(root, reservation))
            or self.isInBlacklist(root, reservation)
            or self.isDuplicateReservation(root, reservation)): return False
        self.cursor.execute(""" INSERT INTO reservations
                                (guestID, arrival_date, departure_date)
                                VALUES((SELECT guestID FROM guests
                                        WHERE name = ?
                                        AND phone_number = ?
                                        LIMIT 1),
                                        ?,?)""",
                            (reservation["name"], reservation["phone_number"], reservation["arrivale_date"], reservation["departure_date"]))
        # commit changes
        self.database.commit()
        return True

    def removeReservation(self, root, reservation:dict) -> bool:
        """
        returns true if successful or false if not
        """
        if (emptyFields(root, reservation)
            or wrongPhoneNumber(root, reservation)): return False

        self.cursor.execute("""DELETE FROM reservations
                                WHERE guestID IN (
                                    SELECT guestsID FROM guests
                                    WHERE guestName = ?
                                    AND phone_number = ?)
                                AND reservations.arrival_date=?
                                AND reservations.departure_date=?""",
                            (reservation["name"], reservation["phone_number"], reservation["arrivale_date"], reservation["departure_date"]))
        # commit changes
        self.database.commit()
        return True

    def blockGuest(self, root, guest_data:dict) -> bool:
        """
        returns true if successful or false if not
        """
        name, phone_number, blocking_reason = guest_data["name"], guest_data["phone_number"], guest_data["blocking_reason"]

        if (emptyFields(root, guest_data)
            or wrongPhoneNumber(root, guest_data)
            or self.isInBlacklist(root, guest_data)): return False
        self.cursor.execute(""" INSERT INTO blacklist
                                (guestID, blocking_reason)
                                VALUES( SELECT guestID
                                        FROM guests
                                        WHERE name LIKE ?
                                        AND phone_number=?
                                        LIMIT 1,
                                    ?) """,
                            (name, phone_number, blocking_reason))
        # commit changes
        self.database.commit()
        return True



    def isDuplicateReservation(self, root, reservation:dict) -> bool:
        name, phone_number, arrival_date, departure_date = list(reservation.values())
        self.cursor.execute("""SELECT reservations.guestID
                                FROM reservations
                                JOIN guests
                                ON reservations.guestID = guests.ID
                                WHERE guests.name LIKE ?
                                AND guests.phone_number=?
                                AND reservations.arrival_date=?
                                AND reservations.departure_date=?""",
                            (name, phone_number, arrival_date, departure_date))
        reservations = db.cursor.fetchall()
        if len(reservations) != 0:
            errorMssg("الحجز موجود", "الحجز موجود بالفعل!", parent=root)
            return True
        return False

    def isInBlacklist(self, root, guest_data:dict) -> bool:
        name, phone_number = guest_data["name"], guest_data["phone_number"]
        self.cursor.execute("""SELECT blacklist.guestID
                                FROM blacklist
                                JOIN guests
                                ON guests.guestID = blacklist.guestID
                                WHERE guests.name=? AND guests.phone_number=?""",
                            (name, phone_number))
        names_list = db.cursor.fetchall()
        if len(names_list) != 0:
            errorMssg("الأسم محظور", "الأسم موجود في قائمة الحظر!", parent=root)
            return True
        return False

# db = DataBaseAPI()
import sqlite3
from Tkinter import *

#second (2-nd) window
def show_add_contact_window():
    def add_contact():
        confirm_save_contact(name.get(), phone_number.get())

    new_wind = Toplevel(root)
    new_wind.title("Data entry")
    new_wind.geometry("500x110")
    Label(new_wind, text="Enter name").grid(row=0)
    Label(new_wind, text="Enter a phone number").grid(row=1)
    save_button = Button(new_wind,
                        text="Save?",
                        bg="white", fg="blue",
                        font="16",
                        width=8, height=1,
                        command=add_contact)
    save_button.grid(row=2)

    name = StringVar()
    phone_number = StringVar()
    name_entry = Entry(new_wind,textvariable=name,width=55)
    phone_number_entry = Entry(new_wind,textvariable=phone_number,width=55)
    name_entry.grid(row=0, column=1)
    phone_number_entry.grid(row=1, column=1)

#save contact in program (add to library)
def add_new_contact(name, phone_number):
    query = """INSERT INTO contacts (name, phone_number) VALUES(?,?)"""
    parameters = [name, phone_number]
    cursor.execute(query, parameters)
    conn.commit()
    print(name + " " + phone_number)

def confirm_save_contact(name, phone_number):
    def yes_action():
        add_new_contact(name, phone_number)
        confirm_wind.destroy()

    def no_action():
        confirm_wind.destroy() #closes the last window

#last (3-th) window
    confirm_wind = Toplevel(root)
    confirm_wind.title("Saving")
    confirm_wind.geometry("500x110")

    contact = StringVar(value = name + " " + phone_number)
    Label(confirm_wind, text="Save new contact?").grid(row=0, columnspan=2)
    Label(confirm_wind, textvariable=contact).grid(row=1, columnspan=2)
    yes_button = Button(confirm_wind,
                        text="Yes",
                        bg="white", fg="blue",
                        font="16",
                        width=20, height=1,
                        command=yes_action)
    yes_button.grid(row=2, column=0)

    no_button = Button(confirm_wind,
                       text="No",
                       bg="white", fg="red",
                       font="16",
                       width=20, height=1,
                       command=no_action)
    no_button.grid(row=2, column=1)

root = Tk()
root.title("Contacts")
root.geometry("500x110")

#first (1-st) window
b1 = Button(root,
            text="Add contact",
            bg="white", fg="blue",
            font="16",
            width=27,height=2,
            command=show_add_contact_window)
b1.grid(row=0, column=0)

b2 = Button(root,
            text="Quit",
            bg="white", fg="red",
            font="16",
            width=27,height=2,
            command=quit)
b2.grid(row=0, column=1)

#library creation
conn = sqlite3.connect("phonebook.sqlite3")
cursor = conn.cursor()

cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'""")

if len(cursor.fetchall()) == 0:
    cursor.execute("""CREATE TABLE contacts (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, phone_number TEXT)""")

root.mainloop()


#my email is yousafsahiwal3@gmail.com

import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3
import hashlib



def set_master_password():
    master_password = simpledialog.askstring("Set Master Password", "(you can only acces all your passwords with master password)\nEnter a master password:", show='*')
    confirm_password = simpledialog.askstring("Confirm Master Password", "Confirm your master password:", show='*')
    
    if master_password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match. Please try again.")
        set_master_password()
    else:
        password_hash = hash_password(master_password)
        c.execute("INSERT INTO master_password (password_hash) VALUES (?)", (password_hash,))
        conn.commit()
        messagebox.showinfo("Success", "Master password has been set.")
def verify_master_password():
    master_password = simpledialog.askstring("Verify Master Password", "Enter your master password:", show='*')
    c.execute("SELECT password_hash FROM master_password WHERE id = 1")
    stored_hash = c.fetchone()
    
    if stored_hash and hash_password(master_password) == stored_hash[0]:
        return True
    else:
        messagebox.showerror("Error", "Incorrect master password.")
        return False

def add_password():
    software = entry_software.get()
    username = entry_username.get()
    password = entry_password.get()

    if software == "" or username == "" or password == "":
        messagebox.showerror("Error", "All fields must be filled out")
        return

    try:
        c.execute("INSERT INTO passwords (software, username, password) VALUES (?, ?, ?)",
                  (software, username, password))
        conn.commit()
        messagebox.showinfo("Success", "Password saved successfully")
    except sqlite3.IntegrityError:
        password_update(software, username, password)

def password_update(software, username, password):
    c.execute("UPDATE passwords SET software = ?, password = ? WHERE username = ?",
              (software, password, username))
    conn.commit()
    messagebox.showinfo("Success", "Password updated successfully")

def passwords():
    if verify_master_password():
        passwords_window = tk.Toplevel(sc)
        passwords_window.title("Stored Passwords")

        c.execute("SELECT software, username, password FROM passwords")
        records = c.fetchall()

        row = 0
        for record in records:
            tk.Label(passwords_window, text=f"Software: {record[0]}").grid(row=row, column=0, padx=10, pady=10)
            tk.Label(passwords_window, text=f"Username: {record[1]}").grid(row=row, column=1, padx=10, pady=10)
            tk.Label(passwords_window, text=f"Password: {record[2]}").grid(row=row, column=2, padx=10, pady=10)
            row += 1

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


#gui
sc = tk.Tk()
sc.title("Password Manager")
#software label and entry
label_software = tk.Label(sc, text="Software")
label_software.grid(row=0, column=0, padx=10, pady=10)
entry_software = tk.Entry(sc)
entry_software.grid(row=0, column=1, padx=10, pady=10)
#username label and entry
label_username = tk.Label(sc, text="Username/Email")
label_username.grid(row=1, column=0, padx=10, pady=10)
entry_username = tk.Entry(sc)
entry_username.grid(row=1, column=1, padx=10, pady=10)
#password label and entry
label_password = tk.Label(sc, text="Password")
label_password.grid(row=2, column=0, padx=10, pady=10)
entry_password = tk.Entry(sc, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=10)

#buttons
button_add_password = tk.Button(sc, text="Add/Update Password", command=add_password)
button_add_password.grid(row=3, column=0, padx=10, pady=10)

button_show_passwords = tk.Button(sc, text="Show My Passwords", command=passwords)
button_show_passwords.grid(row=3, column=1, padx=10, pady=10)


#data base
conn = sqlite3.connect('password_manager.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY,
        software TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
conn.commit()
c.execute('''
    CREATE TABLE IF NOT EXISTS master_password (
        id INTEGER PRIMARY KEY,
        password_hash TEXT NOT NULL
    )
''')
conn.commit()
c.execute("SELECT password_hash FROM master_password WHERE id = 1")
if not c.fetchone():
    set_master_password()


sc.mainloop()
conn.close()

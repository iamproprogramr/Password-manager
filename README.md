# Password Manager

## Description
This Python script serves as a simple password manager application. It allows users to securely store and manage their passwords for various software applications.

## Features
- **Master Password**: Users can set and confirm a master password to access all stored passwords.
- **Password Storage**: Passwords are securely stored in an SQLite database.
- **Add/Update Passwords**: Users can add new passwords or update existing ones.
- **Display Passwords**: Users can view stored passwords for different software applications.

## Usage
1. **Setting up Master Password**:
   - When running the script for the first time, users are prompted to set a master password.
   - This master password is required to access stored passwords in the future.

2. **Adding Passwords**:
   - Users can add new passwords by entering the software name, username/email, and password.
   - If a password already exists for the provided username/email, it will be updated.

3. **Viewing Stored Passwords**:
   - Users can view all stored passwords by clicking the "Show My Passwords" button.
   - This action requires verification of the master password.
## Outputs

## Requirements
- Python 3.x
- Tkinter (for GUI)
- SQLite3 (for database management)

## Author
Muhammad Yousaf
- Email: yousafsahiwal3@gmail.com

---


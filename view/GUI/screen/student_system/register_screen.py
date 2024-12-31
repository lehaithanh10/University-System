import tkinter as tk
from tkinter import messagebox
from controller.student_authentication_controller import process_student_register
from utils.helpers import clear_window, is_succeed
import view.GUI.screen.student_enrollment_system.student_enrollment_menu_screen as student_enrollment_menu_screen
import view.GUI.screen.main_menu_system_screen as main_menu_system_screen


def register_screen(root: tk.Tk):
    clear_window(root)
    menu = tk.LabelFrame(root, text='Register', bg='#607b8d',
                         fg='white', padx=20, pady=20, font='Helvetica 18 bold', bd=5)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    row_existing = 0

    # Email
    emailLbl = tk.Label(menu, text="Email:", justify='left', fg='#ffc107',
                        font='Helvetica 16 bold', bg='#607b8d')
    emailLbl.grid(column=0, row=row_existing, padx=5, pady=5, sticky=tk.W)
    emailText = tk.StringVar()
    emailField = tk.Entry(menu, textvariable=emailText,
                          width=30, font='Helvetica 16')
    emailField.grid(column=1, row=row_existing, padx=5, pady=5)
    emailField.focus()
    row_existing += 1

    # Password
    passwordLbl = tk.Label(menu, text="Password:", fg='#ffc107',
                           font='Helvetica 16 bold', bg='#607b8d')
    passwordLbl.grid(column=0, row=row_existing, padx=5, pady=5, sticky=tk.W)
    passwordTxt = tk.StringVar()
    passwordField = tk.Entry(
        menu, textvariable=passwordTxt, show="*", width=30, font='Helvetica 16')
    passwordField.grid(column=1, row=row_existing, padx=5, pady=5)
    row_existing += 1

    # Confirm Password
    confirmPasswordLbl = tk.Label(menu, text="Confirm Password:", fg='#ffc107',
                                  font='Helvetica 16 bold', bg='#607b8d')
    confirmPasswordLbl.grid(column=0, row=row_existing,
                            padx=5, pady=5, sticky=tk.W)
    confirmPasswordTxt = tk.StringVar()
    confirmPasswordField = tk.Entry(
        menu, textvariable=confirmPasswordTxt, show="*", width=30, font='Helvetica 16')
    confirmPasswordField.grid(column=1, row=row_existing, padx=5, pady=5)
    row_existing += 1

    # Name
    nameLbl = tk.Label(menu, text="Name:", justify='left', fg='#ffc107',
                       font='Helvetica 16 bold', bg='#607b8d')
    nameLbl.grid(column=0, row=row_existing, padx=5, pady=5, sticky=tk.W)
    nameText = tk.StringVar()
    nameField = tk.Entry(menu, textvariable=nameText,
                         width=30, font='Helvetica 16')
    nameField.grid(column=1, row=row_existing, padx=5, pady=5)
    row_existing += 1

    # Register Button
    registerBtn = tk.Button(menu, text="Register",
                            bg='blue', fg='#ffc107',
                            font='Helvetica 15 bold', width=8, height=2, command=lambda: student_register_handler(emailText.get(), passwordTxt.get(), confirmPasswordTxt.get(), nameText.get(), root))
    registerBtn.grid(column=0, row=row_existing, padx=5, sticky=tk.W, pady=10)

    # Cancel Button
    cancelBtn = tk.Button(menu,
                          bg='red', fg='white',
                          font='Helvetica 15 bold',
                          text="Back", height=2, command=lambda: main_menu_system_screen.main_menu_system_screen(root))
    cancelBtn.grid(column=1, row=row_existing, padx=5, sticky=tk.E, pady=10)


def student_register_handler(email, password, confirm_password, name, root):
    if (confirm_password != password):
        messagebox.showerror(
            "Error", "Confirm password did not match password")
        return
    response = process_student_register(email, password, name)
    if is_succeed(response) is False:
        messagebox.showerror("Error", (response['message']))
        return

    messagebox.showinfo("Register", "Successfully register")
    student = response['data']

    student_enrollment_menu_screen.student_enrollment_menu_screen(
        student, root)

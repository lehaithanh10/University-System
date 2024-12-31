from re import S
import tkinter as tk
import view.GUI.screen.student_enrollment_system.student_enrollment_menu_screen as student_enrollment_menu_screen
import view.GUI.screen.student_system.student_menu_system_screen as student_menu_system_screen
from tkinter import messagebox
from controller.student_authentication_controller import process_student_login
from utils.helpers import clear_window, is_succeed


def login_screen(root: tk.Tk):
    clear_window(root)
    menu = tk.LabelFrame(root, text='Log In', bg='#607b8d',
                         fg='white', padx=20, pady=20, font='Helvetica 18 bold', bd=5)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    emailLbl = tk.Label(menu, text="Email:", justify='left', fg='#ffc107',
                        font='Helvetica 16 bold', bg='#607b8d')
    emailLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    emailText = tk.StringVar()
    emailField = tk.Entry(menu, textvariable=emailText,
                          width=30, font='Helvetica 16')
    emailField.grid(column=1, row=0, padx=5, pady=5)
    emailField.focus()

    passwordLbl = tk.Label(menu, text="Password:", fg='#ffc107',
                           font='Helvetica 16 bold', bg='#607b8d')
    passwordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

    passwordTxt = tk.StringVar()
    passwordField = tk.Entry(
        menu, textvariable=passwordTxt, show="*", width=30,  font='Helvetica 16')
    passwordField.grid(column=1, row=1, padx=5, pady=5)

    loginBtn = tk.Button(menu, text="Login",
                         bg='blue', fg='#ffc107',
                         font='Helvetica 15 bold', width=5, height=2, command=lambda: student_login_handler(emailText.get(), passwordTxt.get(), root))
    loginBtn.grid(column=1, row=3, padx=5, sticky=tk.W, pady=10)
    cancelBtn = tk.Button(menu,
                          bg='red', fg='white',
                          font='Helvetica 15 bold',
                          text="Back", height=2, command=lambda: student_menu_system_screen.student_menu_system_screen(root))
    cancelBtn.grid(column=1, row=3, sticky=tk.E, padx=5, pady=10)


def student_login_handler(email, password, root):
    response = process_student_login(email, password)
    if is_succeed(response) is False:
        messagebox.showerror(
            "Error", response['message'])

    else:
        messagebox.showinfo("Log In", "Successfully logged in")
        student = response['data']
        student_enrollment_menu_screen.student_enrollment_menu_screen(
            student, root)

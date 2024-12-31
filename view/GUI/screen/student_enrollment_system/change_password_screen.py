import tkinter as tk
import view.GUI.screen.main_menu_system_screen as main_menu_system_screen
from classes.User import Student
from tkinter import messagebox
from controller.student_enrollment_controller import change_password
from utils.helpers import clear_window, generate_hash_password, is_succeed
import view.GUI.screen.student_enrollment_system.student_enrollment_menu_screen as student_enrollment_menu_screen
import view.GUI.screen.student_system.student_menu_system_screen as student_menu_system_screen


def change_password_screen(student: Student, root: tk.Tk):
    clear_window(root)
    menu = tk.LabelFrame(root, text='Change Password', bg='#607b8d',
                         fg='white', padx=20, pady=20, font='Helvetica 18 bold', bd=5)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # New Password
    newPasswordLbl = tk.Label(menu, text="New Password:", fg='#ffc107',
                              font='Helvetica 16 bold', bg='#607b8d')
    newPasswordLbl.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    newPasswordTxt = tk.StringVar()
    newPasswordField = tk.Entry(
        menu, textvariable=newPasswordTxt, show="*", width=30, font='Helvetica 16')
    newPasswordField.grid(column=1, row=0, padx=5, pady=5)
    newPasswordField.focus()

    # Confirm New Password
    confirmNewPasswordLbl = tk.Label(menu, text="Confirm New Password:", fg='#ffc107',
                                     font='Helvetica 16 bold', bg='#607b8d')
    confirmNewPasswordLbl.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
    confirmNewPasswordTxt = tk.StringVar()
    confirmNewPasswordField = tk.Entry(
        menu, textvariable=confirmNewPasswordTxt, show="*", width=30, font='Helvetica 16')
    confirmNewPasswordField.grid(column=1, row=1, padx=5, pady=5)

    # Change Password Button
    changePasswordBtn = tk.Button(menu, text="Change Password",
                                  bg='blue', fg='#ffc107',
                                  font='Helvetica 15 bold', width=15, height=2, command=lambda: change_password_handler(newPasswordTxt.get(), confirmNewPasswordTxt.get(), student, root))
    changePasswordBtn.grid(column=1, row=2, padx=5, sticky=tk.W, pady=10)

    # Back Button
    backBtn = tk.Button(menu,
                        bg='red', fg='white',
                        font='Helvetica 15 bold',
                        text="Back", height=2, command=lambda: student_enrollment_menu_screen.student_enrollment_menu_screen(student, root))
    backBtn.grid(column=1, row=2, sticky=tk.E, padx=5, pady=10)


def change_password_handler(new_password, confirm_password, student: Student, root: tk.Tk):
    if (confirm_password != new_password):
        messagebox.showerror(
            "Error", "Confirm password did not match password")
        return
    response = change_password(new_password, student.student_id)
    if is_succeed(response) is False:
        messagebox.showerror("Error", response['message'])
    else:
        messagebox.showinfo("Change password", "Successfully change password")

        student.password = generate_hash_password(new_password)

        student.database.update_data_to_file(
            'student.data', student.read_student_information())
        student_menu_system_screen.student_menu_system_screen(root)

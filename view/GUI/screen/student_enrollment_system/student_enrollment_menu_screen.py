import tkinter as tk
import view.GUI.screen.student_enrollment_system.enrollment_list_screen as enrollment_list_screen
import view.GUI.screen.student_enrollment_system.change_password_screen as change_password_screen
import view.GUI.screen.student_enrollment_system.remove_subject_screen as remove_subject_screen
import view.GUI.screen.main_menu_system_screen as main_menu_system_screen

from controller.student_enrollment_controller import enroll_subject
from classes.User import Student
from utils.helpers import clear_window, is_succeed
from view.GUI.component.exit_button import exit_button
from view.GUI.component.menu_label import menu_label
from view.GUI.component.information_label import information_label
from view.GUI.component.option_button import option_button
from tkinter import messagebox


def student_enrollment_menu_screen(student: Student, root: tk.Tk):
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label(menu, "STUDENT MENU")
    information_label(menu, f"Welcome {student.name}")
    information_label(menu, "Please choose your options")
    option_button(menu, "Change password",
                  lambda: change_password_screen.change_password_screen(student, root))
    option_button(menu, "Enrol in subject",
                  lambda: enroll_subjects_handler(student))
    option_button(menu, "Remove a subject",
                  lambda: remove_subject_screen.remove_subject_screen(student, root))
    option_button(menu, "Show enrolled subject",
                  lambda: enrollment_list_screen.enrollment_list_screen(student, root))

    exit_button(menu, "Back to Main Menu",
                lambda: main_menu_system_screen.main_menu_system_screen(root))


def enroll_subjects_handler(student: Student):
    response = enroll_subject(student)

    if is_succeed(response) is False:
        messagebox.showerror(
            "Error", "You have already registered for the maximum number of subjects.")

    else:
        messagebox.showinfo(
            "Enrol subject",  f"""Registered subject {response['data']['subject_name']} ({
                response['data']['subject_id']})  with mark {response['data']['mark']} and grade {response['data']['grade']}.""")

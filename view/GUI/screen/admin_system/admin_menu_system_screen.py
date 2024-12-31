import tkinter as tk
import view.GUI.screen.admin_system.remove_student_screen as remove_student_screen
import view.GUI.screen.admin_system.categorize_student_screen as categorize_student_screen
import view.GUI.screen.admin_system.student_list_by_grade_screen as student_list_by_grade_screen
import view.GUI.screen.admin_system.student_list_screen as student_list_screen
import view.GUI.screen.main_menu_system_screen as main_menu_system_screen

from controller.admin_controller import clear_databases
from utils.helpers import clear_window, is_succeed
from view.GUI.component.exit_button import exit_button
from view.GUI.component.menu_label import menu_label
from view.GUI.component.information_label import information_label
from view.GUI.component.option_button import option_button
from tkinter import messagebox


def admin_menu_system_screen(root: tk.Tk):
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label(menu, "ADMIN MENU")
    information_label(menu, "Welcome to student system")
    information_label(menu, "Please choose your options")
    option_button(menu, "Clear Database", clear_database)
    option_button(menu, "View All Students",
                  lambda: student_list_screen.student_list_screen(root))
    option_button(menu, "Get Students by Grade",
                  lambda: student_list_by_grade_screen.student_list_by_grade_screen(root))
    option_button(menu, "Categorize Students by PASS/FAIL",
                  lambda: categorize_student_screen.categorize_student_screen(root))
    option_button(menu, "Remove Students by ID",
                  lambda: remove_student_screen.remove_student_screen(root))
    exit_button(menu, "Back to Main Menu",
                lambda: main_menu_system_screen.main_menu_system_screen(root))


def clear_database():
    if messagebox.askyesno("Exit", "Are you sure you want to clear system database?"):
        response = clear_databases()
        if (is_succeed(response)):
            messagebox.showinfo("Clear Database", "Database Cleared")
        else:
            messagebox.showerror("Error", response['message'])

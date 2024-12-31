import tkinter as tk
from utils.helpers import clear_window
import view.GUI.screen.student_system.login_screen as login_screen
import view.GUI.screen.main_menu_system_screen as main_menu_system_screen
import view.GUI.screen.student_system.register_screen as register_screen
from view.GUI.component import exit_button, information_label, menu_label, option_button


def student_menu_system_screen(root):
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label.menu_label(menu, "STUDENT MENU")
    information_label.information_label(menu, "Welcome to student system")
    information_label.information_label(menu, "Please choose your options")
    option_button.option_button(
        menu, "Log in", lambda: login_screen.login_screen(root))
    option_button.option_button(
        menu, "Register", lambda: register_screen.register_screen(root))
    exit_button.exit_button(menu, "Back to Main Menu",
                            lambda: main_menu_system_screen.main_menu_system_screen(root))

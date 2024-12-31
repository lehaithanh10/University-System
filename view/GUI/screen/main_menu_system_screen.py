import tkinter as tk
import view.GUI.screen.admin_system.admin_menu_system_screen as admin_menu_system_screen
import view.GUI.screen.student_system.student_menu_system_screen as student_menu_system_screen
from utils.helpers import clear_window, confirm_exit
from view.GUI.component.information_label import information_label
from view.GUI.component.menu_label import menu_label


def main_menu_system_screen(root: tk.Tk):
    clear_window(root)
    menu = tk.Frame(root)
    menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    menu_label(menu, "MAIN MENU")
    information_label(menu, "Welcome to university system"),
    information_label(menu, "Please choose your system")

    button_frame_top = tk.Frame(menu)
    button_frame_top.pack(pady=10, anchor="center")

    tk.Button(button_frame_top, text="Student System", bg='black', fg='white', font='Helvetica 14',
              command=lambda: student_menu_system_screen.student_menu_system_screen(root), height=2).pack(side="left")
    tk.Button(button_frame_top, text="Admin System", bg='black', fg='white', font='Helvetica 14',
              command=lambda: admin_menu_system_screen.admin_menu_system_screen(root), height=2).pack(side="left")

    tk.Button(menu, text="Exit", bg='red', fg='white', font='Helvetica 14', command=lambda: confirm_exit(root), width=12, height=2).pack(
        pady=10, anchor="center")

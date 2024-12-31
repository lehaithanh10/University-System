import tkinter as tk
from view.GUI.component.table import table
from controller.admin_controller import get_all_students_data
import view.GUI.screen.admin_system.admin_menu_system_screen as admin_menu_system_screen

from utils.helpers import clear_window, is_succeed
from tkinter import messagebox


def student_list_screen(root: tk.Tk):
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    response = get_all_students_data()
    if (is_succeed(response)):
        headers = [["Student Id", "Student Name", "Email"]]
        student_data = response['data']
        label = tk.Label(screen, text="STUDENT DATA", padx=20, pady=20,
                         font='Helvetica 16 bold')
        label.grid(row=0, column=1, columnspan=3, pady=(20, 20))
        if (len(student_data) > 0):
            table(screen, student_data, headers, 1)
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(column=3)

        button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                           font='Helvetica 14', command=lambda: admin_menu_system_screen.admin_menu_system_screen(root), height=2)
        button.grid(column=1, columnspan=3, pady=(20, 20))
    else:
        messagebox.showerror("Error", response['message'])

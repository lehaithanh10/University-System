import tkinter as tk
from view.GUI.component.table import table
from controller.admin_controller import categorise_student, get_all_students_data, get_students_by_grade, remove_student_by_id
import view.GUI.screen.admin_system.admin_menu_system_screen as admin_menu_system_screen

from utils.helpers import clear_window, is_succeed
from tkinter import messagebox


def remove_student_screen(root: tk.Tk):
    row_existing = 0
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    student_data_response = get_all_students_data()
    if (is_succeed(student_data_response) is False):
        messagebox.showerror("Error", student_data_response['message'])
    else:
        headers = [["Student Id", "Student Name", "Email"]]
        label = tk.Label(screen, text="LIST STUDENT:", padx=20, pady=20,
                         font='Helvetica 16 bold')
        row_existing += 1
        label.grid(row=0, column=1, columnspan=3, pady=(20, 20))
        if (len(student_data_response['data']) > 0):
            table(screen, student_data_response['data'], headers, 1)
            row_existing += len(student_data_response['data'] + headers)
            studentIdLabel = tk.Label(screen, text="Enter student id to remove:", justify='left', fg='#ffc107',
                                      font='Helvetica 12 bold', bg='#607b8d',)
            studentIdLabel.grid(column=1, row=row_existing,
                                padx=5, pady=20, columnspan=2)

            studentIdText = tk.StringVar()
            studentIdField = tk.Entry(screen, textvariable=studentIdText)
            studentIdField.grid(column=3, row=row_existing, padx=5, pady=20)
            studentIdField.focus()
            row_existing += 1
            tk.Button(screen, text="Remove",
                      bg='#252525', fg='#ffc107',
                      font='Helvetica 10 bold', command=lambda: remove_student_event_handler(studentIdText.get(), root)).grid(column=1, row=row_existing, padx=5, pady=5, sticky=tk.E, columnspan=2)
            row_existing += 1

        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(column=3)

        button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                           font='Helvetica 14', command=lambda: admin_menu_system_screen.admin_menu_system_screen(root), height=2)
        button.grid(column=1, columnspan=3, pady=(20, 20))


def remove_student_event_handler(student_id, root: tk.Tk):
    response = remove_student_by_id(student_id)
    if is_succeed(response) is False:
        messagebox.showerror(
            "Error", response['message'])
    else:
        messagebox.showinfo(
            "Remove student", f"""Student {
                student_id} have been removed from the system."""
        )
        admin_menu_system_screen.admin_menu_system_screen(root)

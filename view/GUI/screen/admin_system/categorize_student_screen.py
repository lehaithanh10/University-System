import tkinter as tk
import math
import view.GUI.screen.admin_system.admin_menu_system_screen as admin_menu_system_screen
from view.GUI.component.table import table
from controller.admin_controller import categorise_student
from utils.helpers import clear_window, is_succeed
from tkinter import messagebox


def categorize_student_screen(root: tk.Tk):
    clear_window(root)
    # Creating Canvas and Scrollbar
    screen_canvas = tk.Canvas(root, width=1200, height=600)
    screen_canvas.place(relx=0.61, rely=0.5, anchor=tk.CENTER)

    scrollbar = tk.Scrollbar(root, orient="vertical",
                             command=screen_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Place the Frame in the Canvas
    screen = tk.Frame(screen_canvas)
    screen_canvas.create_window((0, 0), window=screen, anchor="n")
    screen_canvas.configure(yscrollcommand=scrollbar.set)

    # Update the scroll region of the Canvas
    def configure_canvas(event):
        screen_canvas.configure(scrollregion=screen_canvas.bbox("all"))
    screen.bind("<Configure>", configure_canvas)

    row_existing = 0

    response = categorise_student()

    if (is_succeed(response) is False):
        messagebox.showerror(response['message'])
    else:
        pass_students = response['data']['pass_students']
        fail_students = response['data']['fail_students']

        headers = [["Student Id", "Student Name",
                    "Student Email", "Average Mark", "Overall Grade"]]

        tk.Label(screen, text="CATEGORIZE STUDENT", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=math.floor(len(headers[0])/2), columnspan=len(headers[0])-2, pady=(20, 20))
        row_existing += 1

        tk.Label(screen, text="PASS STUDENT:", pady=20,
                 font='Helvetica 16 bold', fg='green').grid(row=row_existing, column=1, columnspan=2)
        row_existing += 1

        if pass_students:
            table(screen, pass_students, headers, row_existing)
            row_existing += len(pass_students) + 1
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(row=row_existing, column=3, columnspan=2)
            row_existing += 1

        tk.Label(screen, text="FAIL STUDENT:", padx=20, pady=20,
                 font='Helvetica 16 bold', fg='red').grid(row=row_existing, column=1, columnspan=2)
        row_existing += 1

        if fail_students:
            table(screen, fail_students, headers, row_existing)
            row_existing += len(fail_students) + 1
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(row=row_existing, column=3, columnspan=2)
            row_existing += 1

        button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                           font='Helvetica 14', command=lambda: admin_menu_system_screen.admin_menu_system_screen(root), height=2)
        button.grid(column=math.floor(
            len(headers[0])//2), columnspan=2, pady=(20, 20))

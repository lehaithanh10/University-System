import tkinter as tk
import math
from view.GUI.component.table import table
from controller.admin_controller import get_students_by_grade
import view.GUI.screen.admin_system.admin_menu_system_screen as admin_menu_system_screen

from utils.helpers import clear_window, is_succeed
from tkinter import messagebox


def student_list_by_grade_screen(root: tk.Tk):
    clear_window(root)
    # Creating Canvas and Scrollbar
    screen_canvas = tk.Canvas(root, width=1100, height=700)
    screen_canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    # screen_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

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

    response = get_students_by_grade()

    if (is_succeed(response) is False):
        messagebox.showerror(response['message'])
    else:
        z_mark_student = response['data']['z_mark_student']
        p_mark_student = response['data']['p_mark_student']
        c_mark_student = response['data']['c_mark_student']
        d_mark_student = response['data']['d_mark_student']
        hd_mark_student = response['data']['hd_mark_student']

        headers = [["Student Id", "Student Name",
                    "Student Email", "Subject Name", "Mark", 'Grade']]

        tk.Label(screen, text="STUDENT DATA WITH GRADE", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=math.floor(len(headers[0])/2-1), columnspan=4, pady=(20, 20))
        row_existing += 1

        tk.Label(screen, text="Z GRADE:", pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
        row_existing += 1

        if (len(z_mark_student) > 0):
            table(screen, z_mark_student, headers, row_existing)
            row_existing += len(z_mark_student + headers)
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(column=3)
            row_existing += 1

        tk.Label(screen, text="P GRADE:", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
        row_existing += 1

        if (len(p_mark_student) > 0):
            table(screen, p_mark_student, headers, row_existing)
            row_existing += len(p_mark_student + headers)
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(column=3)
            row_existing += 1

        tk.Label(screen, text="C GRADE:", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
        row_existing += 1

        if (len(c_mark_student) > 0):
            table(screen, c_mark_student, headers, row_existing)
            row_existing += len(c_mark_student + headers)
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(column=3)
            row_existing += 1

        tk.Label(screen, text="D GRADE:", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
        row_existing += 1

        if (len(d_mark_student) > 0):
            table(screen, d_mark_student, headers, row_existing)
            row_existing += len(d_mark_student + headers)
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(column=3)
            row_existing += 1

        tk.Label(screen, text="HD GRADE:", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=0, columnspan=2)
        row_existing += 1

        if (len(hd_mark_student) > 0):
            table(screen, hd_mark_student, headers, row_existing)
            row_existing += len(hd_mark_student + headers)
        else:
            tk.Label(screen, text="NOTHING TO SHOW", padx=20, pady=20,
                     font='Helvetica 16 bold').grid(column=3)
            row_existing += 1

        button = tk.Button(screen, text="Back to Admin System", bg='red', fg='white',
                           font='Helvetica 14', command=lambda: admin_menu_system_screen.admin_menu_system_screen(root), height=2)
        button.grid(column=math.floor(
            len(headers[0])/2), columnspan=2, pady=(20, 20))

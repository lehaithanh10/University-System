import tkinter as tk
from classes.User import Student
from controller.student_enrollment_controller import change_password
from utils.helpers import clear_window
import view.GUI.screen.student_enrollment_system.student_enrollment_menu_screen as student_enrollment_menu_screen
from view.GUI.component.table import table


def enrollment_list_screen(student: Student, root: tk.Tk):
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    headers = [[
        "Subject ID", "Subject Name", "Mark", 'Grade']]

    if len(student.enrollment_list) == 0:
        tk.Label(screen, text="You have not registered for any courses",
                 font='Helvetica 16 bold').grid()
        button = tk.Button(screen, text="Back to Student Enrollment System", bg='red', fg='white',
                           font='Helvetica 14', command=lambda: student_enrollment_menu_screen.student_enrollment_menu_screen(student, root), height=2)
        button.grid(column=0, columnspan=2, pady=(20, 20))

    else:
        tk.Label(screen, text="ENROLLED SUBJECT:", padx=20,
                 pady=20, font='Helvetica 16 bold').grid(row=0, column=2, columnspan=2)
        table(screen, [[enrollment['subject_id'],  enrollment['subject_name'],  enrollment['mark'], enrollment['grade']]
                       for enrollment in student.enrollment_list], headers, 1)
        button = tk.Button(screen, text="Back to Student Enrollment System", bg='red', fg='white',
                           font='Helvetica 14', command=lambda: student_enrollment_menu_screen.student_enrollment_menu_screen(student, root), height=2)

        button.grid(column=2, columnspan=2, pady=(20, 20))

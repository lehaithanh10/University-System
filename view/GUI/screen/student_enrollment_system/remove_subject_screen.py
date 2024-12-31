import tkinter as tk
import view.GUI.screen.student_enrollment_system.student_enrollment_menu_screen as student_enrollment_menu_screen

from classes.User import Student
from tkinter import messagebox
from controller.student_enrollment_controller import change_password, remove_subject
from utils.helpers import clear_window, generate_hash_password, is_succeed
from view.GUI.component.table import table


def remove_subject_screen(student: Student, root: tk.Tk):
    row_existing = 0
    clear_window(root)
    screen = tk.Frame(root)
    screen.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    headers = [["Subject Id", "Subject Name", "Mark", "Grade"]]
    if (len(student.enrollment_list) > 0):
        tk.Label(screen, text="ENROLLED SUBJECT:", padx=20, pady=20,
                 font='Helvetica 16 bold').grid(row=row_existing, column=2, columnspan=2, pady=(0, 20))
        row_existing += 1
        table(screen, [[enrollment['subject_id'],  enrollment['subject_name'],  enrollment['mark'], enrollment['grade']]
                       for enrollment in student.enrollment_list], headers, 1)
        row_existing += len([[enrollment['subject_id'],  enrollment['subject_name'],  enrollment['mark'], enrollment['grade']]
                             for enrollment in student.enrollment_list] + headers)
        subjectIdLabel = tk.Label(screen, text="Enter subject id to remove:", justify='left', fg='#ffc107',
                                  font='Helvetica 12 bold', bg='#607b8d',)
        subjectIdLabel.grid(column=1, row=row_existing,
                            padx=5, pady=20, columnspan=2)

        subjectIdText = tk.StringVar()
        subjectIdField = tk.Entry(screen, textvariable=subjectIdText)
        subjectIdField.grid(column=3, row=row_existing, padx=5, pady=20)
        subjectIdField.focus()
        row_existing += 1
        tk.Button(screen, text="Remove",
                  bg='#252525', fg='#ffc107',
                  font='Helvetica 10 bold', command=lambda: remove_subject_event_handler(subjectIdField.get(), student, root)).grid(column=2, row=row_existing, padx=5, pady=5, sticky=tk.E)
        row_existing += 1

    else:
        tk.Label(screen, text="You have not registered for any courses.", padx=20, pady=20,
                 font='Helvetica 16 bold', fg="red").grid(column=3)

    button = tk.Button(screen, text="Back to Student Enrollment System", bg='red', fg='white',
                       font='Helvetica 14', command=lambda: student_enrollment_menu_screen.student_enrollment_menu_screen(student, root), height=2)
    button.grid(column=2, columnspan=2, pady=(20, 20))


def remove_subject_event_handler(subject_id, student: Student, root):
    response = remove_subject(student, subject_id)
    if (is_succeed(response)) is False:
        messagebox.showerror("Error", response['message'])
    else:
        messagebox.showinfo("Remove subject",
                            f"Subject {subject_id}-{response['data']['subject_name']} deleted successfully from enrollment list.")
        student_enrollment_menu_screen.student_enrollment_menu_screen(
            student, root)

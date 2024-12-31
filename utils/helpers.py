import re
import random
import bcrypt
import tkinter as tk
from tabulate import tabulate
from classes.Database import Database
from colorama import Fore
from tkinter import messagebox
from type import ResponseType, Response


def validate_email(email: str) -> bool:
    """
    Args: email: str \n
    validates email i.e checks weather email ends with "@university.com"
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@university\.com$'
    return re.match(pattern, email) is not None


def is_valid_password(password):
    # Check if the password is empty
    if not password:
        return False

    # Check if the password starts with an upper-case character
    if not password[0].isupper():
        return False

    # Check if the password contains at least five letters
    letters = re.findall(r'[A-Za-z]', password)
    if len(letters) < 5:
        return False

    # Check if the password ends with three or more digits
    digits = re.findall(r'\d+', password)
    if not digits or len(digits[-1]) < 3:
        return False

    return True


def is_email_existed(email):
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')
    for student in studentList:
        if student['email'] == email:
            return True  # Account already exists

    return False  # Account not found


def generate_new_student_id() -> str:
    database = Database()
    existing_ids = list(
        map(lambda student: student['student_id'], database.read_file_and_convert_to_list('student.data')))
    while True:
        student_id = random.randint(1, 999999)
        # Convert to six digits with leading zeros if necessary
        student_id_str = f'{student_id:06}'

        # Ensure the ID is unique
        if student_id_str not in existing_ids:
            break

    return student_id_str


def generate_hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def validate_password(password: str, hashPassword: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashPassword.encode('utf-8'))


def print_errors_message(content):
    print(f"{Fore.RED} {content}{Fore.RESET} \n")


def print_successful_message(content):
    print(f"{Fore.GREEN} {content}{Fore.RESET} \n")


def get_warning_message(content):
    return (f"{Fore.YELLOW} {content}{Fore.RESET} \n")


def print_information_message(content):
    print(f"{Fore.BLUE} {content}{Fore.RESET}")


def print_option_message(content):
    print(f"{Fore.MAGENTA} {content}{Fore.RESET}")


def print_list_in_table(list, headers):
    rows = [element.values() for element in list]
    print(tabulate(rows, headers, tablefmt="grid"))
    print('\n')


def is_retry_required():
    retry = input("Do you want to try again?(Y/N):")
    return retry != "N"


def is_succeed(response: Response):
    return response['status'] == ResponseType.SUCCESS.value


def clear_window(root: tk.Tk):
    for widget in root.winfo_children():
        widget.destroy()


def confirm_exit(root: tk.Tk):
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

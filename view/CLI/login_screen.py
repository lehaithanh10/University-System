from controller.student_authentication_controller import process_student_login
from type import ResponseType
from utils.helpers import is_retry_required, is_succeed, print_errors_message, print_information_message, print_successful_message
from view.CLI.student_enrollment_menu_screen import student_enrollment_menu_screen


def login_screen():
    print_information_message("Student login")
    is_login_successfully = False
    student = {}
    while True:
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        response = process_student_login(email, password)
        if is_succeed(response) is False:
            print_errors_message(response['message'])

            if is_retry_required() == False:
                break
        else:
            print_successful_message("Successfully logged in")
            student = response['data']
            is_login_successfully = True
            break

    if is_login_successfully == True:
        student_enrollment_menu_screen(student)

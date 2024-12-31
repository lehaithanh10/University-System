from classes.User import Student
from controller.student_enrollment_controller import change_password, enroll_subject, get_enrollment_list, remove_subject
from utils.helpers import is_retry_required, is_succeed, print_errors_message, print_information_message, print_list_in_table, print_option_message, print_successful_message


def student_enrollment_menu_screen(student: Student):
    while True:
        print_information_message("STUDENT SYSTEM MENU")
        print_information_message(
            f"Welcome {student.name}. Please choose your option")

        print_option_message("  1) Change password")
        print_option_message("  2) Enrol in subject")
        print_option_message("  3) Remove a subject")
        print_option_message("  4) Show enrolled subject")
        print_option_message("  5) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_information_message("Change password...")
            while True:
                new_password = input(
                    "Please enter a new password (requirements: start with a capital letter, at least 5 letters, followed by 3 or more numbers): ")
                response = change_password(new_password, student.student_id)

                if is_succeed(response):
                    print_successful_message(
                        f"Your password has been updated.")
                    break
                else:
                    print_errors_message(response['message'])
                    if is_retry_required() is False:
                        print_information_message(
                            "Exiting password modification.")
                        return
        elif choice == '2':
            print_information_message("Enrol in subject...")
            response = enroll_subject(student)

            if is_succeed(response):
                print_successful_message(
                    f"""Registered subject {response['data']['subject_name']} ({
                        response['data']['subject_id']})  with mark {response['data']['mark']} and grade {response['data']['grade']}.""")
            else:
                print_errors_message(response['message'])

        elif choice == '3':
            print_information_message("Remove a subject...")
            print_enrollment_list(student.enrollment_list)

            subject_id = input("Enter the subject ID to delete: ").strip()

            response = remove_subject(student, subject_id)

            if (is_succeed(response)):
                print_successful_message(
                    f"Subject {subject_id}-{response['data']['subject_name']} deleted successfully from enrollment list.")
            else:
                print_errors_message(response['message'])

        elif choice == '4':
            print_information_message("Show enrolled subject...")
            response = get_enrollment_list(student)
            if (is_succeed(response)):
                print_enrollment_list(response['data'])
            else:
                print_errors_message(response['message'])

        elif choice == '5':
            print_information_message("Exiting...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


def print_enrollment_list(enrollment_list):
    print_information_message("ENROLLED SUBJECT:")

    headers = ["Subject ID", "Subject Name", "Mark", "Grade"]

    print_list_in_table(enrollment_list, headers)

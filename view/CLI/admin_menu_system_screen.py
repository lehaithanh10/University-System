from controller.admin_controller import categorise_student, clear_databases, get_all_students_data, get_students_by_grade, remove_student_by_id
from utils.helpers import get_warning_message, is_retry_required, is_succeed, print_errors_message, print_information_message, print_list_in_table, print_option_message, print_successful_message


def admin_menu_system_screen():
    while True:
        print_information_message("ADMIN SYSTEM")
        print_option_message("  1) Clear database")
        print_option_message("  2) View all students")
        print_option_message("  3) Get students by grade")
        print_option_message("  4) Categories students by PASS/FAIL")
        print_option_message("  5) Remove students by id")
        print_option_message("  6) Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            choice = input(get_warning_message(
                "Are you sure to clear system's data?(Y/N):"))
            if choice == 'Y':
                response = clear_databases()
                if (is_succeed(response)):
                    print_successful_message("System's data has been cleared.")
                else:
                    print_errors_message(response['message'])

        elif choice == '2':
            print_information_message("View all students...")
            response = get_all_students_data()
            if (is_succeed(response)):
                print_list_student(response['data'])
            else:
                print_errors_message(response['message'])

        elif choice == '3':
            print_information_message("Get students by grade...")
            response = get_students_by_grade()

            if (is_succeed(response) is False):
                print_errors_message(response['message'])
            else:
                z_mark_student = response['data']['z_mark_student']
                p_mark_student = response['data']['p_mark_student']
                c_mark_student = response['data']['c_mark_student']
                d_mark_student = response['data']['d_mark_student']
                hd_mark_student = response['data']['hd_mark_student']
                headers = ["Student Id", "Student Name",
                           "Student Email", "Subject Name", "Mark", 'Grade']
                print("Z GRADE: \n")
                if (len(z_mark_student) > 0):
                    print_list_in_table(z_mark_student, headers)
                else:
                    print_information_message("  NOTHING TO SHOW \n")

                print("P GRADE: \n")
                if (len(p_mark_student) > 0):
                    print_list_in_table(p_mark_student, headers)
                else:
                    print_information_message("  NOTHING TO SHOW \n")

                print("C GRADE: \n")
                if (len(c_mark_student) > 0):
                    print_list_in_table(c_mark_student, headers)
                else:
                    print_information_message("  NOTHING TO SHOW \n")

                print("D GRADE: \n")
                if (len(d_mark_student) > 0):
                    print_list_in_table(d_mark_student, headers)
                else:
                    print_information_message("  NOTHING TO SHOW \n")

                print("HD GRADE: \n")
                if (len(hd_mark_student) > 0):
                    print_list_in_table(hd_mark_student, headers)
                else:
                    print_information_message("  NOTHING TO SHOW \n")

        elif choice == '4':
            print_information_message("Categories students by PASS/FAIL...")
            response = categorise_student()
            if (is_succeed(response) is False):
                print_errors_message(response['message'])

            else:
                pass_students = response['data']['pass_students']
                fail_students = response['data']['fail_students']
                headers = ["Student Id", "Student Name",
                           "Student Email", "Average Mark", 'Overall Grade']

                print_successful_message("PASS STUDENT:")
                if (len(pass_students) > 0):
                    print_list_in_table(pass_students, headers)
                else:
                    print_information_message("  NOTHING TO SHOW \n")

                print_errors_message("FAIL STUDENT:")
                if (len(fail_students) > 0):
                    print_list_in_table(fail_students, headers)
                else:
                    print_information_message("  NOTHING TO SHOW \n")

        elif choice == '5':
            print_information_message("Remove students by id...")
            print_information_message("STUDENTS LISTS")
            response = get_all_students_data()
            if (is_succeed(response) is False):
                print_errors_message(response['message'])

            else:
                print_list_student(response['data'])
                while True:
                    student_id = input("Enter student id to remove: ")
                    choice = input(get_warning_message(
                        "Are you sure to remove this student?(Y/N):"))
                    if choice == 'Y':
                        response = remove_student_by_id(student_id)
                        if is_succeed(response):
                            print_successful_message(
                                f"Student {student_id} have been removed from the system.")
                            break
                        else:
                            print_errors_message(response['message'])
                            if is_retry_required() == False:
                                break
                    else:
                        print_information_message("Back to menu")
                        break

        elif choice == '6':
            print_information_message("Returning to main menu...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")


def print_list_student(student_data):
    headers = ["Student Id", "Student Name", "Email"]
    print_list_in_table(student_data, headers)

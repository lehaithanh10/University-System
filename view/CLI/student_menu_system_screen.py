from utils.helpers import print_errors_message, print_information_message, print_option_message
from view.CLI.login_screen import login_screen
from view.CLI.register_screen import register_screen


def student_menu_system_screen():
    while True:
        print_information_message("STUDENT SYSTEM")
        print_option_message("  1) Log in")
        print_option_message("  2) Register")
        print_option_message("  3) Back to main menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            login_screen()

        elif choice == '2':
            register_screen()

        elif choice == '3':
            print_information_message("Returning to main menu...")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")

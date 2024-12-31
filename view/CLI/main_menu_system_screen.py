from utils.helpers import print_errors_message, print_information_message, print_option_message
from view.CLI.admin_menu_system_screen import admin_menu_system_screen
from view.CLI.student_menu_system_screen import student_menu_system_screen


def main_menu_system_screen():
    while True:
        print_information_message("Please choose an option:")
        print_option_message("  1) Go to student system")
        print_option_message("  2) Go to admin system")
        print_option_message("  3) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print_information_message("Navigating to student system...")
            student_menu_system_screen()
        elif choice == '2':
            print_information_message("Navigating to admin system...")
            admin_menu_system_screen()
        elif choice == '3':
            print_information_message("Exiting the system. Goodbye!")
            break
        else:
            print_errors_message("Invalid choice. Please try again.")

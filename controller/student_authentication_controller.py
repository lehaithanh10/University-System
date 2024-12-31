from classes.Database import Database
from classes.User import Student
from type import ResponseType
from utils.helpers import generate_hash_password, generate_new_student_id, is_email_existed, validate_password, validate_email, is_valid_password


def process_student_login(email, password):
    if is_email_existed(email) == False:
        return {
            'status': ResponseType.ERROR.value,
            'message': 'Your email not exists, please try again or register new account.'
        }
    else:
        validated_result = validate_student_account(email, password)
        if (validated_result['account_valid']) == False:
            return {
                'status': ResponseType.ERROR.value,
                'message': 'Incorrect password, please try again.'
            }
        else:
            return {
                'status': ResponseType.SUCCESS.value,
                'data': Student(
                    validated_result['student']['name'],
                    validated_result['student']['email'],
                    validated_result['student']['password'],
                    validated_result['student']['student_id'],
                    validated_result['student']['enrollment_list']
                )
            }


def validate_student_account(email, password):
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')
    studentFound = False
    for student in studentList:
        if student['email'] == email and validate_password(password, student['password']):
            # Account is valid
            studentFound = student
    if studentFound == False:
        return {
            'account_valid': False,
            'student': studentFound
        }
    else:
        return {
            'account_valid': True,
            'student': studentFound
        }


def process_student_register(email, password, name):
    while True:
        if is_email_existed(email) is True:
            return {
                'status': ResponseType.ERROR.value,
                'message': 'Email already exists'
            }
        if validate_email(email) is False and is_valid_password(password) is False:
            return {
                'status': ResponseType.ERROR.value,
                'message': 'Something went wrong with your email and password, please re-enter, make sure they are correctly formatted'
            }

        if is_valid_password(password) is False:
            return {
                'status': ResponseType.ERROR.value,
                'message': 'Something went wrong with your password, please re-enter, make sure it is correctly formatted'
            }
        if validate_email(email) is False:
            return {
                'status': ResponseType.ERROR.value,
                'message': 'Something went wrong with your email, please re-enter, make sure it is correctly formatted'
            }
        return {
            'status': ResponseType.SUCCESS.value,
            'data': post_student_register(email, password, name)
        }


def post_student_register(email, password, name):
    database = Database()
    student = Student(name, email, generate_hash_password(
        password), generate_new_student_id(), [])
    print(student.read_student_information())
    database.write_new_data_to_file(
        'student.data', student.read_student_information())
    return student

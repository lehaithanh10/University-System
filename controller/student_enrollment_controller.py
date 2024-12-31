import random
from classes.Subject import Subject
from classes.Database import Database
from classes.User import Student
from type import ResponseType
from utils.helpers import generate_hash_password, is_valid_password


def change_password(new_password, student_id):
    if is_valid_password(new_password):
        new_password_hashed = generate_hash_password(new_password)
        database = Database()
        database.update_data_to_file(
            'student.data', {'student_id': student_id, 'password': new_password_hashed})
        return {
            'status': ResponseType.SUCCESS.value,
            'data': {}
        }
    return {
        'status': ResponseType.ERROR.value,
        'message': 'Invalid password, please try again.'
    }


def enroll_subject(student: Student):
    database = Database()
    max_courses = 4
    list_subject = [
        Subject("001", "Math"), Subject("002", "Science"),
        Subject("003", "History"), Subject("004", "Art"),
        Subject("005", "Physics"), Subject("006", "Chemistry"),
        Subject("007", "English"), Subject("008", "Programming"),
    ]

    if len(student.enrollment_list) >= max_courses:
        return {
            'status': ResponseType.ERROR.value,
            'message': "You have already registered for the maximum number of subjects."
        }

    available_subject = [
        subject for subject in list_subject if subject.subject_id not in [subject["subject_id"] for subject in student.enrollment_list]]

    select_subject = random.choice(
        available_subject).read_subject_detail()

    mark = random.randint(25, 100)  # Randomly generate scores
    grade = get_grade_from_mark(mark)  # Get ratings based on scores
    student.enrollment_list.append({
        "subject_id": select_subject["subject_id"],
        "subject_name": select_subject["subject_name"],
        "mark": mark,
        "grade": grade
    })

    database.update_data_to_file(
        'student.data', student.read_student_information())

    return {
        'status': ResponseType.SUCCESS.value,
        'data': {
            "subject_id": select_subject["subject_id"],
            "subject_name": select_subject["subject_name"],
            "mark": mark,
            "grade": grade
        }
    }


def get_grade_from_mark(mark):
    if mark < 50:
        return 'Z'
    elif 50 <= mark < 65:
        return 'P'
    elif 65 <= mark < 75:
        return 'C'
    elif 75 <= mark < 85:
        return 'D'
    else:
        return 'HD'


def get_enrollment_list(student: Student):
    if len(student.enrollment_list) == 0:
        return {
            'status': ResponseType.ERROR.value,
            'message': 'You have not registered for any courses.'
        }
    return {
        'status': ResponseType.SUCCESS.value,
        'data': student.enrollment_list
    }


def remove_subject(student: Student, subject_id: str):
    for enrollment_record in student.enrollment_list:
        if enrollment_record['subject_id'] == subject_id:
            student.enrollment_list.remove(enrollment_record)
            student.database.update_data_to_file(
                'student.data', student.read_student_information())
            return {
                'status': ResponseType.SUCCESS.value,
                'data': enrollment_record
            }

    return {
        'status': ResponseType.ERROR.value,
        'data': "Subject ID not found."
    }

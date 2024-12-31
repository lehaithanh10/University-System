from classes.Database import Database
from type import ResponseType


def clear_databases():
    database = Database()
    database.clear_file('student.data')
    return {
        'status': ResponseType.SUCCESS.value
    }


def get_all_students_data():
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')
    return {
        'status': ResponseType.SUCCESS.value,
        'data': [{'student_id': student['student_id'], 'name': student['name'], 'email': student['email']}
                 for student in studentList]
    }


def get_students_by_grade():
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')

    student_enrolled = [
        student for student in studentList if len(student['enrollment_list']) > 0]

    z_mark_student = []
    p_mark_student = []
    c_mark_student = []
    d_mark_student = []
    hd_mark_student = []

    for student in student_enrolled:
        for enrollment_record in student['enrollment_list']:
            student_record_with_enrollment_details = {
                'student_id': student['student_id'],
                'student_name': student['name'],
                'student_email': student['email'],
                'subject_name': enrollment_record['subject_name'],
                'mark': enrollment_record['mark'],
                'grade': enrollment_record['grade'],
            }

            if enrollment_record['grade'] == 'Z':
                z_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'P':
                p_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'C':
                c_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'D':
                d_mark_student.append(student_record_with_enrollment_details)
            elif enrollment_record['grade'] == 'HD':
                hd_mark_student.append(student_record_with_enrollment_details)
    return {
        'status': ResponseType.SUCCESS.value,
        'data': {
            'z_mark_student': z_mark_student,
            'p_mark_student': p_mark_student,
            'c_mark_student': c_mark_student,
            'd_mark_student': d_mark_student,
            'hd_mark_student': hd_mark_student,
        }
    }


def categorise_student():
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')

    student_enrolled = [
        student for student in studentList if len(student['enrollment_list']) > 0
    ]
    fail_students = []
    pass_students = []

    for student in student_enrolled:
        marks = []
        for enrollment_record in student['enrollment_list']:
            marks.append(enrollment_record['mark'])

        average_mark = sum(marks) / len(marks)
        overall_grade = "Pass" if average_mark >= 50 else "Fail"

        student_record_with_enrollment_details = {
            'student_id': student['student_id'],
            'student_name': student['name'],
            'student_email': student['email'],
            'average_mark': average_mark,
            'overall_grade': overall_grade,
        }
        if overall_grade == "Pass":
            pass_students.append(student_record_with_enrollment_details)
        else:
            fail_students.append(student_record_with_enrollment_details)

    return {
        'status': ResponseType.SUCCESS.value,
        'data': {
            'pass_students': pass_students,
            'fail_students': fail_students,
        }
    }


def remove_student_by_id(student_id: str):
    database = Database()
    studentList = database.read_file_and_convert_to_list('student.data')

    if any(student['student_id'] == student_id for student in studentList):
        database.remove_data_from_file('student.data', student_id)
        return {
            'status': ResponseType.SUCCESS.value,
            'data': {}
        }
    else:
        return {
            'status': ResponseType.ERROR.value,
            'message': "This student_id does not exist. Please check again."
        }

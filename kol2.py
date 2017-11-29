# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.

#!/usr/bin/env python2.7
import statistics
import json
from pprint import pprint
from optparse import OptionParser


def get_students_total_average_score():
    with open('data.json') as data_file:
        data_students = json.load(data_file)
    tab = [(statistics.mean(data_students["Students"][i]["Grades"])) for i in range(0, len(data_students))]
    return "Students total average score {}.".format((statistics.mean(tab)))


def get_student_average_score_in_class(s_number):
    with open('data.json') as data_file:
        data_students = json.load(data_file)
    return "Average score of student {} {} is {}.".format(data_students["Students"][s_number]["Name"],
                                                          data_students["Students"][s_number]["Surname"],
                                                          statistics.mean(data_students["Students"]
                                                                          [s_number]["Grades"]))


def count_total_attendance_of_student(s_number):
    with open('data.json') as data_file:
        data_students = json.load(data_file)
    percent_of_total_attendance = sum(data_students["Students"][s_number]["Attendance"]) / float(len(
        data_students["Students"][s_number]["Attendance"]))
    return "Total attendance of student {} {} is {}%.".format(data_students["Students"][s_number]["Name"],
                                                              data_students["Students"][s_number]["Surname"],
                                                              percent_of_total_attendance)


def count_total_average_attendance_of_students():
    with open('data.json') as data_file:
        data_students = json.load(data_file)
    sum_tab = [sum(data_students["Students"][i]["Attendance"])/float(len(data_students["Students"][i]["Attendance"]))
               for i in range(0, len(data_students["Students"]))]
    return "Students total average attendance is {}%.".format((statistics.mean(sum_tab)) * 100)


def add_new_student_grades(number_of__student, *grades):
    with open('data.json') as json_file:
        data = json.load(json_file)
    for i in grades:
        data["Students"][number_of__student]['Grades'].append(i)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


def add_student_attendance(number_of_student, *attendance):
    with open('data.json') as json_file:
        data = json.load(json_file)
    for i in attendance:
        data["Students"][number_of_student]["Attendance"].append(i)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


def correct_student_grade(number_of_student, number_of_grade, new_grade):
    with open('data.json') as json_file:
        data = json.load(json_file)
    data["Students"][number_of_student]["Grades"][number_of_grade] = new_grade
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


def add_new_student(data_student):
    with open('data.json') as json_file:
        data = json.load(json_file)
    data["Students"].append(data_student)
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


def get_all_students():
    with open('data.json') as json_file:
        all_students = json.load(json_file)
    return all_students


def make_parser():
    parser = OptionParser()

    parser.add_option("-1", "--students", help="Print all students", dest="stud", action="store_true")

    parser.add_option("-2", "--add_new_grade", type="int", nargs=2,
                      help="Input two arguments, number of student and new grade", dest="add_new_grade")

    parser.add_option("-3", "--average_score across classes", help="Print average score across classes",
                      dest="average_score", action="store_true")

    parser.add_option("-4", "--student_average_score", type="int", help="Input number of student",
                      dest="student_average_score")

    parser.add_option("-5", "--total_attendance_of_students", help="Print total attendance of students",
                      dest="total_attendance", action="store_true")

    parser.add_option("-6", "--attendance_of_student", type="int", help="Input number of student",
                      dest="student_attendance")

    parser.add_option("-7", "--add_new_attendance", type="int", nargs=2,
                      help="Input two arguments, number of student and new attendance - 0,1", dest="add_new_attendance")

    parser.add_option("-8", "--correct_grade", type="int", nargs=3,
                      help="Input three arguments, number of student, number of grade, new grade", dest="correct_grade")
    return parser


if __name__ == '__main__':
    parser_2 = make_parser()
    (options, args) = parser_2.parse_args()

    if options.stud:
        pprint(get_all_students())

    if options.add_new_grade:
        add_new_student_grades(options.add_new_grade[0], options.add_new_grade[1])

    if options.average_score:
        print(get_students_total_average_score())

    if options.student_average_score >= 0:
        print(get_student_average_score_in_class(options.student_average_score))

    if options.total_attendance:
        print(count_total_average_attendance_of_students())

    if options.student_attendance >= 0:
        print(count_total_attendance_of_student(options.student_attendance))

    if options.add_new_attendance:
        add_student_attendance(options.add_new_attendance[0], options.add_new_attendance[1])

    if options.correct_grade:
        correct_student_grade(options.correct_grade[0], options.correct_grade[1], options.correct_grade[2])

    else:
        print("No option chosen")
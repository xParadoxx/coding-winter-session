"""
Represents the main relationship between classes + interaction between other objects / types.

Student:
    --> name: str - student name
    --> age: int
    --> id: str - school id
    --> registered_courses: list - list of courses

Teacher:
    --> name
    --> id
    --> age
    --> courses: a list of courses they teach

Course:
    --> name
    --> subject
    --> teacher: assigned teacher
    --> students: list of registered students

University:
    --> name
    --> motto
    --> students: a list of students
    --> teachers: a list of teachers
    --> courses: a list of courses

"""


import random
random.seed(10)


class Student:
    def __init__(self, name, age, identifier):
        self.name = name
        self.age = age
        self.id = identifier
        self.registered_courses = []


class Teacher:
    pass


class Course:
    pass


class University:
    def __init__(self, name, motto):
        self.name = name
        self.motto = motto
        self.students = {}
        self.teachers = []
        self.courses = []

    def add_student(self, student_name, student_age):
        identifier = f"{student_name[0]}{student_name[-1]}{student_age * random.randint(0, 200)}".lower().strip()
        student = Student(student_name, student_age, identifier)
        self.students[identifier] = student

    def display_student_info(self, stud_id):
        student = self.students.get(stud_id, None)
        if not student:
            print(f"WARNING: student with id {stud_id} not found")
            return
        print(f"student info:\n\tname: {student.name}\n\tage: {student.age}\n\tid: {self.students[stud_id].id}")


def main():
    # stud_1 = Student("Andrew Cheng", 18, "42069")
    # print(f"one of the students is {stud_1.name} and he is {stud_1.age} with id {stud_1.id}")

    uni = University("university of southwest", "rise and grind")

    # STUDENT CREATION
    uni.add_student("Andrew Cheng", 18)
    uni.display_student_info("ag2628")

    uni.add_student("bobby jebediah", 7)
    uni.display_student_info("bh56")

    print(f"there are {len(uni.students)} students in the school")

    uni.display_student_info("42")


main()

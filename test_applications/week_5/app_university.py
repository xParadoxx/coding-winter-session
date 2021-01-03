"""
Represents the main relationship between classes + interaction between other objects / types.

UniversityMember:
    --> name: str - student name
    --> age: int
    --> id: str - school id

Student extends UniversityMember:

    --> registered_courses: list - list of courses

Teacher extends UniversityMember:
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


class UniversityMember:
    def __init__(self, name, age, identifier):
        self.name = name
        self.age = age
        self.id = identifier
        self.courses = {}

    def display_info(self):
        print(
            f"INFO:\n\tname: {self.name}\n\tage: {self.age}\n\tcourses registered: {len(self.courses)}\n\tid: {self.id}")

    def add_course_to_schedule(self, course):
        self.courses[course.id] = course


class Student(UniversityMember):
    def __init__(self, name, age, identifier):
        super().__init__(name, age, identifier)
        self.gpa = None  # freshman student just being enrolled

    def add_grade(self, grade):
        pass  # logic to calculate gpa


class Teacher(UniversityMember):
    def __init__(self, name, age, identifier):
        super().__init__(name, age, identifier)
        self.office_hours = []

    def add_office_hours(self, time_block):
        pass


class Course:
    def __init__(self, name, subject, identifier):
        self.name = name
        self.subject = subject
        self.id = identifier
        self.teacher = None
        self.students = {}

    def display_info(self):
        print(f"INFO:\n\tname: {self.name}\n\tsubject: {self.subject}\n\tteacher: {self.teacher.name if self.teacher else None}")
        print(f"\tnumber of students: {len(self.students)}\n\tid: {self.id}")

    def register_student(self, student):
        self.students[student.id] = student
        student.add_course_to_schedule(self)

    def assign_teacher(self, teacher):
        self.teacher = teacher
        teacher.add_course_to_schedule(self)


class University:
    def __init__(self, name, motto):
        self.name = name
        self.motto = motto
        self.students = {}
        self.teachers = {}
        self.courses = {}

    def add_student(self, student_name, student_age):
        identifier = f"{student_name[0]}{student_name[-1]}{student_age * random.randint(0, 200)}".lower().strip()
        student = Student(student_name, student_age, identifier)
        self.students[identifier] = student

    def display_student_info(self, stud_id):
        student = self.students.get(stud_id, None)
        if not student:
            print(f"WARNING: student with id {stud_id} not found")
            return
        student.display_info()

    def add_teacher(self, teacher_name, teacher_age):
        identifier = f"{teacher_name[0]}{teacher_name[-1]}{teacher_age * random.randint(0, 200)}".lower().strip()
        teacher = Teacher(teacher_name, teacher_age, identifier)
        self.teachers[identifier] = teacher

    def display_teacher_info(self, teach_id):
        teacher = self.teachers.get(teach_id, None)
        if not teacher:
            print(f"WARNING: teacher with id {teach_id} not found")
            return
        teacher.display_info()

    def add_course_offering(self, course_name, course_subject):
        identifier = f"{course_name[0]}{course_subject[0]}{random.randint(0, 200)}".lower().strip()
        course = Course(course_name, course_subject, identifier)
        self.courses[identifier] = course

    def display_course_info(self, c_id):
        course = self.courses.get(c_id, None)
        if not course:
            print(f"WARNING: course with id {c_id} not found")
        course.display_info()

    def register_student_for_course(self, student_id, course_id):
        student = self.students.get(student_id, None)
        course = self.courses.get(course_id, None)
        if not student:
            print(f"WARNING: student does not exist with id {student_id}")
            return
        if not course:
            print(f"WARNING: course does not exist with id {course_id}")
            return
        course.register_student(student)
        print(f"successfully registered {student.name} in {course.name}")

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = self.teachers.get(teacher_id, None)
        course = self.courses.get(course_id, None)
        if not teacher:
            print(f"WARNING: teacher does not exist with id {teacher_id}")
            return
        if not course:
            print(f"WARNING: course does not exist with id {course_id}")
            return
        course.assign_teacher(teacher)
        print(f"successfully assigned {teacher.name} to {course.name}")


def main():
    # stud_1 = Student("Andrew Cheng", 18, "42069")
    # print(f"one of the students is {stud_1.name} and he is {stud_1.age} with id {stud_1.id}")

    uni = University("university of southwest", "rise and grind")

    # STUDENT CREATION
    uni.add_student("Andrew Cheng", 18)
    # uni.display_student_info("ag2628")

    uni.add_student("bobby jebediah", 7)
    # uni.display_student_info("bh56")

    # print(f"there are {len(uni.students)} students in the school")
    # uni.display_student_info("42")

    # TEACHER CREATION
    uni.add_teacher("mo bamba", 97)
    uni.add_teacher("eddie crusty", 45)
    # print(f"there are {len(uni.teachers)} teachers in the school")

    # uni.display_teacher_info("ma10573")
    # uni.display_teacher_info("ey5535")

    # COURSE CREATION
    uni.add_course_offering("Walking 204", "Life Skills")
    uni.add_course_offering("Ladders 101", "Life Sciences")
    # print(f"there are {len(uni.courses)} courses being offered")
    # uni.display_course_info("wl147")
    # uni.display_course_info("ll3")

    # INTERACTION
    uni.assign_teacher_to_course("ma10573", "wl147")
    uni.assign_teacher_to_course("ma10573", "ll3")

    uni.register_student_for_course("ag2628", "wl147")
    uni.register_student_for_course("bh56", "wl147")
    uni.register_student_for_course("bh56", "ll3")

    uni.display_student_info("ag2628")
    uni.display_student_info("bh56")
    uni.display_course_info("wl147")
    uni.display_course_info("ll3")
    uni.display_teacher_info("ma10573")



main()

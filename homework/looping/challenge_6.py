"""
Write a program that asks a teacher for the number of students in his or her class. Next, ask the teacher
how many assignments are given in this class. With this information prompt the user to enter in scores for each
student and compute their average grade in the class. Here's a sample running of your program:

How many students in the class? 2
How many assignments in the class? 2

Student #1
Assignment #1: 100
Assignment #2: 90
Student #1 earned a 95

Student #2
Assignment #1: 90
Assignment #2: 80
Student #2 earned a 85

"""


def get_num_students_and_assignments():
    num_students = int(input("how many students are in the class? "))
    num_assignments = int(input("how many assignments are in the class? "))
    return num_students, num_assignments


def calc_grades(num_students, num_assignments):
    for stud in range(num_students):
        print(f"\nstudent #{stud + 1}")

        sum_grade = 0
        for a in range(num_assignments):
            grade = int(input(f"\tassignment #{a + 1}: "))
            sum_grade += grade

        avg = sum_grade / num_assignments
        print(f"student #{stud + 1} earned a {avg:.2f}")

    return


def main():
    num_students, num_assignments = get_num_students_and_assignments()
    calc_grades(num_students, num_assignments)


main()

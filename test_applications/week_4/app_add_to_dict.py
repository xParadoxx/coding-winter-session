"""
this program takes in a list of students from the user and creates a set of IDs for them with proper mapping.

example of id setups:

id1: 00000
id2: 00001
id3: 00002
"""

import uuid


def get_num_students():
    num_students = int(input("how many students do you want to input? "))  # TODO(mo): you should always validate input
    return num_students


def create_students_dict(num_studs):
    students = {}
    for i in range(num_studs):
        students[uuid.uuid4()] = input("what is the full name of the student? ")
    # OPTIONAL: dictionary comprehension to condense lines 20-22 into one line
    # students = {uuid.uuid4(): input("what is the full name of the student? ") for i in range(num_studs)}
    return students


def main():
    num_studs = get_num_students()
    students = create_students_dict(num_studs)
    print(f"these are the students who currently enrolled: {students}")


main()

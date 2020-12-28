"""
so far we have only seen 1 (technically 2) collection objects:

lists       --> mutable ordered collections of items of same or varying types
strings     --> immutable ordered collection of chars (single char strings)

but there is a new type of collection object, called a dictionary

a dictionary is a helpful data structure that is builtin to python. in natural language, a dictionary has a series
of terms and each term has a definition. a python dictionary isn't much different, but instead of "terms" we call them
"keys" and instead of definitions we call them "values" or "data"

basically, a dictionary is a mapping from specific keys to specific values

f(x) ==> f: X -> Y
X is the domain, and y is the co-domain (for real functions, it is called the image aka the range)

FOR DICTIONARIES:

dictionary = {key_1: value_1, key_2: value_2, key_3: value_3, ..., key_n: value_n}
each key is UNIQUE

in other languages, dictionaries are called Map (i.e: HashMaps)
"""

"""
real world application: schools

NYU --> N#
"""

# students = {"N12345678": "Bruce Wayne", "N87654321": "Billy Bob"}
# print(students)

# look up in a dictionary
# specific_stud = students["N12345678"]
# print(specific_stud)


"""
different way of creating this dictionary
"""

# students = dict()
students = {}  # create an empty dictionary
# adding to the dictionary:
students["N12345"] = "Bruce Wayne"
students["N49592"] = "Peter Parker"
students["N99999"] = "Clark Kent"

# print(students)

# check if an element exists in the dictionary
# if "N12345" in students:
#     print(students["N12345"])

# to delete an element in the dictionary: use the del keyword

# del students["N49592"]

# print(students)

# to replace an element, it's the same as adding:
students["N99999"] = "Superman"

# print(students)

# to get a list of keys, you can use a dictionary method

# for key in students.keys():
#     # print(key)
#     print(students[key])

# to get a list of values, you can use a dictionary method

# for values in students.values():
#     print(values)

# to get a list of both keys and values (as a pair), you can use a dictionary method

# for key, value in students.items():
#     print(f"student info:\n\tstudent id: {key}\n\tname: {value}")

# OPTIONAL:
# for i, k_v in enumerate(students.items()):
#     key, value = k_v
#     print(f"student #{i+1} info:\n\tstudent id: {key}\n\tname: {value}")

# print(f"number of students: {len(students)}")
# print(students["N1234"])

# this is technically safer and better:
# print(students.get("N1234", "N/A"))


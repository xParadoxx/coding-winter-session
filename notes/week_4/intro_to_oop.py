"""
before, we learned that there were a few types in python

there are:

str
int
float
double
bool

NOTE: (collection types)
list
dict

but can we define our own types? yes we can

what if we want to develop an application that takes advantage of user defined types?

lets say we simulating a menagerie (collection of animals)

its illogical for me to say:
dog = 5

but its brittle coding to say:
dog = "dog"

because i don't capture the behaviorism of a dog:
    dogs bark, walk, fetch, eat, and sleep --> ACTIONS [DOES_A]
    they also have a name, color, breed, weight, and height --> ATTRIBUTES [HAS_A]

how can i represent this type of logic? using classes and objects

NOTES ON CLASSES:

the class definition this behaviorism we discussed

class TypeName:
    ...

classes have fields, and they have methods / functions:
--> fields are attributes
--> methods are the actions
"""

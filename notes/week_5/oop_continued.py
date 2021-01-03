"""
class continued
example of a class definition
"""

# version 0
# class Dog:
#     """
#     docstring of the class comes here
#     """
#     # this specific method / function is called the constructor
#     def __init__(self, name: str, age: int, breed: str, weight: float):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.weight = weight
#         # self._ssn = 69696969  # still not private
#         return


# my_dog = Dog("Lisa", 2, "corgi", 70)  # create an instance of the class
# print(type(my_dog))

# access a field or method using the . operator
# print(f"my dog's name is {my_dog.name} and she is {my_dog.age} years old")
"""
NOTE: other languages
other languages have what's called access restrictions on fields
--> public
--> protected
--> private
"""

"""
the my_dog variable is an instance of the Dog class
the Dog class has been instantiated --> my_dog object 
the type of my_dog is Dog
"""

# doggo = Dog("larry", 1, "aussie retriever", 60)
# another_doggo = Dog("jorge", 5, "corgi", 20)

# print(doggo.name)
# print(another_doggo.name)

"""
fields are defined in the constructor, but they can also be defined in any method of the class

methods are defined in the class body -- they are actions that the object can perform

we can also define new fields in our methods if need be (python feature, not present in other languages)
"""

# version 1
# class Dog:
#     """
#     docstring of the class comes here
#     """
#     # this specific method / function is called the constructor
#     def __init__(self, name: str, age: int, breed: str, weight: float):
#         self.name = f"sir {name}"
#         self.age = age * 7
#         self.breed = breed
#         self.weight = weight
#         self.number_of_barks = 0
#         self.ate_food = False
#         return
#
#     def eat(self):
#         print("dog am eating")
#         # specific python feature
#         self.ate_food = True
#
#     def bark(self):
#         print("wan wan")
#         self.number_of_barks += 1
#         if self.number_of_barks % 5 == 0:
#             self.eat()
#
#
# kawaii_dog = Dog("pikachu", 19, "pokemon", 13)
# kawaii_dog.bark()
# kawaii_dog.bark()
# kawaii_dog.bark()
# kawaii_dog.bark()
# kawaii_dog.bark()
# print(f"how many times did {kawaii_dog.name} bark? {kawaii_dog.number_of_barks}")
# print(f"did {kawaii_dog.name} eat food? {kawaii_dog.ate_food}")
#
#
# class Cat:
#     def __init__(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def meow(self):
#         pass


"""
well a dog is a ** type of animal ** and a cat is a ** type of animal **, and there are similarities between cats and
dogs which can be represented in a more logical structure using a fundamental aspect of oop --> inheritance

in an inheritance structure, we have the base class and the derived class
this is also sometimes known as the parent class and the child class
"""

# version 2
class Animal:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def eat(self):
        print(f"{self.name} is eating in the animal class")


class Dog(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)

    # overriding a method
    def eat(self):
        print("eating like a dawg")

    # this method does not depend on an instance of the class
    @staticmethod
    def cool_dog_fact():
        print("dogs are direct descendants of wolves")


class Cat(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)


# doggo = Dog("charizard", "gold", 50)
# doggo.eat()
#
# kitty = Cat("kitteh", "black", 2)
# kitty.eat()
#
# # BAD DESIGN
# unknown = Animal("some_name", "some_color", 1)
# unknown.eat()

Dog.cool_dog_fact()

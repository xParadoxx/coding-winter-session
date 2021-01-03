"""
Create a menagerie of animals

NOTE: inheritance layer

Some suggestions:

Animal:
    Dog
    Tiger
    Wolf

ALTERNATE:

Animal
    Domesticated:
        Dog
        Tiger
    Wild:
        Wolf

Write some test code to experiment with the behavior and functionality of your code!
"""


class Animal:
    def __init__(self, color, weight, breed):
        self.color = color
        self.weight = weight
        self.breed = breed

    def eat(self):
        print(f"nom nom i am {self.weight} lbs")


class Domesticated(Animal):
    def __init__(self, name, color, weight, breed, owner):
        super().__init__(color, weight, breed)
        self.name = name
        self.owner = owner


class Wild(Animal):
    def __init__(self, color, weight, breed):
        super().__init__(color, weight, breed)
        self.ailments = []

    def add_ailment(self, disease):
        self.ailments.append(disease)

    def get_cured(self, index):
        if index > len(self.ailments):
            print("not a valid illness")
            return
        print(f"removing this disease: {self.ailments.pop(index)}")


class Dog(Domesticated):
    def __init__(self, name, color, weight, breed, owner):
        super(Dog, self).__init__(name, color, weight, breed, owner)
        self.num_barks = 0
        self.is_neutered = False

    def bark(self):
        print(f"woof woof american dawg {self.name}")
        self.num_barks += 1
        if self.num_barks >= 10:
            self.neuter()

    def neuter(self):
        if self.is_neutered:
            print("already did the snip")
            return
        print("snip snip doggy")
        self.is_neutered = True


class Tiger(Domesticated):
    def __init__(self, name, color, weight, breed, owner, num_stripes):
        super(Tiger, self).__init__(name, color, weight, breed, owner)
        self.num_stripes = num_stripes

    def purr(self):
        print(f"meow meow or wtv {self.name.upper()}")


class Wolf(Wild):
    def __init__(self, color, weight, breed):
        super(Wolf, self).__init__(color, weight, breed)

    def growl(self):
        print("growling")

    def health_status(self):
        if len(self.ailments) > 1:
            print("bad condition")
        else:
            print("not too bad")


def main():
    # TEST CODE FOR DOG
    # doggo = Dog("doge", "beige", 22, "shiba", "me")
    # for i in range(10):
    #     doggo.bark()
    # doggo.neuter()
    # doggo.eat()

    # TEST CODE FOR TIGER
    # my_tiger = Tiger("rahah", "yellow", 336, "middle eastern", "aladding", 200)
    # my_tiger.purr()
    # my_tiger.eat()

    # TEST CODE FOR WOLF
    wolfy = Wolf("grayish brown", 420, "timber wolf")
    wolfy.growl()
    wolfy.add_ailment("rabies")
    wolfy.add_ailment("alzheimers")
    wolfy.health_status()
    wolfy.get_cured(10)
    wolfy.get_cured(1)
    wolfy.health_status()
    wolfy.eat()


main()


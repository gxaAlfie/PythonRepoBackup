# Program demonstrates relationship (i.e. is-a, has-a) between class and object

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# Dog is-an Animal
class Dog(Animal):
    def __init__(self, name):
        # Dog has-a name of some kind
        self.name = name

# Cat is-an Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has-a name of some kind
        self.name = name

# Person is-an Object
class Person(object):
    def __init__(self, name):
        # Person has-a name of some kind
        self.name = name
        # Person has a pet of some kind
        self.pet = None

# Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        # ?? hmm what is this strange magic
        # super returns parent of current class
        # this line calls __init__ method of parent(i.e. Person) and passing name argument
        super(Employee, self).__init__(name)
        self.salary = salary

# Fish is-an Object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog('Rover')

#satan is-a Cat
satan = Cat('Satan')

#mary is-a Person
mary = Person('Mary')

#frank is-an Employee with name "Frank" and Salary of 120000
frank = Employee("Frank", 120000)

#frank has-a pet rover
frank.pet = rover

#flipper is-a Fish
flipper = Fish()

#crouse is-a Salmon
crouse = Salmon()

#harry is-a Halibut
harry = Halibut()

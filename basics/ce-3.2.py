"""
class Car:

    def __init__(self, model, make, year):
        self.model = model
        self.make = make
        self.year = year

"""


class Dog:
    def __init__(self, pet_name):
        self.pet_name = pet_name


d1 = Dog("Mavis")

print(d1.pet_name)


class Guest:
    def __init__(self, first, last):
        self.first = first
        self.last = last


g_1 = Guest("Test", "User")

print(g_1.first)

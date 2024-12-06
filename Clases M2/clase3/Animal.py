class Animal:
    def  __init__(self):
        pass

    def hablar(self):
        pass

class Perro (Animal):

    def __init__(self):
        pass

    def hablar(self):
        return " el perro hace woof woof"
    
class Gato (Animal):

    def __init__(self):
        pass

    def hablar(self):
        return " el gato hace miau miau"
    
animales = [Perro(), Gato()]

for animal in animales:
    print(animal.hablar())

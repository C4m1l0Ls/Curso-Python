class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        pass

    def hablar(self):
        return "todo animal habla de alguna forma"

    def __str__(self):
        return f"mi animalito se llama {self.name}"
        
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    def hablar(self):
        return"woof woof"
    def _str_(self):
        return f"El nombre del perro es: {self.nombre}  su raza es : {self.raza}"

animal1 = Animal("whisky")
perro1 = Perro("Ginebra", "Pastor Aleman")

print(animal1.hablar())
print(animal1.__str__())

print(perro1.hablar())
print(perro1.__str__())



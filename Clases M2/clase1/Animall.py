#metodos de clase
class Animall:
    cantidadAnimales = 0
    def __init__(self, name):
        self.name = name
        Animall.cantidadAnimales += 1

    #decoradores pueden cabiar el comportamiento de los metodos
    @classmethod
    def totalAnimales(cls):
        return f"tengo {cls.catidadeAnimales}  animalitos"
animal1 = Animall("ron")
animal2 = Animall("rayo")

print (animal1.name)
print (Animall.totalAnimales())
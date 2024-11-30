class Vehiculo:
    def __init__(self, tipo):
        self.tipo = tipo

    def descripcion (self):
        return f"Este vehiculo es de tipo {self.tipo}"
    
class Moto (Vehiculo):
    def __init__(self, tipo, marca):
        super(). ___init__(tipo)
        self.marca = marca

moto1 =Moto("motocicleta", "ducatTi")
print (moto1.descripcion())
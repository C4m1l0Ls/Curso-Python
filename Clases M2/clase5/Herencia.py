class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"El vehiculo es de marca {self.marca}, modelo {self.modelo}"
    
class Auto (Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca,modelo)
        self.puertas = puertas

    def descripcion(self):
        return f"El vehiculo es de marca {self.marca}, modelo {self.modelo} y tiene {self.puertas} puertas"
    
    
        
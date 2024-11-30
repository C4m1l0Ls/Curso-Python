class persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    

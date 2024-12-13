from abc import ABC, adstractmethod


#clase abstracta = super clase "Clases"

class Clases (ABC)
    @adstractmethod
    def operacion (self):
        pass
#creacion de subclases
class ClaseA (Clases):
    def operacion(self):
        return "esta es la clase A"
    
class ClaseB (Clases):
    def operacion(self):
        return "Esta es la clase B "
    
class FabricaClases:

    @adstractmethod
    def creacionObjetos (tipoObjeto):
        if tipoObjeto == "A":
            return ClaseA()
        elif tipoObjeto == "B":
            return ClaseB()
        else:
            raise ValueError (f"la clase {tipoObjeto} no existe")

objeto1 = FabricaClases.creacionObjetos("A")
objeto2 = FabricaClases.creacionObjetos("B")


print (objeto2.popitem())
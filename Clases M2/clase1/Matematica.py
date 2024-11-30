# Metodos estaticos
class Matematicas:
    @staticmethod
    def suma(a, b):
        return a + b
    
    @staticmethod
    def resta (a,  b):
        return a - b
    
print (Matematicas.suma(10,10))
print (Matematicas.resta(10,5))

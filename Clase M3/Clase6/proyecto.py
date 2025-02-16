import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Empleado (ABC):
    nombre: str
    salario_base: float
    
    @abstractmethod
    def calcular_salario (self):
        pass
@dataclass
class Manager(Empleado):
    def calcular_salario(self):
        return self.salario_base + 5000
    
class Developer (Empleado):
    def calcular_salario(self):
        return self.salario_base + 2000

def calcular_total_salario(empleado: Empleado) -> float:
    """_summary_

    n = avance de linea en linea
    s = para saltar de funcion (metodo) en funcion (metodos)
    c = para saltar hacia la siguiente pausa 
    p variable = muestra el valor de una variable en algun momneto 
    
    """
    pdb.set_trace() # activacion del debuger
    return empleado.calcular_salario()

if __name__ == '__main__':
    manager = Manager("pascual", 30000)
    developer = Developer("jacinta", 25000)

    print(calcular_total_salario (manager))
    print(calcular_total_salario (developer))
    
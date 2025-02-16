# Uso de  breakpoint simples

class Empleado:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas

    def calculo_comision (self):
        if self.ventas > 5000:
            print(f"Empleado : {self.nombre}. Ventas: {self.ventas}. comision del 10%") # log point 
            return self.ventas *0.10
        print(f"Empleado : {self.nombre}. Ventas: {self.ventas}. comision del 5%") # log point 
        return self.ventas * 0.05
    

empleado = [
    Empleado("ana", 6000),
    Empleado("luis", 3000)
]
        
for emp in empleado:
    print (f"Empleado: {emp.nombre}. Comision: {emp. calculo_comision()}")

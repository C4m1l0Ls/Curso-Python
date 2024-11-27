from datetime import datetime
import statistics 

class Tarea:
    #funcion de inicializacion = metodo constructor
    def __init__(self, nombre, fechalimite, categoria, horasDedicadas):
        self.nombre = nombre
        self.fechalimite = fechalimite
        self.categoria = categoria
        self.horasDedicadas = horasDedicadas

#funcion para agregar una tarea

def agregarTarea(listaTareas):
    nombre = input("Ingrese el nombre de la tarea: ")
    fechalimite_str = input("ingrese la  fecha limite de la tarea (DD/MM/AAAA): ")
    try:
        fechaLimite =datetime.strptime(fechalimite_str, "%d/%m/%Y")
    except ValueError:
        print("fecha no valida.")
        return
    categoria = input("Ingrese la categoria de la tarea (Estudio, Personal, trabajo y otros): ")
    horasDedicadas_str = input("ingrese las horas dedicadas a la tarea separadas en comas: ")

    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
    except ValueError:
        print("horas no validas.")
        return
    
    #crear un objeto y lo agrega a la lista de taras
    tarea =  Tarea (nombre, fechaLimite, categoria, horasDedicadas)
    listaTareas.append(tarea)
    print("Tarea agregada exitosamente.")

def VusualizarTareas(listaTareas):
    if not listaTareas:
        print("no hay tareas resgistradas")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha limite: {tarea.fechalimite.strftime('%d/%m/%Y')}")
        print(f"Categoria: {tarea.categoria}")
        print(f"Horas dedicadas: {tarea.horasDedicadas}")

#funcion para analizar horas
def analizarHoras(listaTareas):
    if not listaTareas:
        print("no hay tareas resgistradas")
        return
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f"\nAnalisis de {tarea.nombre}")
        print(f"Promedio de horas dedicadas: {promedio}")
        print(f"Horas dedicadas maxima: {maximo}")
        print(f"Horas dedicadas minima: {minimo}")


#funcion exportar a txt
def generarInforme(listatareas):
    if not listatareas:
        print("no hay tareas resgistradas")
        return
    # crear y abrir un archivo tct para escribir un informe
    with open("informe.txt", "w") as archivo:
        #escribir el informe en el txt
        for tarea in listatareas:
            archivo.write(f"\nnombre {tarea.nombre}\n")
            archivo.write(f"fecha limite {tarea.fechalimite.strftime('%d/%m/%Y')}\n")
            archivo.write(f"categoria {tarea.categoria}\n")
            archivo.write(f"horas dedicadas {tarea.horasDedicadas}\n")
            archivo.write("\n")
    print("informe generado exitosamente.")


def menu():
    listaTareas = []
    while True:
        print("\nMenu:")
        print("1. Agregar Tarea")
        print("2. Vesualizar Tareas")
        print("3. Analizar Horas Dedicadas")
        print("4. Generar Informe")
        print("5. Salir")

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            agregarTarea(listaTareas)
        elif opcion == "2":
            VusualizarTareas(listaTareas)
        elif opcion == "3":
            analizarHoras(listaTareas)
        elif opcion == "4":
            generarInforme(listaTareas)
        elif opcion == "5":
            print("saliendo del programa")
            break
        else:
            print("Opcion invalida. Por favor, ingrese un numero entre 1 y 5.")

if __name__ == "__main__":
    menu()
           
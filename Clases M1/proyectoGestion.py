from datetime import datetime
import statistics 

class Tarea:
    #funcion de inicializacion = metodo constructor
    def __init__(self, nombre, fechaRealizacion, tipoExperimento, resultados,detalle):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultados = resultados
        self.detalle = detalle
        

#funcion para agregar una tarea

def agregarTarea(listaTareas):
    nombre = input("Ingrese el nombre del Experimento: ")
    detalle = input("Ingrese el detalle del Experimento: ")
    fechaRealizacion_str = input("ingrese la  fecha del Experimento (DD/MM/AAAA): ")
    try:
        fechaRealizacion =datetime.strptime(fechaRealizacion_str,"%d/%m/%Y")
    except ValueError:
        print("fecha no valida.")
        return
    #tipoExperimento = input("Ingrese la tipo de experimento (Quimica , Biologica , Fisica): ")
    try:
        tipoExperimento = ["Quimica", "Biologica", "Fisica"]
        if not (0 <= int(input(f"Ingrese el numero correspondiente al tipo de experimento: \n 1. Quimica\n 2. Biologica\n 3. Fisica\n ")) - 1 < 3):
            raise ValueError
    except ValueError:
        print("opcion no valida.")
        return
    resultados_str = input("ingrese  los resultados de los experimentos separadas en comas: ")

    try:
        resultados = list(map(float, resultados_str.split(",")))
    except ValueError:
        print("Valores no validos.")
        return
    
    #crear un objeto y lo agrega a la lista de tareas
    tarea =  Tarea (nombre, fechaRealizacion, tipoExperimento, resultados,detalle)
    listaTareas.append(tarea)
    print("Tarea agregada exitosamente.")

def VisualizarTareas(listaTareas):
    if not listaTareas:
        print("no hay tareas resgistradas")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha: {tarea.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Detalle: {tarea.detalle}")
        print(f"Categoria: {tarea.tipoExperimento}")
        print(f"puntajes obtenidos: {tarea.resultados}")
        print(f"puntaje maximo: {max(tarea.resultados)}")
        print(f"puntaje minimo: {min(tarea.resultados)}")

#funcion para analizar horas
def analizarHoras(listaTareas):
    if not listaTareas:
        print("no hay tareas resgistradas")
        return
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.resultados)
        maximo = max(tarea.resultados)
        minimo = min(tarea.resultados)
        print(f"\nAnalisis de {tarea.nombre}")
        print(f"Promedio Puntaje: {promedio}")
        print(f"Puntaje Maximo: {maximo}")
        print(f"Puntaje Minimo: {minimo}")


#funcion exportar a txt
def generarInforme(listatareas):
    if not listatareas:
        print("no hay tareas resgistradas")
        return
    # crear y abrir un archivo txt para escribir un informe
    with open("informe.txt", "w") as archivo:
        #escribir el informe en el txt
        for tarea in listatareas:
            archivo.write(f"\nnombre {tarea.nombre}\n")
            archivo.write(f"fecha limite {tarea.fechaRealizacion.strftime('%d/%m/%Y')}\n")
            archivo.write(f"categoria {tarea.tipoExperimento}\n")
            archivo.write(f"pntajes obtenidos {tarea.resultados}\n")
            archivo.write("\n")
    print("informe generado exitosamente.")


def menu():
    listaTareas = []
    while True:
        print("\nMenu:")
        print("1. Agregar Tarea")
        print("2. Vesualizar Tareas")
        print("3. Analizar de Puntajes")
        print("4. Generar Informe")
        print("5. Salir")

        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            agregarTarea(listaTareas)
        elif opcion == "2":
            VisualizarTareas(listaTareas)
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
           
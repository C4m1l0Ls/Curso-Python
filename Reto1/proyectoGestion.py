from datetime import datetime
import statistics 

class Tarea:
    #funcion de inicializacion = metodo constructor
    def __init__(self, nombre, fechaRealizacion, tipoExperimento, resultados,):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultados = resultados
        

#funcion para agregar una tarea

def agregarTarea(listaTareas):
    nombre = input("Ingrese el nombre del Experimento: ")
    fechaRealizacion_str = input("ingrese la  fecha del Experimento (DD/MM/AAAA): ")
    try:
        fechaLimite =datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")
    except ValueError:
        print("fecha no valida.")
        return
    tipoExperimento = input("Ingrese la tipo de experimento (Quimica , Biologica , Fisica): ")
    resultados_str = input("ingrese  los resultados de los experimentos separadas en comas: ")

    try:
        resultados = list(map(float, resultados_str.split(",")))
    except ValueError:
        print("Valores no validos.")
        return
    
    #crear un objeto y lo agrega a la lista de taras
    tarea =  Tarea (nombre, fechaLimite, tipoExperimento, resultados)
    listaTareas.append(tarea)
    print("Tarea agregada exitosamente.")

def VusualizarTareas(listaTareas):
    if not listaTareas:
        print("no hay tareas resgistradas")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha: {tarea.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Categoria: {tarea.tipoExperimento}")
        print(f"Horas dedicadas: {tarea.resultados}")

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
        print(f"Puntaje MAximo: {maximo}")
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
           
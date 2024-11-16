from datetime import datetime
import statistics


class Tarea:
    def __init__(self, nombre, fechaRealizacion, tipoExperimento, resultados, detalle):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultados = resultados
        self.detalle = detalle


def agregarTarea(listaTareas):
    nombre = input("Ingrese el nombre del Experimento: ")
    detalle = input("Ingrese el detalle del Experimento: ")
    fechaRealizacion_str = input("Ingrese la fecha del Experimento (DD/MM/AAAA): ")
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no válida.")
        return
    
    tipoExperimentos = ["Química", "Biológica", "Física"]
    try:
        opcion_tipo = int(input("Seleccione el tipo de experimento:\n1. Química\n2. Biológica\n3. Física\n"))
        if not (1 <= opcion_tipo <= 3):
            raise ValueError
        tipoExperimento = tipoExperimentos[opcion_tipo - 1]
    except ValueError:
        print("Opción no válida.")
        return

    resultados_str = input("Ingrese los resultados de los experimentos separados por comas: ")
    try:
        resultados = list(map(float, resultados_str.split(",")))
        if not resultados:
            raise ValueError
    except ValueError:
        print("Resultados no válidos. Deben ser números separados por comas.")
        return

    tarea = Tarea(nombre, fechaRealizacion, tipoExperimento, resultados, detalle)
    listaTareas.append(tarea)
    print("Tarea agregada exitosamente.")


def visualizarTareas(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha: {tarea.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Detalle: {tarea.detalle}")
        print(f"Categoría: {tarea.tipoExperimento}")
        print(f"Puntajes obtenidos: {tarea.resultados}")
        print(f"Puntaje máximo: {max(tarea.resultados)}")
        print(f"Puntaje mínimo: {min(tarea.resultados)}")


def analizarPuntajes(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.resultados)
        maximo = max(tarea.resultados)
        minimo = min(tarea.resultados)
        print(f"\nAnálisis de {tarea.nombre}")
        print(f"Promedio de Puntajes: {promedio:.2f}")
        print(f"Puntaje Máximo: {maximo}")
        print(f"Puntaje Mínimo: {minimo}")


#funcion para obtener el mejor resultado en las tareas registradas
def compararResultados(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
    
    mejorPuntaje = float ('-inf')
    tareaMP = None

    for tarea in listaTareas:
        maxPT = max(tarea.resultados)
        if maxPT > mejorPuntaje:
            mejorPuntaje = maxPT
            tareaMP = tarea
    print("\nCompracion de resultados:")

    if tareaMP:
        print(f"El mejor puntaje es {mejorPuntaje}, obtenido del experimento '{tareaMP.nombre}' "
              f"(Categoría: {tareaMP.tipoExperimento}, Fecha: {tareaMP.fechaRealizacion.strftime('%d/%m/%Y')}).")
        


def generarInforme(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
# Inicializar variables para encontrar el mejor puntaje global    
    mejorPuntaje = float('-inf')
    tareaMP = None

# Buscar el mejor puntaje global
    for tarea in listaTareas:
        maxPT = max(tarea.resultados)
        if maxPT > mejorPuntaje:
            mejorPuntaje = maxPT
        tareaMP = tarea


    with open("informe.txt", "w") as archivo:
            for tarea in listaTareas:
                archivo.write(f"\nNombre: {tarea.nombre}\n")
                archivo.write(f"Fecha: {tarea.fechaRealizacion.strftime('%d/%m/%Y')}\n")
                archivo.write(f"Categoría: {tarea.tipoExperimento}\n")
                archivo.write(f"Detalle: {tarea.detalle}\n")
                archivo.write(f"Puntajes obtenidos: {tarea.resultados}\n")
                archivo.write(f"Promedio de Puntajes: {statistics.mean(tarea.resultados):.2f}\n")
                archivo.write(f"Puntaje Máximo: {max(tarea.resultados)}\n")
                archivo.write(f"Puntaje Mínimo: {min(tarea.resultados)}\n")
                archivo.write("-" * 40 + "\n")
                archivo.write("\nExperimento con mejor puntaje:")
                archivo.write("-" * 40 + "\n")
                if maxPT:
                    archivo.write(f"El mejor puntaje es {mejorPuntaje}, obtenido en la tarea '{tareaMP.nombre}' "
                              f"(Categoría: {tareaMP.tipoExperimento}, Fecha: {tareaMP.fechaRealizacion.strftime('%d/%m/%Y')}).")
                
    print("Informe generado exitosamente en 'informe.txt'.")
    

def menu():
    listaTareas = []
    while True:
        print("\nMenú:")
        print("1. Agregar Tarea")
        print("2. Visualizar Tareas")
        print("3. Analizar Puntajes")
        print("4. Generar Informe")
        print("5. Comparar Resultados")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            agregarTarea(listaTareas)
        elif opcion == "2":
            visualizarTareas(listaTareas)
        elif opcion == "3":
            analizarPuntajes(listaTareas)
        elif opcion == "4":
            generarInforme(listaTareas)
        elif opcion == "5":
            compararResultados(listaTareas)
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")


if __name__ == "__main__":
    menu()
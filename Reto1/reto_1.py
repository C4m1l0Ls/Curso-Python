from datetime import datetime
import statistics

# Clase para representar una tarea
class Tarea:
    def __init__(self, nombre, fechaRealizacion, tipoExperimento, resultados, detalle):
        self.nombre = nombre
        self.fechaRealizacion = fechaRealizacion
        self.tipoExperimento = tipoExperimento
        self.resultados = resultados
        self.detalle = detalle

# Funcion para agregar una tarea
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
    print("Experimento Agregado Exitosamente.")

#funcion para eliminar una tarea
def eliminarTarea(listaTareas):
    if not listaTareas:
        print("No hay experimentos registrados para eliminar")
        return
    visualizarTareas(listaTareas)
    try:
        indice = int(input("\nIngrese el numero del experimento que desea eliminar: ")) - 1
        if 0 <= indice < len(listaTareas):
            eliminado = listaTareas.pop(indice)
            print(f"El experimento '{eliminado.nombre}' ha sido eliminado.")
        else:
            print("Numero invalido.")
    except ValueError:
        print("Entrada no valida. por favor ingrese un Numero.")
        return
    
#funcion para editar una tarea
def editarTarea(listaTareas):
    if not listaTareas:
        print("No hay experimentos registrados para editar")
        return
    visualizarTareas(listaTareas)
    try:
        indice = int(input("\nIngrese el nuemro del experimento que desea editar: ")) - 1
        if 0 <= indice < len(listaTareas):
            tarea = listaTareas[indice]
            print("\nOpciones de edición:")
            print("1. Editar Nombre")
            print("2. Editar Fecha")
            print("3. Editar Categoría")
            print("4. Editar Detalle")
            print("5. Editar Resultados")
            print("6. Cancelar")

            opcion = input("Ingrese el numero de la opcion que desea editar: ")
            if opcion == "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                tarea.nombre = nuevo_nombre
            elif opcion =="2":
                nueva_fecha = input("Ingrese la nueva fecha (DD/MM/AAAA): ")
                try:
                    nueva_fecha_dt= datetime.strptime(nueva_fecha, "%d/%m/%Y")
                    tarea.fechaRealizacion = nueva_fecha_dt
                except ValueError:
                    print("Fecha no valida.")
                    return
            elif opcion == "3":
                tipoExperimentos = ["Química", "Biológica", "Física"]
                try:
                    nueva_categoria = int(input("Seleccione la nueva categoría:\n1. Química\n2. Biológica\n3. Física\n"))
                    if 1 <= nueva_categoria <= 3:
                        tarea.tipoExperimento = tipoExperimentos[nueva_categoria - 1]
                    else:
                        print("Opción no valida.")
                except ValueError:
                    print("Entrada no valida.")
            elif opcion == "4":
                nuevo_detalle = input("ingrese el nuevo detalle: ")
                tarea.detalle = nuevo_detalle
            elif opcion == "5":
                nuevos_resultados_str = input("Ingrese los nuevos resultados del experimento separados por comas: ")
                try:
                    tarea.resultados = list(map(float, nuevos_resultados_str.split(",")))
                except ValueError:
                    print("Resultados no validos. No se realizaron cambios.")
            elif opcion == "6":
                print("Edicion cancelada.")
            else:
                print("Opcion no valida. por favor ingrese un Numero.")
            print("Experimento editado exitosamente.")
        else:
            print("Numero invalido.")
    except ValueError:
        print("Opcion no valida. por favor ingrese un Numero.")
            

#funcion para visualizar las tareas
def visualizarTareas(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas.")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nExperimento {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha: {tarea.fechaRealizacion.strftime('%d/%m/%Y')}")
        print(f"Detalle: {tarea.detalle}")
        print(f"Categoría: {tarea.tipoExperimento}")
        print(f"Puntajes obtenidos: {tarea.resultados}")
        print(f"Puntaje máximo: {max(tarea.resultados)}")
        print(f"Puntaje mínimo: {min(tarea.resultados)}")

#funcion para analizar los puntajes
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
        

#funcion para generar el informe
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
                

            if tareaMP and maxPT:
                  archivo.write(f"El mejor puntaje es {mejorPuntaje}, obtenido en la tarea '{tareaMP.nombre}' "
                             f"(Categoría: {tareaMP.tipoExperimento}, Fecha: {tareaMP.fechaRealizacion.strftime('%d/%m/%Y')}).")
    
    print("Informe generado exitosamente en 'informe.txt'.")
    
#funcion para el menu
def menu():
    listaTareas = []
    while True:
        print("\nMenú:")
        print("1. Agregar un Experimento")
        print("2. Visualizar los Experimentos")
        print("3. Analizar Puntajes")
        print("4. Generar Informe")
        print("5. Comparar Resultados")
        print("6. Eliminar un Experimento")
        print("7. Editar un Experimento")
        print("8. Salir")

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
            eliminarTarea(listaTareas)
        elif opcion == "7":
            editarTarea(listaTareas)
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")


if __name__ == "__main__":
    menu()
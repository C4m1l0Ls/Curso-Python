estudiantes = []
cursos = ['java', 'python']
docentes = []
horarios = []

#funcion para registrar estudiante

def matricularEstudiantes():
    nombre = input('Ingresa el Nombre del Estudiante: ')
    print('seleccione el curso: ')
    for i , curso in enumerate(cursos):
        print (f'{i+1}: {curso}')
    
    cursosSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursosSeleccionado > 0 and cursosSeleccionado <= len(cursos):
        curso = cursos[cursosSeleccionado-1]
        # Diccionarios en estudiantes
        estudiante = {'nombre':nombre, 'curso':curso}
        estudiantes.append(estudiante)
        print (f'Estudiante: {nombre} , matriculado en el curso {curso}')
    else:
        print (f'opcion del curso no valida, recuerde que solo hya {len(cursos)} cursos')

#funcion para registrar docentes

def asignarDocente():
    print('seleccionar el curso al que desea asignar el docente')
    for i, curso in enumerate(cursos):
        print (f'{i+1}: {curso}')

    cursosSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursosSeleccionado > 0 and cursosSeleccionado <= len(cursos):
        curso = cursos[cursosSeleccionado-1]
        nombreDocente = input('Ingrese el nombre del docente: ')
        # Diccionarios docentes
        docente = {'docente':nombreDocente, 'curso':curso}
        docentes.append(docente)
        print (f'docente: {nombreDocente} , asignado al curso {curso}')
    else:
        print (f'opcion del curso no valida, recuerde que solo hya {len(cursos)} cursos')

#funcion para registrar horarios a un curso

def asignarHorario():
    print('seleccionar el curso al que desea asignar el horario')
    for i, curso in enumerate(cursos):
        print (f'{i+1}: {curso}')

    cursosSeleccionado = int(input('Ingrese el numero del curso: '))
    if cursosSeleccionado > 0 and cursosSeleccionado <= len(cursos):
        curso = cursos[cursosSeleccionado-1]
        dias = input('Ingrese los dias de clase (ej: Martes y Jueves): ')
        hora = input('Ingrese la hora de clase (ej: 6pm): ')
        # Diccionarios horarios
        horario = {'curso':curso, 'dias':dias, 'hora':hora}
        horarios.append(horario)
        print (f'horario: {dias} , asignado al curso {curso} a las {hora}')
    else:
        print (f'opcion del curso no valida, recuerde que solo hay {len(cursos)} cursos')

def mostrasEstudiantes():
    if estudiantes:
        print('Lista de estudiantes matriculadas')
        for estudiante in estudiantes:
            print(f'Estudiante: {estudiante['nombre']} , Curso: {estudiante['curso']}')
    else:
        print('No hay estudiantes matriculados')

def mostrasDocentes():
    if docentes:
        print('Lista de docentes asignados')
        for docente in docentes:
            print(f'docente: {docente['docente']} , Curso: {docente['curso']}')
    else:
        print('No hay docentes asignados')

def mostrasHorarios():
    if horarios:
        print('\nLista de docentes asignados')
        for horario in horarios:
            print(f'Curso: {horario['curso']} , Dias: {horario['dias']} , Hora: {horario['hora']}')
    else:
        print('No hay horarios asignados')

while True:
    print('\n Sistema de matricula DEv Senior')
    print('1. MAtricular estudiante')
    print('2. Asignar docente a un curso')
    print('3. Asignar horario a un curso')
    print('4. Mostrar  lista de estudiantes matriculados')
    print('5. Mostrar  lista de docentes asignados')
    print('6. Mostrar  lista de horarios de los cursos')
    print('7. Salir')

    opcion = int(input('digite una opcion: '))

    if opcion == 1:
        matricularEstudiantes()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostrasEstudiantes()
    elif opcion == 5:
        mostrasDocentes()
    elif opcion == 6:
        mostrasHorarios()
    elif opcion == 7:
        print('gracias por usar el sistema de matricula dev senior')
        break
    else:
        print('Opción inválida. Por favor, ingrese un numero entre 1 y 7.')
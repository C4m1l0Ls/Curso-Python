#los diccionarios tiene un ID y un valor

conceptosProgramacion = {'POO': 'Programación orientada a objetos', 
                         'IDE': 'Entrono de Desarrollo Integrado', 
                         'DBMS': 'Sistema de gestion de bases de datos',}

print(conceptosProgramacion) #imprime todo el diccionario

print (len(conceptosProgramacion)) #imprime la longitud del diccionario

print (type(conceptosProgramacion)) #imprime el tipo de variable (conceptosProgramacion)

print (conceptosProgramacion['POO']) #imprime el valor de la clave 'POO'

print (conceptosProgramacion.get ('IDE')) #imprime el valor de la clave 'IDE'

print (conceptosProgramacion.keys()) #imprime las claves del diccionario

conceptosProgramacion['DBMS'] = 'Database Management System' #modifica el valor de la clave 'DBMS'
print(conceptosProgramacion)

for key , value in conceptosProgramacion.items(): #imprime las claves del diccionario
    print(key, value)





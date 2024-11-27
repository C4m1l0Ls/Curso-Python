#igual  que las listas pero no tienen posisciones no se puede organizar ni agregar elementos ni eliminar

lenguajes = {"python", "java", "JS"}
print(lenguajes)

print(type(lenguajes))  #imprime el tipo de variable (lenguajes)

print (len(lenguajes)) #imprime la longitud del set

print ('go' in lenguajes) #imprime si el elemento esta en el set

lenguajes.add ('go') #agrega un elemento al set
print(lenguajes)

for lenguaje in lenguajes:
    print(lenguaje) #imprime los elementos del set en vertical

lenguajes.remove('go') #elimina un elemento del set con el literal de informacion
print(lenguajes)

lenguajes.discard('go') #elimina un elemento del set con el literal de informacion
print(lenguajes)

lenguajes.clear() #limpia el set

paises = ('colombia', 'venezuela', 'mexico', 'ecuador')

print(type(paises)) #imprime el tipo de variable (paises)

print (len(paises)) #imprime la longitud de la tupla

print (paises[2]) #imprime elemento de la tupla

print (paises[-1]) #imprime el ultimo elemento

for pais in paises:
    print(pais) #imprime los elementos de la tupla en vertical

paisesLista = list(paises) #convierte la tupla en una lista para poder modificarla
print(paisesLista)

paises = tuple(paisesLista) #convierte la lista en una tupla
print(paises)

del paises #elimina la tupla


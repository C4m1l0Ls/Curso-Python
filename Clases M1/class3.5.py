# Condicionales anidados 

edad = 23
nacionalidad = "colombiana"

if edad >= 18: 
    if nacionalidad == "colombiana":
        print ("puede votar")
    else:
        print ("no puede votar")
else:
    print ("no puedes votar")

# bucle for
for i in range (0,10,2):
    print (i)


for i in range(10):
    dato = int (input("Ingresa Numero: "))

    if dato == 0:
        break
    elif dato == 1:
        continue
    elif dato == 2:
        pass
    print (i)
else:
    print (i)
    

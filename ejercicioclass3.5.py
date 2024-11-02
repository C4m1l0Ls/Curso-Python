import random

num = random.randint(0, 10)
vidas = 3 

while vidas > 0:
    intento = int(input("Intenta un numero entre 0 y 10: "))
    if intento == num:
        print("Felicidades, has acertado")
        break
    elif intento < num:
        print("El numero es mayor")
        vidas -= 1
    else:
        print("El numero es menor")
        vidas -= 1
    if vidas == 0:
        print("Perdiste, el numero era: ", num)
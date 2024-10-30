

# ejercicio 1 

    
inputusuario = input ("ingrese el primer numero")
num1 = float (inputusuario)
num2 = float (input ("ingrese el segundo numero"))
isnumeric = inputusuario.isnumeric()
isfloat = is_float(inputusuario)

def is_float (value):
    try:
        float (value)
        return True
    except ValueError:
        return False

if not isfloat  :
    inputusuario ("el numero no es valido")
    
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

print ("suma", suma)
print (f"suma: {suma}")
print (f"resta: {resta}")
print (f"multiplicacion: {mult}")
print (f"division: {div}")
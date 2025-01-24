# Estructura general  de una excepcion
# 
# try:
#   #codigo
# except AlgunaExcepcion  as e:
#    #Codigo
#else:
    #Codigo
#finally:
    #codigo

# app que permirta dividir dos numeros


"""
def division_cero (nuemro1,numero2):
    try:    
        resultado = nuemro1 / numero2
        print (f"El resultado es {resultado}")
    except ZeroDivisionError as e:
        print ("la disvision entre Cero no se plograr")
        return None

"""

# mismo ejercicio explicando las excepciones multiples

"""
def division_segura():
    try:
        numerador = int(input("ingrese el numero de la division"))
        denominador = int (input("ingrese el denomiador"))
        resultado = numerador / denominador
        print (f"El resultado de la division de {numerador} entre el {denominador} es igual a : {resultado}")
    except (ZeroDivisionError, ValueError) as e:
        print (f"error {e}")

division_segura()
"""


"""
#Manejo de excepciones especificas "Execption" << No es recomendable Siempre ya que puede escondererrores>>
def abrir_archivo():
    try:
        with open ("datos.txt", "r") as archivo:
            contenido = archivo.read()
            numero = int (contenido.strip())
            print (numero)
    except Exception as e:
        print(f"se produjo un error{e}")
abrir_archivo()
"""


"""
# uso del finally

#ejercicio del division por Cero

def divison_completa():
    try:
        numero = int(input("ingrese un numero: "))
        resultado = 10 /numero
        print (f"El resultado es {resultado}")

    except ValueError as e:
        print (f"Error {e}")
    except ZeroDivisionError as e:
        print (f"Error: {e}")

    else: 
        print (f"El resultado es {resultado}")

    finally: 
        print("La operacion finalizo...")
divison_completa()
"""


#app  que permite procesar pedidos
#validar que el codigo sea alfanumerico
#validar que la cantida sea mayor que cero

"""
def procesar_pedidios():
    try:

        codigo_prducto = input ("ingrese el codigo del producto")
        cantidad = int(input("ingrese la cantidad del producto"))
        #validar que el codigo sea alfanumerico
        if not codigo_prducto.isalnum():
            raise ValueError("El codigo del producto debe ser alfa numerico")
        
        #validar que la cantidad sea mayor que cero
        if  cantidad <=0:
            raise ValueError (" la cantidad debe ser mayor a cero")
        
        precio_unitario = 50
        total = precio_unitario * cantidad

    except ValueError as e:
        print (f"erro al procesar el pedidio {e}")
    else:
        print (f"total a pagar {total}")
    finally:
        print ('operacion finalizada')

procesar_pedidios()
    """

# Excepciones personalizadas 

class ErrorDePago(Exception):
    pass

class PasarelaDepago():

    @staticmethod
    def procecsar_pago(numero_tarjeta, monto):
        if not numero_tarjeta.startswith("4"):
            raise ErrorDePago ("El nuemro de la tarjeta no es valido")
        if monto <= 0:
            raise ErrorDePago ("El monto debe ser mayo a 0")
        return f"pagode $ {monto} fue procesado con exioto"

def procesar_pago_cliente (nombre_cliente, numero_tarjeta, monto):
    try:
            print (f"iniciando el ptroceso de pago para {nombre_cliente}")
            resultado = PasarelaDepago.procecsar_pago(numero_tarjeta, monto)
    except ErrorDePago as e:
            print(f"Error al procesar el pago {e}")
    except Exception as e:
            print (f"Se produjo un error inesperado {e}")
    else:
            print (resultado)
    finally:
            print ("Registro finalizado")

if __name__=="__main__":
    procesar_pago_cliente("Jose", "1234", 99.80)
    procesar_pago_cliente("luis", "12345", 100)
    procesar_pago_cliente("Carolina","456789", 0)
    
from abc import ABC, abstractclassmethod
from datetime import datetime


class Persona (ABC):
    def ___init___(self, nombre, contacto, direccion ):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion


        @abstractclassmethod
        def mostrar_informacion (self):
            pass

class Mascota(ABC):
    def ___init__ (self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.historial_citas =[]

    @abstractclassmethod
    def agrega_historial (self, detalles_servicio):
        pass
class Cita(ABC):
    def __init__(self, fecha, hora, servicio ,veterianario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterianario

        @abstractclassmethod
        def actualizar (self, **kwargs):
            pass
#Definicion de las Subclases
class Cliente (Persona):
    def ___init___(self, nombre, contacto, direccion):
        super().___init___(nombre, contacto, direccion)
        self.mascotas =[]

    def agregar_mascota (self, mascota):
        self.mascotas.append(mascota)

    def mostrar_informacion(self):
        return f"cliente {self.nombre}, Contacto {self.contacto}, Direccion: {self.direccion}"

class RegistroMascota(Mascota):
    def Agregar_al_historial(self, detalle_servicio):
        self.historial_citas.append(detalle_servicio)

    def obtener_historial(self):
        return self.historial_citas
    
class CitaMascota(Cita):
    def actualizar (self, **kwargs):
        for clave, valor in kwargs.intems():
            if hasattr (self, clave):
                setattr(self, clave, valor)


class SistemaVeterinaria:
    def __init__(self):
        self.clientes = []

    def registrar_clientes(self):
        try:
            nombre = input ("Ingrese el nombre del cliente").strip()
            contacto = input("Ingrese el contacto: ").strip()
            direccion = input ("Ingrese la direccion: ").strip()

            if not nombre or not contacto or not direccion:
                raise ValueError("todos los campos son obligatorios")
            
            cliente = Cliente (nombre, contacto, direccion)
            self.clientes.append(Cliente)
            print("Cliente registrado con exito")
        except ValueError as e:
            print(f"error: {e}")

    def registrar_mascota(self):
        try:
            nombre_cliente = input("Ingrese el nombre del cliente al que asociar la mascota: ").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError ("Cliente no encontrado")
            
            nombre_mascota = input("ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie: ").strip()
            raza = input ("ingrese la raza: ").strip()
            edad = int(input("Ingrese la edad: ").strip())

            if not nombre_mascota or not especie or not raza or edad <= 0:
                raise ValueError ("detalles de la mascota invalidos")
            
            mascota = RegistroMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print ("!mascota registrada con exito!")

        except ValueError as e:
            print(f"error {e}")

    def pogramar_cita(self):
        try:
            nombre_cliente = ("ingrese el nombre del cliente al que asociar la mascota: ").strip()
            nombre_mascota = input("Ingrese el nombre e la mascota: ").strip()

            cliente = next ((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError ("Cliente no encotrado")
            
            mascota = next ((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError ("mascota no encontrada")
            
            fecha = input("Ingrese la fecha (AAAA-MM-DD: )").strip()
            hora = input ("Ingrese la hora (HH:MM): ").strip()
            servicio = input("Ingrese el servicio (consulta, vacunacion, ect): ").strip()
            veterinario = input("Ingrese el nombre del veterinario: ").strip()

            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")

            if not servicio or not veterinario:
                raise ValueError ("Detalles de la cita invalidos")
            
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_al_historial(cita)
            print ("Cita programada con exito")
                    

        except ValueError as e:
            print(f"error {e}")

    def actualizar_cita(self):
            try:
                nombre_cliente = ("ingrese el nombre del cliente al que asociar la mascota: ").strip()
                nombre_mascota = input("Ingrese el nombre e la mascota: ").strip()

                cliente = next ((c for c in self.clientes if c.nombre == nombre_cliente), None)
                if not cliente:
                    raise ValueError ("Cliente no encotrado")
            
                mascota = next ((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
                if not mascota:
                    raise ValueError ("mascota no encontrada")
            
                if not mascota.historial_citas:
                    raise ValueError ("No hay citas registradas para esta mascota")
            
                print("citas disponibles para actualizar")
                for i, cita in enumerate(mascota.historial_cita):
                    print (f"{i+1}:Fecha: {cita.fecha}. Hora: {cita.hora}. Servicio {cita.servicio}. Veterinario: {cita.veterinario}")

                indice = int (input("seleccione el numero de la cita para actualizar: ").strip()) -1
                if indice < 0 or indice >= len(mascota.historial_citas):
                    raise ValueError ("selleccion invalida")
            
                cita = mascota.histarial_citas[indice]

                print ("Deje en blanco los campos que no desea actualizar")
                nueva_fecha = input("Nueva fecha (AAAA-MM-DD): ").strip()
                nueva_hora = input("Nueva hora (HH:MM): ").strip()
                nuevo_servicio = input("Nuevo servicio: ").strip()
                nuevo_veterianario = input("Nuevo veterianario: ").strip()

                if nueva_fecha:
                    datetime.strptime(nueva_fecha, "%Y-%m-%d")
                    cita.actualizar (fecha = nueva_fecha)
                if nueva_hora:
                    datetime.strptime (nueva_hora, "%H:%M")
                    cita.actualizar_hora(hora = nueva_hora)
                if nuevo_servicio:
                    cita.actualizar (servicio = nuevo_servicio)
                if nuevo_veterianario:
                    cita.actualizar (veterinario = nuevo_veterianario)

                print ("Cita actualizada con exito")

            except ValueError as e:
                print(f"error {e}")

    def consultar_historial(self):
        try:
            nombre_cliente = input("ingrese el nombre del cliente: ").strip()
            nombre_mascota = input ("Ingrese el nombre de la mascota").strip()

            cliente = next ((c for c in self.clientes if c.nombre == nombre_cliente), None)
            if not cliente:
                raise ValueError ("Cliente no encotrado")
            mascota = next ((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError ("mascota no encontrada")
            historial = mascota.obtener_historial()
            if not historial:
                print("No hay historial disponible para esta mascota")
            else:
                for entrada in historial:
                    print (f"fehca:  {entrada.fecha}. Hora: {entrada.hora}. Servicio: {entrada.servicio}. Veterianrio {entrada.veterinario}")

        except ValueError as e:
                print(f"error {e}")


    def iniciar (self):
        while True:
            print ("\nSistema de Gastion Veterinaria")
            print ("1. registrar Cliente")
            print ("2. Registrar Mascota")
            print ("3. Programar Cita")
            print ("4. Actualizar Cita")
            print ("5. consultal Historial")
            print ("6. Salir")

            opcion = input ("ingrese su opcion: ").strip()
            if opcion =="1":
                self.registra_cliente()
            elif opcion == "2":
                self.registra_mascota()
            elif opcion == "3":
                self.programar_cita
            elif opcion =="4":
                self.actualizar_cita
            elif opcion == "5":
                self.consultar_historial()
            elif opcion =="6":
                print("Saliendo del programa")
                break
            else:
                print ("opcion invalida, porfa intente de nuevo.")


if __name__ == "__main__":
    sistema = SistemaVeterinaria()
    sistema.iniciar()
            
            


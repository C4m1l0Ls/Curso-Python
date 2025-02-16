class Reserva:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha

reservas = [
    Reserva("juan", None),
    Reserva("carolina", "2025-01-25")
    ]

for reserva in reservas:
    if not reserva.fecha:
        print (f" error Fecha no asiganda para el cliente {reserva.cliente}")


        


        
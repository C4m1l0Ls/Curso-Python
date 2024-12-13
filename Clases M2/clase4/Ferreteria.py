import threading
from abc import ABC, abstractmethod

#patron singleton 

class SistemaFacturacion:
    _instacia = None
    _lock = threading.Lock

    def __new__(cls, *args, **kwargs):
        
        if not cls._instacia:
            cls._instacia = super(SistemaFacturacion, cls).__new__(cls)
            cls._instacia._inicializacionHistorico()
        return cls._instacia
        
        #opcional
        """
        with cls._lock:
            if cls._instacia is None
                cls._instacia = super (SistemaFacturacion, cls).__new__(cls)
                cls._instacia._inicializacionHistorico()
            return cls._instacia  """
        
    def _inicializacionHistorico(self):
        self.historial = []
        print ("Sistema de facturacion incializacion")
    
    def resgistrarOperacion (self, operacion):
        self.historial.append(operacion)
        print (f"La operacion fue resgistrada: {operacion}")

#clase Adstracta = Superclase

class ProcesoNegocio (ABC):

    @abstractmethod

    def ejecutar (self):
        pass

class ProcesarPedido (ProcesoNegocio):

    def ejecutar(self):
        print ("procesando pedido...")
        return "pedido procesado"

class ProcesarFactura(ProcesoNegocio):

    def ejecutar(self):
        print ("Procesando Factura")
        return "Factura procesada"
            
#crear la fabicra (patron Factory)

class FabicraProcesosNegocio:
    @staticmethod
    def crearProceso (tipoProceso):
        if tipoProceso == "pedido":
            return ProcesarPedido()
        elif tipoProceso == "factura":
            return ProcesarFactura()
        else:
            raise ValueError (f" El proceso {tipoProceso} no existe")
        
if __name__ == "__main__":

    sistema_facturacion = SistemaFacturacion()

    proceso1 = FabicraProcesosNegocio.crearProceso("pedido")
    proceso2 = FabicraProcesosNegocio.crearProceso("factura")

    resultadoPedido1 = proceso1.ejecutar()
    sistema_facturacion.resgistrarOperacion(resultadoPedido1)

    resultadoPedido2 = proceso2.ejecutar()

    sistema_facturacion.resgistrarOperacion(resultadoPedido2)

    print ("\n*** Historico de procesos de negocios***\n")
    for operacion in sistema_facturacion.historial:
        print(f"Transacción: {operacion}")
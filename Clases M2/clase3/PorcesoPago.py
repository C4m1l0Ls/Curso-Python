#interfarces en python

from abc import ABC, abstractmethod 

class ProcesoPago (ABC):

    @abstractmethod
    def procesoPago(self,cantidad: float) -> None:
        pass
    
    @abstractmethod
    def reembosoPAgo(self, transaccionId: str) -> None:
        pass

class Paypal(ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print (f"Procesando Pago por $ {cantidad} por Paypal")

    def reembosoPAgo(self, transaccionId: str)-> None:
        print (f"reembolso ID ransaccion numero {transaccionId}")

class Stripe (ProcesoPago):
    def procesoPago(self, cantidad: float) -> None:
        print (f"Procesando Pago por $ {cantidad} por Stripe")

    def reembosoPAgo(self, transaccionId: str)-> None:
        print (f"reembolso ID ransaccion numero {transaccionId}")
    
if __name__ == "__main__":
    procesoPaypal = Paypal
    procesoStripe = Stripe

    procesoPaypal.procesoPago(500.0)
    procesoPaypal.reembosoPAgo("SDFE4845564Xe")

    procesoStripe.procesoPago(1000.0)
    procesoStripe.reembosoPAgo("SDFE484457864Xde")



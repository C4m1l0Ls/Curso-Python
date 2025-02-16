import logging
from dataclasses import dataclass , field

"""
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

logging.debug ("este mensaje es del DEBUG")
logging.info ("este mensaje es del INFO")
logging.warning("este mensaje es del WARNING")
logging.error ("Este mensaje es para el ERROR ")
logging.critical ("Este mensaje es del Critico")
"""


# App que permite llevar seguimiento de compras / fallos en este tipo de transaccion
#Esta app, registrara ;a cantidad de productos comprados, confrimacnion de compra y error en estas trancacciones

logging.basicConfig(
    dlevel=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='registro.log',
    filemode='a'

    )
@dataclass
class Producto:
    nombre : str
    precio : float
    cantidad : int
    
    def comprar (self, cantidad: int):
        if cantidad > self.cantidad:
            logging.error(f"Error: No hay sufuciente cantidad del producto  {self.nombre}. El stock disponible es de {self.cantidad}")
            raise ValueError (f"Error: No hay cantidad suficeinte del producto {self.nombre} el stock disponible es de {self.cantidad} ")
        else:
            self.cantidad -= cantidad
            logging.info (f" la compra fue exitosa, el stock restante es {self.cantidad}")
            return self.precio * cantidad
        
@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)

    def agregar_producto(self, producto : Producto):
        self.productos.append(producto)
        logging.debug (f"El {producto.nombre} fue agregado con exito. El precio es de {producto.precio} - cantidad: {producto.cantidad} unidades en stock")

    def realizar_compra (self, nombre_producto: str, cantidad : int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None)
        if producto
            try:
                total = producto.comprar(cantidad)
                logging.info (f"Compra realizada: {cantidad} unidades de de {nombre_producto} por un total de $ {total}")
                return total
            except ValueError as e:
                logging.error(f"Error al efectuar la compra: {e}")
            else:
                logging.warning (f"Producto fuera de stock")

if __name__ == "__main__":
    tienda = Tienda()
    
    inventario_portatil = Producto(nombre="Portatíl", precio=1000, cantidad=10 )
    tienda.agregar_producto(inventario_portatil)
    tienda.realizar_compra("Portatíl", 4)
    
    inventario_teclado = Producto(nombre="Teclado", precio=50, cantidad=5 )
    tienda.agregar_producto(inventario_teclado)
    tienda.realizar_compra("Teclado", 10)
            
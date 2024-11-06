#codificacion camel case 
# 1.5 float 35 int johan manuel str 
ventasTotales = 0.0

#solicitar el numero de productos
numProductos = int(input('Ingrese el numero de productos a gestionar: '))

#listas para almacenar la informacion
nombres = []
precios = []
cantidades = []

print('Ingreso inicial de productos a la tienda: ')
for i in range(numProductos):
    print(f'Producto {i+1}: ')
    nombre = input('Ingrese el nombre del producto: ').lower()
    nombres.append(nombre)
    precio = float(input('Digite el precio del producto: '))
    precios.append(precio)
    cantidad = int(input('Digite el cantidad del producto: '))
    cantidades.append(cantidad)
    
#ciclo principal menu
while True:
    print('\n ---MENU DE GESTION DROGUERIA---')
    print('1. Vender Producto')
    print('2. Mostrar Inventario')
    print('3. Mostrar Ventas Totales')
    print('4. Salir')
    
    
    opcion = int(input('Ingrese una opcion: '))
    
    if opcion == 1:
        print('\nVender Producto')
        nombreVenta = input('Ingrese el nombre del producto a vender: ').lower()
        cantidadVender = int(input('Ingrese la cantidad a vender: '))
        productoEncontrado = False
        
        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado = True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTotales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f'Venta realizada. total de esta venta ${totalVenta:.2f}')
                    print(f'Quedan { cantidades[i]} unidades de {nombres[i]} en el inventario')
                else:
                    print(f'cantidad insuficiente en inventario. ya que en stock solo tenemos {cantidades[i]}')
                break
            
        if not productoEncontrado:
            print('Producto no encontrado en el inventario')
           
                    
    
    elif opcion == 2:
        print('\nInventario de Productos')
        for i in range(len(nombres)):
            print(f'Producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]:.2f}, Cantidad: {cantidades[i]}')
            
        
    elif opcion == 3:
         print(f'\nVentas totales acumuladas: ${ventasTotales:.2f}')
         
    elif opcion == 4:
        print('gracias por usar el sistema de gestion drogueria dev senior')
        break
    
    else:
            
         print('opcion invalida. ingresar entre (1-4)')
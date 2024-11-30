ventasTolales = 0.0

#solicitar el nuemro de productos
numProsuctos = int(input("ingrese el numero de productos: "))

#listas para almacenar la informacion
nombres = []
precios = []
cantidades = []

print("ingreso incial de productos a la tienda: ")
for i in range(numProsuctos):
    print(f"producto {i+1}: ")
    nombre = input("ingrese el nombre del producto: ").lower()
    nombres.append(nombre)
    precio = float(input("ingrese el precio del producto: "))
    precios.append(precio)
    cantidad = int(input("ingrese la cantidad del producto: "))
    cantidades.append(cantidad)
# ciclo principal menu
while True:
    print("\n ----- MENU DROGRERIA ------")
    print("1. Vender producto")
    print("2. Mostrar inventario")
    print("3. Mostrar ventas totales")
    print("4. Salir")

    opcion = int(input ("ingrese una opcion: "))
    if opcion == 1:
        print("\nVender Producto")
        nombreVenta = input("ingrese el nombre del producto a vender: ").lower()
        cantidadVender = int(input("ingrese la cantidad a vender: "))
        productoEncontrado = False
        for i in range(len(nombres)):
            if nombres[i] == nombreVenta:
                productoEncontrado - True
                if cantidadVender <= cantidades[i]:
                    totalVenta = cantidadVender * precios[i]
                    ventasTolales += totalVenta
                    cantidades[i] -= cantidadVender
                    print(f"venta realiazada, el total de la venta es $: {totalVenta: .2f}")
                    print(f"quedan {cantidades[i]} unidades de {nombres[i]} en el inventario")
                else:
                    print(f"no hay suficientes unidades de {nombres[i]}")
                break
        if not productoEncontrado:
            print ("producto no encontrado")
    elif opcion == 2:
        print("\nInventario de Productos")
        for  i in range(len(nombres)):
            print(f"producto {i+1}: {nombres[i].capitalize()}, Precio: ${precios[i]: .2f}, Cantidad: {cantidades[i]}")
    elif opcion == 3:
        print(f"\nVentas totales: $, {ventasTolales:.2f}")
    elif opcion == 4:
        print("Saliendo del programa")
        
    else:
        print("Opción inválida. Por favor, ingrese un numero entre 1 y 4.")
        break



                

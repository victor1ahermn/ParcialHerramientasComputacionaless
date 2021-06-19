# Parcial herramienras computacionales
# Punto 1

# Pareja:
# Isabella Victoria Henríquez, cód. 8961991
# Manuel Córtes González, cód. 8962732

productos_disponibles = {"001" : "gaseosa",
                         "002" : "agua",
                         "003" : "rebanada de pastel",
                         "004" : "paquete de papas",
                         "005" : "paquete de gomitas"}

def calcular_valor(productos_disponibles):
    MENSAJE_INICIO = "Bienvenido al sistema de caja de" \
                     "la Universidad Javeriana"

    print(MENSAJE_INICIO)

    cedulaCliente = int(input("Digite la cédula del cliente: "))
    rolCliente = input("Digite el rol del cliente: profesor o estudiante ")

    codigoProducto = input("Inserte código del producto: ")
    totalConDescuento = 0
    productosALlevar = []

    while codigoProducto != "":

        if codigoProducto not in productos_disponibles:

            print("Lo sentimos, ese producto no está disponible")

        else:
            productosALlevar.append(codigoProducto)

            cantidadUnidades = int(input("Unidades a llevar del producto: "))
            precioProducto = int(input("Precio de la unidad: "))
            subTotal = 0
            subTotalProducto = cantidadUnidades * precioProducto

            if rolCliente == "profesor":

                descuento = (subTotalProducto / 100)* 20
                subTotalProducto -= descuento
                subTotal += subTotalProducto

            elif rolCliente == "estudiante":

                descuento = (subTotalProducto / 100) * 50
                print(descuento)
                subTotalProducto -= descuento
                subTotal += subTotalProducto

        codigoProducto = input("Inserte código del producto: ")
        totalConDescuento += subTotal

    print("El", rolCliente, "con cédula:", cedulaCliente,
          "debe pagar", "$" + str(totalConDescuento),
          "por el/los producto/s:")

    for i in range(len(productosALlevar)):
        print(productosALlevar[i], end = " ")
        print(productos_disponibles[productosALlevar[i]])

calcular_valor(productos_disponibles)

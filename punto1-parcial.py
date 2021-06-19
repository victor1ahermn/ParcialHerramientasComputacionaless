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

# Diccionario de productos disponibles. Claves: código producto,
# Valores: nombre producto.

def calcular_valor(productos_disponibles):

    MENSAJE_INICIO = "Bienvenido al sistema de caja de" \
                     "la Universidad Javeriana" # Constante

    print(MENSAJE_INICIO)

    cedulaCliente = int(input("Digite la cédula del cliente: ")) # Cédula
    rolCliente = input("Digite el rol del cliente: profesor o estudiante ")
    # Rol: profesor o estudiante

    codigoProducto = input("Inserte código del producto: ")
    totalConDescuento = 0 # Valor total a pagar.
    productosALlevar = [] # Lista para guardar los códigos de los productos
                          # a llevar.

    while codigoProducto != "": # Cuando se pulse tecla ENTER, el programa
                                # procede a mostar el cálculo.

        if codigoProducto not in productos_disponibles:

            # Verificación disponiblidad

            print("Lo sentimos, ese producto no está disponible")

        else:
            productosALlevar.append(codigoProducto)

            cantidadUnidades = int(input("Unidades a llevar del producto: "))
            precioProducto = int(input("Precio de la unidad: "))
            subTotal = 0 # Sumatoria de precios por productos y sus cantidades
            subTotalProducto = cantidadUnidades * precioProducto

            if rolCliente == "profesor": # Rol profesor recibe un 20% menos

                descuento = (subTotalProducto / 100)* 20
                subTotalProducto -= descuento
                subTotal += subTotalProducto

            elif rolCliente == "estudiante":
                # Rol estudiante recibe un 50% menos

                descuento = (subTotalProducto / 100) * 50
                print(descuento)
                subTotalProducto -= descuento
                subTotal += subTotalProducto

        totalConDescuento += subTotal # Sumatoria de el precio por producto
                                      # y sus cantidades al total a pagar.
        codigoProducto = input("Inserte código del producto: ")
        

    print("El", rolCliente, "con cédula:", cedulaCliente,
          "debe pagar", "$" + str(totalConDescuento),
          "por el/los producto/s:")

    for i in range(len(productosALlevar)): # Imprime lista de productos con su
                                           # código.
        print(productosALlevar[i], end = " ")
        print(productos_disponibles[productosALlevar[i]])

calcular_valor(productos_disponibles) #Inialización del programa

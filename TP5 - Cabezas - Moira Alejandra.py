# Cabezas Moira Alejandra

#inicializo las listas


Lista_codigo = []
Lista_nombre = []
Lista_stock = []
Lista_cantidad = []
Lista_precio = []

#procesamiento

print ("----- MENU DE OPCIONES ----- \n 1. Registrar un producto nuevo\n 2. Borrar un producto\n 3. Mostrar productos\n 4. Hacer una venta\n 5. Salir")
op = int(input("\n Ingrese el numero de la operación que desea realizar: "))

while(op != 5):
    if(op>=1 and op<5):
        if(op==1):
            ban = 0   # bandera para identificar posibles errores
            
            print("\n----- REGISTRAR UN PRODUCTO NUEVO -----")
            cod = int(input(" Codigo: "))
            for codigo in Lista_codigo:
                if(codigo == cod):
                    ban = 1

            nom = input(" Nombre: ")
            for nombre in Lista_nombre:
                if(nombre == nom):
                    ban = 2

            if(ban == 0):
                Lista_codigo.append(cod)
                Lista_nombre.append(nom)
                stock = int(input(" Stock disponible: "))
                Lista_stock.append(stock)
                Lista_cantidad.append(0)
                precio = float(input(" Precio de venta: "))
                Lista_precio.append(precio)
                print("\n Producto nuevo correctamente cargado!")
                
            else:
                print("\n No es posible cargar el producto")
                if(ban == 1):
                    print(" El codigo ingresado fue cargado anteriormente")
                else:
                    print(" El nombre ingresado fue cargado anteriormente")
                    
        elif(op==2):
            print("\n----- BORRAR UN PRODUCTO -----")
            print("\n Desea borrar un producto ingresando: \n 1. Su nombre \n 2. Su codigo")
            op_Eleccion = int(input(" Ingrese la opcion elegida: "))

            indice = -1

            if(op_Eleccion == 1):
                nom = input(" Nombre: ")

                for i in range(len(Lista_nombre)):
                        if(nom == Lista_nombre[i]):
                            indice = i
            else:
                cod = int(input(" Codigo: "))
                
                for i in range(len(Lista_codigo)):
                        if(cod == Lista_codigo[i]):
                            indice = i

            if (indice == -1):
                print("\n Producto no encontrado")
            else:
                del Lista_nombre[indice]
                del Lista_codigo[indice]
                del Lista_stock[indice]
                del Lista_cantidad[indice]
                del Lista_precio[indice]
                print("\n Producto borrado correctamente")
                
        elif(op==3):
            print("\n----- MOSTRAR PRODUCTOS -----")
            
            for i in range(len(Lista_nombre)):
                print("\n --------------------")
                print(f" Codigo: {Lista_codigo[i]:10}")
                print(f" Nombre: {Lista_nombre[i]:10}")
                print(f" Stock: {Lista_stock[i]:10}")
                print(f" Cantidad vendida: {Lista_cantidad[i]:10}")
                print(f" Precio de venta: {Lista_precio[i]:10}")

        else:
            print("\n----- HACER UNA VENTA -----")
            
            print(" Desea vender un producto ingresando: \n 1. Su nombre\n 2. Su codigo")
            op_Eleccion = int(input(" Ingrese la opcion elegida: "))

            indice = -1

            if(op_Eleccion == 1):
                nom = input(" Nombre: ")

                for i in range(len(Lista_nombre)):
                    if(Lista_nombre[i] == nom):
                        indice = i

            else:
                cod = int(input(" Codigo: "))

                for i in range(len(Lista_codigo)):
                    if(Lista_codigo[i] == cod):
                        indice = i

            if(indice == -1):
                print("\n Producto no encontrado")
            else:
                print("\n Producto encontrado! :D")
                cant = int(input(" Cantidad que desea vender: "))

                if(cant <= Lista_stock[indice]):
                    Lista_stock[indice] = Lista_stock[indice] - cant         # resto al stock
                    Lista_cantidad[indice] = Lista_cantidad[indice] + cant      # sumo a la cant de ventas
                    print(" Venta realizada :)")
                else:
                    print(" No hay suficiente stock")

    else:
        print("\n >>>>>>> OPCION NO VALIDA")
                    

    print ("\n\n----- MENU DE OPCIONES ----- \n 1. Registrar un producto nuevo\n 2. Borrar un producto\n 3. Mostrar productos\n 4. Hacer una venta\n 5. Salir")
    op = int(input("\n Ingrese el numero de la operación que desea realizar: "))

print("\n----- SALIR -----")



# procesamiento
# defino funciones

def CargarMat(mat,M,N):
    print("\n ----- CARGAR MATRIZ DE PRODUCCION")
    for i in range(M):
        for j in range(N):
            mat[i][j] = float(input(f"\n EQUIPO {(i+1):2} - MES {(j+1):2}: "))

def MostrarMat(mat,M,N):        # muestra toda la matriz fila x fila
    print("\n ----- PRODUCCION TOTAL")
    i = 1
    for M in mat:
        print(f"\n EQUIPO {i:2}: ",M)
        i += 1
            

def ProdMes(mat,M,N,Mes):
    if((Mes-1) <= N):
        suma = 0
        print(f"\n ----- PRODUCCION DEL MES {Mes:2}")
        for i in range(M):
            suma += mat[i][Mes-1]
            
        print(f"\n Se produjeron un total de {suma:5} litros")
        
    else:
        print("\n Mes no registrado")
        
def AgregarCol(mat,M,N):
    for i in range(M):      # agrego los datos del ultimo mes agregado
        mat[i].append(float(input(f"\n EQUIPO {i+1:2} - MES {N:2}: ")))
    
def EliminarEquipo(mat,M,N,Eq):
    if (Eq <= M):
        for i in range(N):
            
            mat[Eq-1][i] = 0
            #del mat[Eq-1][:]
        print(f"\n Los datos del equipo {Eq:2} fueron eliminados")
            
    else:
        print("\n Equipo no registrado")
    
def ProdEquipo(mat,M,N,Eq):
    if(Eq <= M):
        print(f"\n ----- PRODUCCION DEL EQUIPO {Eq:2}")
        suma = 0
        for i in range(N):
            suma += mat[Eq-1][i]
            
        print(f"\n Se produjeron un total de {suma:5} litros")
        
    else:
        print("\n Equipo no registrado")

def opciones():
    print("\n ---------- MENU ----------")
    print("1) Cargar la matriz de produccion")
    print("2) Mostrar la produccion total de un mes elegido")
    print("3) Mostrar la produccion total de un equipo")
    print("4) Agregar un nuevo mes de produccion de los equipos")
    print("5) Eliminar toda la informacion de un equipo")
    print("6) Mostrar la matriz completa, fila por fila")
    print("0) SALIR")

    op = int(input("\n Ingrese la opcion elegida: "))
    return op

def menu():
    # inicializo la matriz al iniciar el programa
    
    filas = int(input(" Cantidad de equipos: "))  # M
    columnas = int(input(" Cantidad de meses: ")) # N
    matriz = []                                   

    for i in range(filas):
        matriz.append([0]*columnas)


    op = opciones()
    
    while(op!= 0 and op <= 6 and op >= 1):
        match(op):
            case 1:
                CargarMat(matriz,filas,columnas)
            case 2:
                print("\n ----- PRODUCCION TOTAL DE UN MES ELEGIDO")
                Mes = int(input("\n Mes seleccionado: "))
                ProdMes(matriz,filas,columnas,Mes)
                
            case 3:
                print("\n ----- PRODUCCION TOTAL DE UN EQUIPO")
                Eq = int(input("\n Equipo seleccionado: "))
                ProdEquipo(matriz,filas,columnas,Eq)
                
            case 4:
                print("\n ----- AGREGAR MES DE PRODUCCION")
                columnas += 1
                AgregarCol(matriz,filas,columnas)
                
            case 5:
                print("\n ----- ELIMINAR INFORMACION DE UN EQUIPO")
                Eq = int(input("\n Equipo a eliminar: "))
                EliminarEquipo(matriz,filas,columnas,Eq)
                
            case 6:
                MostrarMat(matriz,filas,columnas)

        op = opciones()

menu()
                
                
    




# Cabezas Moira Alejandra

""" A B C D
A ----> 2 DIGITOS
B ----> 5 DIGITOS
C ----> 5 DIGITOS
D ----> 1 DIGITO

"""
# entradas

precio = float(input(" Precio del producto: "))
cod = int(input(" Codigo de barras: "))

#procesamiento

cont = 0
cont15 = 0
cont18 = 0

while(cod != 0):
    cont += 1
    
    suma = 0
    prom = 0
    
    aux = cod//10

    for i in range(5):
        dig1 = aux%10
        suma += dig1
        aux//=10

    prom = suma/5

    if(prom >= 5):
        cont15 += 1
        
    else:
        cont18 += 1
        
    
    cod = int(input(" Codigo de barras: "))

# salidas

porc15 = (cont15/cont)*100
porc18 = (cont18/cont)*100

dineroAResignar = precio*0.15*cont15 + precio*0.18*cont18

print("\n Cantidad de vasitos con 15% de descuento: ", cont15," (",porc15,"% del total)")
print(" Cantidad de vasitos con 18% de descuento: ", cont18," (",porc18,"% del total)")

print("\n Dinero que la distribuidora va a resignar: ",dineroAResignar)












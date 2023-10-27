# Cabezas Moira Alejandra

gan = float(input(" Ingrese la ganancia obtenida: "))
print("\n Resultados del test de control ")
m1 = int(input(" DIA 1: "))
m2 = int(input(" DIA 2: "))
m3 = int(input(" DIA 3: "))
m4 = int(input(" DIA 4: "))
m5 = int(input(" DIA 5: "))
prom = (float)(m1+m2+m3+m4+m5)/5

if (prom<=220):                     # [0,220] buena ---> no hay multa
    multa = 0
elif(prom>220 and prom<=450):       # (220,450] razonablemente buena ---> 5%
    multa = 0.05*gan
elif(prom>450 and prom<=675):       # (450,675] regular ---> 10%
    multa = 0.1*gan
elif(prom>675 and prom<=1120):      # (675,1120] desfavorable ---> 25%
    multa = 0.25*gan
elif(prom>1120 and prom<=1695):     # (1120,1695] muy desfavorable ---> 50%
    multa = 0.5*gan
else:                               # (1695 o más) extremadamente desfavorable ---> 75%
    multa = 0.75*gan

print("\n La multa a pagar es de $ ",multa)

            


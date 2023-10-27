# Cabezas Moira Alejandra

# calcular la potencia de una bomba (expresada en HP) para
# transportar agua a través de una tubería cilíndrica horizontal

import math

f = 0.00579     # factor de friccion de Fanning
Ro = 1000       # densidad del agua
Vz = 1.38       # velocidad media
L = 270         # longitud ingresada por el usuario
D = 0.0254      # diametro de la tuberia
R = D/2         # radio de la tuberia


P_P =  f*0.5*Ro*(Vz**2)*((4*L)/D)    # perdida de presion
Q = Vz* math.pi *(R**2)   # caudal de fluido

Pot = P_P * Q   # potencia de la bomba
Pot/=1000
Pot/=0.7457


print(" Perdida de presión   ---> PP = ", P_P)
print(" Caudal del fluido    ---> Q = ", Q)
print("\n\n Potencia de la bomba ---> Pot = PP * Q")
print("\n\n Potencia de la bomba ---> Pot = ", Pot," (en HP)")


# Cabezas Moira Alejandra

#entrada

print(" DATOS A INGRESAR \n Recuerde separar su/s apellido/s de su/s nombre/s con una coma! \n")
nomApe = (input(" Apellidos/s y Nombre/s (como aparecen en su DNI): "))
num = (input(" Un entero de hasta cuatro dígitos: "))

#procesamiento

nomApe = nomApe.split(",")

apellido = nomApe[0].split()
apellido = [i.capitalize() for i in apellido]

nom = nomApe[1].split()

email = ""
aux = ""

for i in nom:
    email += i[0].upper()
    
for i in apellido:
    email += i

email += num + "@unsa.edu.ar"


aux += email.split("@")[0]
contra = ""

for letra in aux:
    if(letra == 'A' or letra == 'a'):
        letra = "1"
    elif (letra == 'E' or letra == 'e'):
        letra = "2"
    elif (letra == 'I' or letra == 'i'):
        letra = "3"
    elif (letra == 'O' or letra == 'o'):
        letra = "4"
    elif (letra == 'U' or letra == 'u'):
        letra = "5"
        
    contra += letra


# salidas

print(f"\n Mail sugerido para la universidad: {email:35}")
print(f" Contraseña sugerida: {contra:20}")























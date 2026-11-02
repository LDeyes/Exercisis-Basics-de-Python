# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 02/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un numero enter positiu i determina si es primer o no.
# Especificacions d'entrada: Número enter positiu introduit per l'usuari.

# Variables
numero = int(input("Introdueix un número enter positiu: "))
# Comprovem que el número sigui positiu i major que 0 i 1
if numero == 1 or numero == 0:
    print("El número no és primer.")
# Comprovem si el número és primer
else:
    for i in range(2, numero):
        if numero % i == 0:
            print("El número" + " " + str(numero) + " no és primer.")
            break
# Si el bucle finalitza sense trobar cap divisor, el número és primer
    else:
        print("El número" + " " + str(numero) + " és primer.")
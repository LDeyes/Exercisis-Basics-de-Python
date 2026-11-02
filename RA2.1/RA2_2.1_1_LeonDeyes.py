# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Mostra si un numero és més gran o no que zero
# Especificacions d'entrada: Un numero enter donat per l'usuari
# Definim Variables
numero = int(input("Posa un numero: "))

# Comparem si es menor, igual o superior que 0 i imprimim una frase segons el resultat
if(numero < 0):
    print("És menor que zero")
elif(numero == 0):
    print("És Zero!")
else:
    print("És major que zero")
    
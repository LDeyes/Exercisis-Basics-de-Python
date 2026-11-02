# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 02/11/2026
# Versió: 1.0
#
# Descripció: Demana a l'usuari un numero i mostra la taula de multiplicar de l'1 al 10
# Especificacions d'entrada: Numero enter de l'usuari 

# Variables
numero = int(input("Introdueix un número enter per veure la seva taula de multiplicar: "))

# Programa
for i in range(1, 11):
    resultat = numero * i
    print(f"{numero} x {i} = {resultat}")


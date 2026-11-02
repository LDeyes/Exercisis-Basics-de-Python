# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 02/11/2026
# Versió: 1.0
#
# Descripció: Troba el màxima d'una llista de numeros de l'usuari 
# Especificacions d'entrada: Nombres enters introduïts per l'usuari.

# Variables
entrada = (input("Introdueix un nombre: "))
numeros = [int(x) for x in entrada.split()
           
if len(numeros) == 0:
    print("No s'han introduït nombres.")
    
else:
    max_num = max(numeros)
    print("El nombre màxim és:", max_num)]

for num in numeros:
    if num == max_num:
            print("El nombre màxim és:", num)

print("El nombre màxim és:", max_num)
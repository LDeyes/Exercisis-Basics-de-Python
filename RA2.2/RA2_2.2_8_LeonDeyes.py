# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 02/11/2026
# Versió: 1.0
#
# Descripció: Demana una frase i compta vocals
# Especificacions d'entrada: Text introduït per l'usuari.

# Variables 
frase = input("Introdueix una frase: ")

# Inicialitzem el comptador de vocals
comptador_vocals = 0

# Recorrem cada caràcter de la frase
for car in frase:
    if car.lower() in 'aeiou':
            comptador_vocals += 1
else:
    print("El nombre de vocals a la frase és:", comptador_vocals)


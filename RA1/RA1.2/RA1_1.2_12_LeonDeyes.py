# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 30/09/2026
# Versió: 1.0
#
# Descripció: Substitueix una paraula d'una frase 
# Especificacions d'entrada: Text

# Variable
frase = input("Escriu una frase:")

paraula_sub = input("Quina paraula vols substituir?")

paraula_nova = input("Posa la paraula nova:")

frase_nova = frase.replace(paraula_sub, paraula_nova)

print(frase_nova)

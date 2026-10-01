# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 30/09/2026
# Versió: 1.0
#
# Descripció: Borra els espais en blanc d'una frase
# Especificacions d'entrada: Text amb espai al principi i final

# Variable
frase = input("Escriu una frase: ")

# Definim la longitud de frase
longitud = len(frase)

frase_nova = frase[1:longitud-1]

print(frase_nova)

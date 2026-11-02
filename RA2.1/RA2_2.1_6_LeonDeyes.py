# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Determina si una lletra introduida per l'usuari és vocal o consonant
# Especificacions d'entrada: Lletra intriduida per l'usuari
# Definim Variables
lletra = str(input("Posa una lletra: "))
vocals = "aeiou"

# Comparem si lletra coincideix amb vocals
if(lletra == vocals[0] or lletra == vocals[1] or lletra == vocals[2] or lletra == vocals[3] or lletra == vocals[4]):
    print(lletra + " " + "és una vocal")
# Si no coincideix imprimim consonant
else:
    print(lletra + " " + "és una consonant")
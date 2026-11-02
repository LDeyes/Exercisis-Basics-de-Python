# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Mostra si un numero és parell o senar
# Especificacions d'entrada: Numero enter donat per l'usuari
# Definim Variables 
numero = int(input("Posa una numero: "))
parell = numero % 2

# Si el residu del numero dividit entre 2 és 0 és parell sinó és senar i imprimim un missatge segons el resultat 
if(parell == 0):
    print("És Parell!")
else:
    print("És Senar!")
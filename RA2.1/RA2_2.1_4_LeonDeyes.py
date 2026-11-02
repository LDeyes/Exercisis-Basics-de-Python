# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Mostra Aprovat/Suspès segons una nota que dona l'usuari
# Especificacions d'entrada: Numero decimal major que 0 i menor o igual que 10

nota = float(input("Posa la nota: "))

if(nota >= 5):
    print("Has aprovat amb un" + " " + str(nota))
else:
    print("Has suspès amb un" + " " + str(nota))
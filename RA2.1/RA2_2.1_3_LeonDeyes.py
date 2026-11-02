# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Compara 3 numeros que dona l'usuari
# Especificacions d'entrada: 3 Numeros enters 
# Definim Variables
num1 = int(input("Posa un numero: "))
num2 = int(input("Posa un segon numero: "))
num3 = int(input("Posa un tercer numero: "))

# Comparem els 3 numeros segons de quin es més gran i imprimim un missatge segons el resultat
if(num1 > num2):
    if(num1 > num3):
        print(str(num1) + " " + "és el més gran!")
else:
    if(num2 > num3):
         print(str(num2) + " " + "és el més gran!")
    else:
         print(str(num3) + " " + "és el més gran!")
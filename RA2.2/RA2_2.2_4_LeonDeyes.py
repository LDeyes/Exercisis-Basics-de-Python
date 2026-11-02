# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 02/11/2026
# Versió: 1.0
#
# Descripció: Genera un número aleatori entre 1 i 100 i demana a l'usuari que endevini el número. El programa indica si el número introduït és massa alt, massa baix o correcte.
# Especificacions d'entrada: Número enter introduït per l'usuari

# Variables
import random
# Generació d'un número aleatori entre 1 i 100
numero_aleatori = random.randint(1, 100)
# Demana a l'usuari que introdueixi un número entre 1 i 100
numero = int(input("Introdueix un número entre 1 i 100: "))
# Número de intents
intents = 0

# Programa
while numero != numero_aleatori:
    intents += 1
    if numero < numero_aleatori:
        print("El número introduït és massa baix. Torna-ho a intentar.")
    else:
        print("El número introduït és massa alt. Torna-ho a intentar.")
    numero = int(input("Introdueix un número entre 1 i 100: "))
    if numero == numero_aleatori:
        print("Felicitats! Has endevinat el número" + " " + str(numero_aleatori) + " en " + str(intents) + " intents.")


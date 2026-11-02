# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 02/11/2026
# Versió: 1.0
#
# Descripció: Mostra els primers 10 termes de Fibonacci
# Especificacions d'entrada: 10 numeros enters

# Variables 
num1 = 0
num2 = 1

print("Sequència de Fibonacci")

for i in range(10):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3)
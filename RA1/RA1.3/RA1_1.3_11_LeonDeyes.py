minuts = int(input("Introdueix el nombre de minuts: "))
hores = minuts // 60
minuts_restants = minuts % 60

print("Sobren " + str(hores) + " hores i " + str(minuts_restants) + " minuts.")
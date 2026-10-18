IVA = 0.21 # Escrivim IVA en majúscules per indicar que és una constant
preu = float(input("Introdueix el preu del producte: "))
preu_amb_iva = preu + (preu * IVA)

print("El preu del producte sense IVA és: " + str(preu))
print("L'import del IVA és: " + str(preu * IVA))
print("El preu del producte amb IVA és: " + str(preu_amb_iva))

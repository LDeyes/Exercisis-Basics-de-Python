nom = input("Posa el teu nom: ")
cognom = input("Posa els teus cognoms: ")
ciutat = input("Posa la teva ciutat: ")
edat = int(input("Posa la teva edat: "))
cicle = input("Posa el teu cicle formatiu: ")
edat_futura = edat + 1
correu = nom.lower() + "." + cognom.lower() + "alumnes@.cat"
nom_complet = nom.upper() + " " + cognom.upper()

print("FITXA DE L'ALUMNE")
print("Nom Complet :" + " " + nom_complet)
print("Edat any vinent: " + str(edat_futura))
print("Ciutat: " + ciutat)
print("Cicle Formatiu: " + cicle)
print("Correu: " + correu)
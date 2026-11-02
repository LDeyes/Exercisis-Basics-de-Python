# Administració de Sistemes Informàtics en Xarxa
# Autor: Leon Clark Deyes
# Data: 26/10/2026
# Versió: 1.0
#
# Descripció: Calcula si l'usuari és major/menor segons la seva data de naixement
# Especificacions d'entrada: 3 nombres enters i la data d'avui
from datetime import date
dia = int(input("Posa el dia que vas nèixer: "))
mes = int(input("Posa el mes que vas nèixer: "))
any = int(input("Posa l'any que vas nèixer: "))
data_avui = date.today()
anys = int(data_avui.year) - any


if(anys > 18):
    print("Ets major! ")
if(anys < 18):
    print("Ets menor! ")
if(anys == 18):
    if(data_avui.month < mes):
        print("Ets menor! ")
    if(data_avui.month> mes):
        print("Ets major! ")
    if(data_avui.month == mes):
        if(data_avui.day < dia):
            print("Ets menor! ")
        if(data_avui.day > dia):
            print("Ets major! ")
        if(data_avui.day == dia):
            print("Felicitats! ")


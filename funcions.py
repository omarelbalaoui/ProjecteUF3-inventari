import os
from datetime import date

fitxers = []
lines = []
contingut_fitxer = []
contingut_total = []
inventari_total = []
inventari_cru = []
lista_cru = []
lista_total = []
nom = ""
quantitat = 0
biblioteca_total = {}
biblioteca_cru = {}

config = open("config.txt", "r")
config_vars = config.readlines()
config.close()

def parametres(num):
     return str(config_vars[num].rstrip())

def fitxers_inventari(files):
    global fitxers
    files = os.listdir(files)
    for name in files:
        if name.endswith(".txt"):
            fitxers.append(name)
    return fitxers

def nom_arxiu(fitxer):
    return fitxer.split("_")[0]

def crear_biblioteca_cru():
    global biblioteca_cru
    for line in inventari_cru:
        clau = (line[0],line[1])
        quantitat = line[2]
        if clau in biblioteca_cru:
            biblioteca_cru[clau] += quantitat
        else:
            biblioteca_cru[clau] = quantitat
    return biblioteca_cru

def crear_biblioteca_total():
    global biblioteca_total
    for line in inventari_total:
        clau = (line[0],line[1],line[2])
        quantitat = line[3]
        if clau in biblioteca_total:
            biblioteca_total[clau] += quantitat
        else:
            biblioteca_total[clau] = quantitat
    return biblioteca_total

def data_actual():
    today = date.today()
    return today.strftime("%d%m%Y")   


from funcions import *
from zipfile import ZipFile
from os import remove

error = []
noms_fitxers = []
fitxers_inventari(parametres(0).rstrip())

try:
    for file in fitxers:
        noms_fitxers.append(file)
        nom = nom_arxiu(file)
        with open(parametres(0).rstrip()+ file, "r") as f:
            contingut_fitxer = f.readlines()
            f.close()
            for line in contingut_fitxer:
                codi_article = line.split(";")[1]
                quantitat_str = line.split(";")[7].strip()
                codi_color = line.split(";")[2]  
                if quantitat_str.isdigit():  
                    quantitat = int(quantitat_str)
                    inventari_cru.append([nom, codi_article, quantitat])
                    inventari_total.append([nom, codi_article, codi_color, quantitat])
except Exception as e:
    error.append(e)
    

log = open("log.txt", "w")
log.write("Fitxers processats amb èxit: "+ "\n")
for file in noms_fitxers:
    log.write(file + "\n")
log.write("\n")
for error in error:
    log.write("Fitxers amb error: "+ "\n")
    log.write(file + ":")
    log.write(str(error) + "\n")
log.close()

for key, value in crear_biblioteca_cru().items():
    lista_cru.append([key[0],key[1],value])

for key, value in crear_biblioteca_total().items():
    #crear lista total separada por ;
    lista_total.append([key[0],key[1],key[2],value])

fitxer_cru = open(parametres(2).rstrip()+"cru.txt", "w")
for line in lista_cru: 
    fitxer_cru.write(line[0] + ";" + line[1] + ";" + str(line[2]) + "\n")
fitxer_cru.close()  
    
fitxer_total = open(parametres(2).rstrip()+"articleColor.txt", "w")
for line in lista_total:
    fitxer_total.write(line[0] + ";" + line[1] + ";" + line[2] + ";" + str(line[3]) + "\n")
fitxer_total.close()

#Comprimir fitxers de l'inventari en zip
zipObj = ZipFile(parametres(1).rstrip()+"inventari.zip", 'w')
for file in fitxers:
    try:
        zipObj.write(parametres(0).rstrip()+file)
        remove(parametres(0).rstrip()+file)
    except Exception as e:
        pass
zipObj.close()

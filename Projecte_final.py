from funcions import *

fitxers_inventari(parametres(0).rstrip())

for file in fitxers:
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

#for key, value in crear_biblioteca_cru().items():
#    print(key[0])

for key, value in crear_biblioteca_cru().items():
    lista_cru.append([key, value])

for key, value in crear_biblioteca_total().items():
    lista_total.append([key, value])


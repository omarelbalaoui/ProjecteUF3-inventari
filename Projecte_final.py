from funcions import *

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
#Guardar el error del terminal en una lista
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

#En caso de que haya algun error, envia un correo con el log.txt adjunto
if len(error) > 0:
    email = Email(parametres(4).rstrip(), parametres(5).rstrip(), parametres(6).rstrip())
    email.send_mail("Error en el programa de inventario", "Adjuntamos el log.txt con los errores encontrados", "log.txt")




for key, value in crear_biblioteca_cru().items():
    print(key)

for key, value in crear_biblioteca_cru().items():
    lista_cru.append([key, value])

for key, value in crear_biblioteca_total().items():
    lista_total.append([key, value])


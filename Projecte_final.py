from funcions import *
from zipfile import ZipFile
from os import remove
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from rich import print

error = []
noms_fitxers = []
fitxers_inventari(parametres(0).rstrip())

fitxers_exits = []
fitxers_fallits = []
for file in fitxers:
    try:
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
        fitxers_exits.append(file)

    except Exception as e:
        error.append(e)
        fitxers_fallits.append(file)
        
    
log = open("log.txt", "w")
log.write("Fitxers processats amb èxit: "+ "\n")
for line in fitxers_exits:
    log.write(line + "\n")
log.write("\n")
log.write("Fitxers fallits: "+ "\n")
for line in fitxers_fallits:
    log.write(line + "\n")
    log.write("     Error: "+ str(error) + "\n")
log.close()


for key, value in crear_biblioteca_cru().items():
    lista_cru.append([key[0],key[1],value])

for key, value in crear_biblioteca_total().items():
    lista_total.append([key[0],key[1],key[2],value])

fitxer_cru = open(parametres(2).rstrip()+"cru.txt", "w")
for line in lista_cru: 
    fitxer_cru.write(line[0] + ";" + line[1] + ";" + str(line[2]) + "\n")
fitxer_cru.close()  
    
fitxer_total = open(parametres(2).rstrip()+"articleColor.txt", "w")
for line in lista_total:
    fitxer_total.write(line[0] + ";" + line[1] + ";" + line[2] + ";" + str(line[3]) + "\n")
fitxer_total.close()

zipObj = ZipFile(parametres(1).rstrip()+"inventari.zip", 'w')
for file in fitxers:
    try:
        zipObj.write(parametres(0).rstrip()+file)
        #remove(parametres(0).rstrip()+file)
    except Exception as e:
        pass
zipObj.close()

msg = MIMEMultipart()
msg['From'] = parametres(5)
msg['To'] = parametres(7)
msg['Subject'] = "Logs de l'inventari"

nombre_archivo = "log.txt"
with open(nombre_archivo, 'r') as file:
    contenido_archivo = file.read()

cuerpo = contenido_archivo
msg.attach(MIMEText(cuerpo, 'plain'))

try:
    server = smtplib.SMTP(parametres(3).rstrip(), parametres(4).rstrip())
    server.ehlo()  
    server.starttls()  
    server.login(parametres(5), parametres(6))  
    text = msg.as_string()

    server.sendmail(parametres(5), parametres(7), text)
    server.quit()
    print("\n" + "*"*50)
    print("\n" + f'[bold green]Correu enviat correctament a {parametres(7)} el {datetime.now().strftime("%d/%m/%Y a les %H:%M:%S")}.[/bold green]')
    print("\n" + "*"*50)
except Exception as e:
    print(f'[bold red]Ha ocorregut un error en enviar el correu: [/bold red]', e)


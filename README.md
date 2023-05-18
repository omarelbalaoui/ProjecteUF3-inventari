<h1 align="center"> Projecte UF3 - Inventari de Cremalleres amb Python </h1>

<p align="center">
  <img src="https://github.com/omarelbalaoui/ProjecteUF3-inventari/assets/91249151/97c8f6d7-0fe3-4e4c-bd7e-dfd2b6562b29">
</p>

## Taula de continguts 📑
- [Descripció🔍](#descripció)
- [Requisits💻](#requisits)
- [Autors👨🏿👨🏻](#autors)


## Descripció🔍
---
Aquest projecte es tracta d'un programa que processa fitxers d'inventari de cursors en una botiga o magatzem, generant dos fitxers de resum. Un resum destaca la quantitat total de cursors per secció (cru.txt), mentre que l'altre considera també el color del cursor (articleColor.txt).

El programa també comprimeix i emmagatzema els fitxers d'inventari originals, enviant un resum per correu electrònic al responsable, indicant si el processat ha tingut èxit o ha generat errors. Si hi ha errors, es registren en un fitxer log.txt.

Les dades per a la seva operació es prenen d'un fitxer config.txt, que inclou ubicacions de fitxers, dades del servidor SMTP i informació de correu electrònic.


## Requisits💻
---

```bash
apt install python3
```
```bash
pip install rich
```

## Autors👨🏿👨🏻
---
- [Omar El Balaoui Ben Zaid](https://github.com/omarelbalaoui)
- [Andreu Gisbert Bel](https://github.com/agisbertb/)


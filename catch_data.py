#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
import json
import mysql.connector
import codecs

print("Téléchargement données")
reader = codecs.getreader("utf-8")
act = urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json')
comm = urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json')
equ = urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json')
print("Fin téléchargement données")

activite = json.load(reader(act))
commune = json.load(reader(comm))
equipement = json.load(reader(equ))
cnx = mysql.connector.connect(user='E154817E', password = 'E154817E', database='E154817E', host ='infoweb')
cursor = cnx.cursor()

print("Indexation activité")
cursor.execute("truncate table activite")
for i in activite['data'] :
    insertion = "INSERT INTO activite (ActCode, ActLib, ActNivLib, ComInsee, ComLib, EquActivitePraticable, EquActivitePratique, EquActiviteSalleSpe, EquipementId, EquNbEquIdentique) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (i.get('ActCode'), i.get('ActLib'), i.get('ActNivLib'), i.get('ComInsee'), i.get('ComLib'), i.get('EquActivitePraticable'), i.get('EquActivitePratique'), i.get('EquActiviteSalleSpe'), i.get('EquipementId'), i.get('EquNbEquIdentique'))
    cursor.execute(insertion, data)
cnx.commit()
print("Fin indexation activite")

print("Indexation commune")
cursor.execute("truncate table commune")
for i in commune['data'] :
    insertion = "INSERT INTO commune (ComLib, NbEquipements, ComInsee, InsLibelleVoie, Longitude, Latitude, InsNumeroInstall) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    data = (i.get('ComLib'), i.get('Nb_Equipements'), i.get('ComInsee'), i.get('InsLibelleVoie'), i.get('Longitude'), i.get('Latitude'), i.get('InsNumeroInstall'))
    cursor.execute(insertion, data)
cnx.commit()
print("Fin indexation commune")

print("Indexation equipement")
cursor.execute("truncate table equipement")
for i in equipement['data'] :
    insertion = "INSERT INTO equipement (GestionTypeProprietaireSecLib, EquNom, ComInsee, InsNumeroInstall, InsNom, EquGpsY, EquGpsX, EquipementId) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (i.get('GestionTypeProprietaireSecLib'), i.get('EquNom'), i.get('ComInsee'), i.get('InsNumeroInstall'), i.get('InsNom'), i.get('EquGpsY'), i.get('EquGpsX'), i.get('EquipementId'))
    cursor.execute(insertion, data)
cnx.commit()
print("Fin indexation equipement")

cnx.close()

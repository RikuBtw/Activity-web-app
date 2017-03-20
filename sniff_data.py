#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
import mysql.connector


fichier = open("leNomDuFichier.txt", "w")
fichier.write("")
fichier.close()



response1 = urllib2.urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J334/equipements_activites_table/content/?format=json')
response2 = urllib2.urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J335/installations_table/content/?format=json')
response3 = urllib2.urlopen('http://data.paysdelaloire.fr/api/publication/23440003400026_J336/equipements_table/content/?format=json')

data1 = json.load(response1)
data2 = json.load(response2)
data3 = json.load(response3)

connection = mysql.connector.connect(user="E154817E", password="E154817E", host="infoweb", database = "E154817E")

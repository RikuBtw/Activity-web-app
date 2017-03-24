#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

class SGBD:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='E154817E', password = 'E154817E', database='E154817E', host ='infoweb')
        self.cursor = self.cnx.cursor()


    # renvoie toutes les villes et les activités disponibles
    def datalist(self):
        query = ("SELECT ComLib, ActLib FROM activite")
        self.cursor.execute(query)
        resultat=[]
        for data in self.cursor:
            triplet = { data[0], data[1], data[2] }
            rData.append(triplet)
        return rData

    # à partir du nom d'une ville, renvoie toutes les activités disponibles dans la ville
    def ville_act(self,ville):
        query = ("SELECT ActLib FROM activite WHERE ComLib=%s")
        ville = (ville,)
        rActivite = []
        self.cursor.execute(query, ville)
        for (a) in self.cursor:
            paire = { a[0], a[1] }
            rActivite.append( paire )
        return rActivite

    # à partir d'une activité, renvoie toutes les villes qui permettent cette activité
    def act_ville(self,act):
        act.capitalize()
        query = ("SELECT ComLib FROM activite WHERE ActLib=%s GROUP BY ComLib")
        act = (act,)
        rVille = []
        self.cursor.execute(query, act)
        for (v) in self.cursor:
            paire = v[0]
            rVille.append( paire )
        return rVille

    # à partir d'une ville, renvoie sa latitude
    def LatitudeGPS(self, ville):
        ville.capitalize()
        query = ("SELECT Latitude FROM commune WHERE ComLib=%s GROUP BY Latitude")
        ville = (ville,)
        rVille = []
        self.cursor.execute(query, ville)
        for (a) in self.cursor:
          rVille = a[0]
        return rVille

    # à partir d'une ville, renvoie sa longitude
    def LongitudeGPS(self, ville):
        ville.capitalize()
        query = ("SELECT Longitude FROM commune WHERE ComLib=%s GROUP BY Longitude")
        ville = (ville,)
        rVille = []
        self.cursor.execute(query, ville)
        for (a) in self.cursor:
          rVille = a[0]
        return rVille

    #renvoie toutes les villes
    def villes(self):
        query = ("SELECT ComLib FROM commune GROUP BY ComLib")
        rVille = []
        self.cursor.execute(query)
        for (a) in self.cursor:
          element = {a[0]}
          rVille.append(a[0])
        return rVille

    #renvoie toutes les activités
    def activites(self):
        query = ("SELECT ActLib FROM activite GROUP BY ActLib")
        rActivite = []
        self.cursor.execute(query)
        for (a) in self.cursor:
          rActivite.append(a[0])
        return rActivite

    #renvoie toutes les activités
    def niveau(self):
        query = ("SELECT ActNivLib FROM activite GROUP BY ActNivLib")
        rNiveau = []
        self.cursor.execute(query)
        for (a) in self.cursor:
          rNiveau.append(a[0])
        return rNiveau

    # à partir d'une activité et d'un niveau, renvoie toutes les équippemts qui permettent cette activité
    def act_equ(self,act):
        act.capitalize()
        query = ("SELECT ComLib FROM activite WHERE ActLib=%s GROUP BY ComLib")
        act = (act,)
        rVille = []
        self.cursor.execute(query, act)
        for (v) in self.cursor:
            paire = v[0]
            rVille.append( paire )
        return rVille

    # à partir d'une ville et d'une activité, renvoie tous ses équipements
    def equipements_villes(self, ville, act):
        ville.capitalize()
        rEquVille = []
        ville = (ville,)
        query = ("SELECT ComInsee FROM commune WHERE %s=ComLib")
        self.cursor.execute(query, ville)
        for (a) in self.cursor:
            insee=a[0]

        act.capitalize()
        act=(act,)
        query = ("SELECT EquipementId FROM activite WHERE %s=ActLib")
        self.cursor.execute(query, act)
        for (a) in self.cursor:
            equId=a[0]

        paire = (insee, equId)
        query = ("SELECT EquNom FROM equipement WHERE ComInsee=%s AND EquipementId=%s GROUP BY EquNom")
        self.cursor.execute(query, paire)
        for (a) in self.cursor:
          rEquVille.append( a[0] )
        return rEquVille

bd = SGBD()
tmp = bd.equipements_villes("Nantes", "Basket-Ball")
print(str(tmp))

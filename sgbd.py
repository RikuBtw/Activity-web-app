#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

class SGBD:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='E154817E', password = 'E154817E', database='E154817E', host ='infoweb')
        self.cursor = self.cnx.cursor()

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

    # à partir du nom d'une ville et d'un niveau, renvoie toutes les activités disponibles dans la ville
    def ville_act(self,ville,niv):
        ville.capitalize()
        query = ("SELECT ActLib FROM activite WHERE ComLib=%s AND ActNivLib=%s GROUP BY ActLib")
        paire = (ville,niv)
        rActivite = []
        self.cursor.execute(query, paire)
        for (a) in self.cursor:
            rActivite.append( a[0] )
        return rActivite

    # à partir d'une activité et d'un niveau, renvoie toutes les villes qui permettent cette activité
    def act_ville(self,act,niv):
        act.capitalize()
        query = ("SELECT ComLib FROM activite WHERE ActLib=%s AND ActNivLib=%s GROUP BY ComLib")
        paire = (act,niv)
        rVille = []
        self.cursor.execute(query, paire)
        for (v) in self.cursor:
            rVille.append( v[0] )
        return rVille

    # à partir d'une ville, d'une activité et d'un niveau, renvoie tous ses équipements
    def equipements_villes(self, ville, act, niv):
        ville.capitalize()
        act.capitalize()
        rRecherche = []
        listeEquId = []
        paire = (ville, act)
        query = ("SELECT EquipementId FROM activite WHERE ComLib=%s AND ActLib=%s")
        self.cursor.execute(query, paire)
        for (a) in self.cursor:
            listeEquId.append(a[0])
        for (a) in listeEquId:
            paire = (a,)
            query = ("SELECT EquNom FROM equipement WHERE EquipementId=%s")
            self.cursor.execute(query, paire)
            for (a) in self.cursor:
                rRecherche.append(a[0])
        return rRecherche

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

bd = SGBD()
tmp = bd.equipements_villes("Nantes", "Basket-Ball", "Scolaire")
print(str(tmp))

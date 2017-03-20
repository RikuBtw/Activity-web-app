#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

class SGBD:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='E154817E', password = 'E154817E', database='E154817E', host ='infoweb')
        self.cursor = self.cnx.cursor()


    # renvoie toutes les villes et les activités disponibles
    def datalist(self):
        query = ("SELECT ComLib, ActLib, ActNivLib FROM activite")
        self.cursor.execute(query)
        resultat=[]
        for data in self.cursor:
            triplet = { data[0], data[1], data[2] }
            rData.append(triplet)
        return rData

    # à partir du nom d'une ville, renvoie toutes les activités et leurs niveaux disponibles dans la ville
    def ville_act(self,ville):
        query = ("SELECT ActLib, ActNivLib FROM activite WHERE ComLib=%s")
        ville = (ville,)
        rActivite = []
        self.cursor.execute(query, ville)
        for (a) in self.cursor:
            paire = { a[0], a[1] }
            rActivite.append( paire )

        return rActivite

    # à partir d'une activité, renvoie toutes les villes et leurs codes postaux qui permettent cette activité
    def act_ville(self,act):
        act.capitalize()
        query = ("SELECT ComLib, ComInsee FROM activite WHERE ActLib=%s")
        act = (act,)
        rVille = []
        self.cursor.execute(query, act)
        for (v) in self.cursor:
            paire ={v[0], v[1]}
            rVille.append( paire )
        return rVille

    # à partir d'une activité et une ville, renvoie tous les niveaux disponibles
    def act_ville_niv(self,act, ville):
        act.capitalize()
        query = ("SELECT ComLib, ComInsee FROM activite WHERE ActLib=%s AND ComLib=%s")
        actVille = (act,ville)
        rNiv = []
        self.cursor.execute(query, actVille)
        for (v) in self.cursor:
            paire ={v[0], v[1]}
            rNiv.append( paire )
        return rNiv

    # à partir d'une activité et son niveau, renvoie toutes les villes disponible
    def niveau(self,act,niv):
        niv.capitalize()
        query = ("SELECT ComLib, ComInsee FROM activite WHERE ActLib=%s AND ActNivLib=%s")
        actNiv = (act,niv)
        rNiveau = []
        self.cursor.execute(query, actNiv)
        for (a) in self.cursor:
          paire = {a[0], a[1]}
          rNiveau.append( paire )
        self.cursor.close()
        return rNiveau

    # à partir d'une ville, renvoie ses coordonnées
    def positionGPS(self, ville):
        ville.capitalize()
        query = ("SELECT Latitude, Longitude FROM commune WHERE ComLib=%s")
        ville = (ville,)
        rVille = []
        self.cursor.execute(query, ville)
        for (a) in self.cursor:
          paire = {a[0], a[1]}
          rVille.append( paire )
        self.cursor.close()
        return rVille

    def villes(self):
        query = ("SELECT ComLib FROM commune GROUP BY ComLib")
        rVille = []
        self.cursor.execute(query)
        for (a) in self.cursor:
          rVille.append( a[0] )
        self.cursor.close()
        return rVille

    def activites(self):
        query = ("SELECT ActLib FROM activite GROUP BY ActLib")
        rActivite = []
        self.cursor.execute(query)
        for (a) in self.cursor:
          element = {a[0]}
          rActivite.append( element )
        self.cursor.close()
        return rActivite

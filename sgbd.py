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
        ville=""
        activite=""
        niveau=""
        s=""
        for data in self.cursor:
            rData+= str(data)
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

s = SGBD()
print(s.niveau("Basket-Ball","Compétition national"))

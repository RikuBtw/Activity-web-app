#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

class SGBD:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='E154817E', password = 'E154817E', database='E154817E', host ='infoweb')
        self.cursor = self.cnx.cursor()
        self.latitude = self.cnx.cursor()
        self.longitude = self.cnx.cursor()

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
            if a[0]!="None":
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
            rActivite.append(a[0])
        return rActivite

    # à partir d'une activité et d'un niveau, renvoie toutes les villes qui permettent cette activité
    def act_ville(self,act,niv):
        act.capitalize()
        villes = []
        tmp = []
        query = ("SELECT ComLib FROM activite WHERE ActLib=%s AND ActNivLib=%s GROUP BY ComLib")
        paire = (act,niv)
        rVille = []
        self.cursor.execute(query, paire)
        for (a) in self.cursor:
            villes.append(a[0])
        for ville in villes:
            tmp = ville, self.PositionGPS(ville)
            rVille.append(tmp)
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
            query = ("SELECT EquNom, EquGpsX, EquGpsY FROM equipement WHERE EquipementId=%s")
            self.cursor.execute(query, paire)
            for (a) in self.cursor:
                tmp = a[1],a[2]
                tmp2= a[0],tmp
                rRecherche.append(tmp2)
        return rRecherche

    # à partir d'une ville, renvoie sa latitude et sa longitude
    def PositionGPS(self, ville):
        ville.capitalize()
        query = ("SELECT Latitude, Longitude FROM commune WHERE ComLib=%s GROUP BY Latitude")
        ville = (ville,)
        rVille = []
        self.latitude.execute(query, ville)
        for (a) in self.latitude:
          rVille = a[0],a[1]
        return rVille

#<%
#ville = []
#tmp=[]
#for a in gps:
#tmp = "lat:" + str(a[0]) + ", lng:" +str(a[1])
#ville.append(tmp)
#%>
#%end
#var ville = {{ville[0]}};

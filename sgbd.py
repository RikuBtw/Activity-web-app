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
            if a[0]!=None:
                rNiveau.append(a[0])
        return rNiveau

    # à partir du nom d'une ville et d'un niveau, renvoie toutes les activités disponibles dans la ville
    def ville_act(self,ville,niv):
        ville.capitalize()
        resultat = []
        rAct =[]
        tempResult = []
        if niv=="Non défini":
            query = ("SELECT ActLib, ActNivLib, EquipementId, ComLib, ComInsee FROM activite WHERE ComLib=%s AND ActNivLib=%s GROUP BY ActLib")
            paire = (ville,niv)
        else:
            query = ("SELECT ActLib, ActNivLib, EquipementId, ComLib, ComInsee FROM activite WHERE ComLib=%s GROUP BY ActLib")
            paire = (ville,)
        rActivite = []
        self.cursor.execute(query, paire)

        for (a) in self.cursor:
            results = a[0],a[1],a[2],a[3],a[4]
            tempResult.append(results)
        for (a) in tempResult:
            resultat = []
            NumIns = 0;
            InsLib = "";
            tmpGPS = []
            tmpEqu = []
            query2 = ("SELECT EquGpsX, EquGpsY, EquNom, InsNom, InsNumeroInstall  FROM equipement WHERE EquipementId=%s")
            paire2 = (a[2],)
            self.cursor.execute(query2, paire2)
            for (b) in self.cursor:
                tmpGPS.append(str(b[1]))
                tmpGPS.append(str(b[0]))
                tmpEqu.append(b[2])
                tmpEqu.append(b[3])
                NumIns = b[4]
            query3 = ("SELECT InsLibelleVoie FROM commune WHERE InsNumeroInstall=%s")
            paire3 = (NumIns,)
            self.cursor.execute(query3, paire3)
            for (b) in self.cursor:
                tmpEqu.append(b[0])
            tmpAct = []
            tmpAct.append(str(a[0]))
            tmpAct.append(str(a[1]))
            tmpCom = []
            tmpCom.append(str(a[3]))
            tmpCom.append(str(a[4]))
            resultat.append(tmpGPS)
            resultat.append(tmpAct)
            resultat.append(tmpCom)
            resultat.append(tmpEqu)
            rAct.append(resultat)
        return rAct

    # à partir d'une activité et d'un niveau, renvoie toutes les villes qui permettent cette activité
    def act_ville(self,act,niv):
        act.capitalize()
        resultat = []
        rVille =[]
        tempResult = []
        if niv=="Non défini":
            query = ("SELECT ActLib, ActNivLib, EquipementId, ComLib, ComInsee FROM activite WHERE ActLib=%s AND ActNivLib=%s GROUP BY ComLib")
            paire = (act,niv)
        else:
            query = ("SELECT ActLib, ActNivLib, EquipementId, ComLib, ComInsee FROM activite WHERE ActLib=%s GROUP BY ComLib")
            paire = (act,)
        rActivite = []
        self.cursor.execute(query, paire)

        for (a) in self.cursor:
            results = a[0],a[1],a[2],a[3],a[4]
            tempResult.append(results)
        for (a) in tempResult:
            resultat = []
            NumIns = 0;
            InsLib = "";
            tmpGPS = []
            tmpEqu = []
            query2 = ("SELECT EquGpsX, EquGpsY, EquNom, InsNom, InsNumeroInstall  FROM equipement WHERE EquipementId=%s")
            paire2 = (a[2],)
            self.cursor.execute(query2, paire2)
            for (b) in self.cursor:
                tmpGPS.append(str(b[1]))
                tmpGPS.append(str(b[0]))
                tmpEqu.append(b[2])
                tmpEqu.append(b[3])
                NumIns = b[4]
            query3 = ("SELECT InsLibelleVoie FROM commune WHERE InsNumeroInstall=%s")
            paire3 = (NumIns,)
            self.cursor.execute(query3, paire3)
            for (b) in self.cursor:
                tmpEqu.append(b[0])
            tmpAct = []
            tmpAct.append(str(a[0]))
            tmpAct.append(str(a[1]))
            tmpCom = []
            tmpCom.append(str(a[3]))
            tmpCom.append(str(a[4]))
            resultat.append(tmpGPS)
            resultat.append(tmpAct)
            resultat.append(tmpCom)
            resultat.append(tmpEqu)
            rVille.append(resultat)
        return rVille

    # à partir d'une ville, d'une activité et d'un niveau, renvoie tous ses équipements
    def equipements_villes(self, ville, act, niv):
        ville.capitalize()
        act.capitalize()
        rRecherche = []
        listeEquId = []
        tempResult = []
        if niv=="Non défini":
            query = ("SELECT ActLib, ActNivLib, EquipementId, ComLib, ComInsee FROM activite WHERE ComLib=%s AND ActLib=%s AND ActNivLib=%s")
            paire = (ville,act,niv)
        else:
            query = ("SELECT ActLib, ActNivLib, EquipementId, ComLib, ComInsee FROM activite WHERE ComLib=%s AND ActLib=%s")
            paire = (ville,act,)
        rActivite = []
        self.cursor.execute(query, paire)

        for (a) in self.cursor:
            results = a[0],a[1],a[2],a[3],a[4]
            tempResult.append(results)
        for (a) in tempResult:
            resultat = []
            NumIns = 0;
            InsLib = "";
            tmpGPS = []
            tmpEqu = []
            query2 = ("SELECT EquGpsX, EquGpsY, EquNom, InsNom, InsNumeroInstall  FROM equipement WHERE EquipementId=%s")
            paire2 = (a[2],)
            self.cursor.execute(query2, paire2)
            for (b) in self.cursor:
                tmpGPS.append(str(b[1]))
                tmpGPS.append(str(b[0]))
                tmpEqu.append(b[2])
                tmpEqu.append(b[3])
                NumIns = b[4]
            query3 = ("SELECT InsLibelleVoie FROM commune WHERE InsNumeroInstall=%s")
            paire3 = (NumIns,)
            self.cursor.execute(query3, paire3)
            for (b) in self.cursor:
                tmpEqu.append(b[0])
            tmpAct = []
            tmpAct.append(str(a[0]))
            tmpAct.append(str(a[1]))
            tmpCom = []
            tmpCom.append(str(a[3]))
            tmpCom.append(str(a[4]))
            resultat.append(tmpGPS)
            resultat.append(tmpAct)
            resultat.append(tmpCom)
            resultat.append(tmpEqu)
            rRecherche.append(resultat)
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

bd = SGBD()

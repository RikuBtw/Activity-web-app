#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

class SGBD:

    def __init__(self):
        self.cnx = mysql.connector.connect(user='E154817E', password = 'E154817E', database='E154817E', host ='infoweb')
        self.cursor = self.cnx.cursor()

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

    def ville_act(self,ville):
        query = ("SELECT ActLib, ActNivLib FROM activite WHERE ComLib=%s")
        ville = (ville,)
        rActivite = None
        self.cursor.execute(query, ville)
        for (a) in self.cursor:
            rActivite={a[0], a[1]}

        return rActivite

    def act_ville(self,act):
        act.capitalize()
        query = ("SELECT ComLib, ComInsee FROM activite WHERE ActLib=%s")
        act = (act,)
        rVille = None
        self.cursor.execute(query, act)
        for (v) in self.cursor:
            rVille={v[0], v[1]}
        return rVille

    def niveau(self,niv):
        niv.capitalize()
        query = ("SELECT ActLib FROM activite WHERE ActNivLib=%s")
        niv = (niv,)
        rNiveau = None
        self.cursor.execute(query, niv)
        for (a) in self.cursor:
          rNiveau={a[0], a[1]}
        self.cursor.close()
        return rNiveau

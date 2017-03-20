#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

cnx = mysql.connector.connect(user='E154817E', password = 'E154817E', database='E154817E', host ='infoweb')
cursor = cnx.cursor()

query = ("SELECT ActCode FROM activite WHERE ComLib=%s")

ville = ('Croisic',)
cursor.execute(query, ville)

for (EquActivitePraticable) in cursor:
  print(EquActivitePraticable[0])

cursor.close()
cnx.close()

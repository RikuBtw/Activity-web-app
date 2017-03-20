#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#Booléen de vérification
testPremier = True
try:
    #Saisie en paramètre
    nombre = input("Entrez votre valeur : ")
    #Gestion des non entier
    if (isinstance(nombre, int) == False):
        sys.exit(0)

    #Gestion des négatifs
    if nombre < 0:
        sys.exit(0)
    nombre = int(nombre)

    #Pour chaque division autre que 1 et lui-même
    for i in range(2, nombre-1):
        #Si on peut diviser, on stocke ce chiffre et on passe le booléen à false.
        #On interrompt également la boucle
        if (nombre%i == 0) :
            cause = i
            testPremier = False
            break
#Gestion de l'absence de paramètre
except IndexError:
    print "Veuillez saisir un nombre en paramètre"
    sys.exit(0)
#Gestion d'un caractère non entier
except :
    print "Veuillez saisir un nombre entier positif"
    sys.exit(0)

#Vérification de la condition
if (testPremier):
    print (str(nombre) + " est premier")
else:
    #On affiche également le premier exemple de division
    print (str(nombre) + " n'est pas premier, exemple de division : " + str(cause))

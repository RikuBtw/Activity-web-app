#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file, error
from sgbd import SGBD

#CSS et images
@route('/<filename>')
def send_static(filename):
    return static_file(filename, root='static/')

#Gestion des erreurs 404
@error(404)
def custom404(error):
    return "La page n'existe pas, désolé :("


#Page d'accueil
@route('/')
def index():
    bd = SGBD()
    ville = bd.villes()
    niv = bd.niveau()
    act = bd.activites()
    #Création de la boite de dialoge du curseur "Nantes"
    #Les données doivent être initialisées, dans le cas contraire, la boite ne s'affiche pas, étant la même pour celle-ci et les villes plus complêtes
    gps =[]
    act =[]
    equ = []
    com = []
    marker = []
    tmp=[]
    tmpMarker=[]
    gps.append(47.223225)
    gps.append(-1.5450021)
    act.append('Nantes')
    act.append('Vous êtes ici !')
    equ.append("")
    equ.append("")
    com.append("")
    com.append("")
    com.append("")
    tmp.append(gps)
    tmp.append(act)
    tmp.append(equ)
    tmp.append(com)
    marker.append(tmp)
    marker.append(tmpMarker)
    return template('index.tpl', villes=ville, activites=act, niveau=niv, markers=marker)

#En cas de recherche
@route('/', method='POST')
def index():
    #Initialisation
    e=None
    bd = SGBD()
    ville = bd.villes()
    niv = bd.niveau()
    act = bd.activites()
    marker = []

    #Récupérer les données en post
    rVille = request.forms.get('ville')
    rActivite = request.forms.get('activite')
    rNiveau = request.forms.get('niveau')

    #Création des bulles d'information
    def infobox(array):
        for element in array:
            tmp= []
            #Localisation
            gps =[]
            #Activité
            act =[]
            #Equipement
            equ = []
            #Commune
            com = []
            #Insertion des données de la base sql
            if (element[0] != []):
                gps.append(element[0][0])
                gps.append(element[0][1])
                act.append(element[1][0])
                if(element[1][1] != 'None'):
                    act.append(element[1][1])
                else:
                    act.append("Niveau inconnu")
                com.append(element[2][0] + " -")
                com.append(element[2][1] +",")
                equ.append(element[3][0]+ ",")
                equ.append(element[3][1])
                if(element[3][2] != None):
                    com.append(element[3][2])
                else:
                    com.append("Adresse inconnue")
                tmp.append(gps)
                tmp.append(act)
                tmp.append(equ)
                tmp.append(com)

                marker.append(tmp)

    #Recherche de ville et activité
    if rVille!="" and rActivite!="":
        rEqu = bd.equipements_villes(rVille, rActivite, rNiveau)
        infobox(rEqu)

    #Recherche de ville
    if rVille!="" and rActivite=="":
        rAct = bd.ville_act(rVille,rNiveau)
        infobox(rAct)

    #Recherche d'activité
    if rVille=="" and rActivite!="":
        rVille = bd.act_ville(rActivite, rNiveau)
        infobox(rVille)
        
    return template('index.tpl', villes=ville, activites=act, niveau=niv, markers=marker)



run(host='localhost', port=8000)

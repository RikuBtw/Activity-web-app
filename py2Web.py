#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file, error
from sgbd import SGBD

@route('/<filename>')
def send_static(filename):
    return static_file(filename, root='static/')

@error(404)
def custom404(error):
    return "La page n'existe pas, désolé :("


@route('/')
def index():
    bd = SGBD()
    ville = bd.villes()
    niv = bd.niveau()
    act = bd.activites()
    gps =[]
    act =[]
    equ = []
    com = []
    marker = []
    tmp=[]
    tmpMarker=[]
    gps.append(47.237225)
    gps.append(-1.510021)
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
    return template('index.tpl', erreur=None, villes=ville, activites=act, niveau=niv, markers=marker)

@route('/', method='POST')
def index():

    e=None
    bd = SGBD()
    ville = bd.villes()
    niv = bd.niveau()
    act = bd.activites()
    rVille = request.forms.get('ville')
    rActivite = request.forms.get('activite')
    rNiveau = request.forms.get('niveau')
    marker = []
    rData = []

    def infobox(array):
        for element in array:
            tmp= []
            gps =[]
            act =[]
            equ = []
            com = []
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


    if rVille!="" and rActivite!="":
        rEqu = bd.equipements_villes(rVille, rActivite, rNiveau)
        infobox(rEqu)

    if rVille!="" and rActivite=="":
        rAct = bd.ville_act(rVille,rNiveau)
        infobox(rAct)

    if rVille=="" and rActivite!="":
        rVille = bd.act_ville(rActivite, rNiveau)
        infobox(rVille)

    if rVille=="" and rActivite=="":
        e="Veuillez renseigner au moins un champs de recherche"

    return template('index.tpl', erreur=e, villes=ville, activites=act, niveau=niv, markers=marker)



run(host='localhost', port=8000)

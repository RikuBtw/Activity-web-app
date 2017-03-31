#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file
from sgbd import SGBD

@route('/<filename>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/')
def index():
    bd = SGBD()
    ville = bd.villes()
    niv = bd.niveau()
    act = bd.activites()
    tmp=[]
    marker = []
    tmp.append('<b>Nantes</b>')
    tmp.append('Vous êtes ici !')
    tmp.append(47.237225)
    tmp.append(-1.510021)
    marker.append(tmp)
    return template('index.tpl', data=None, erreur=None, villes=ville, activites=act, niveau=niv, markers=marker)

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

    if rVille!="" and rActivite!="":
        rEqu = bd.equipements_villes(rVille, rActivite, rNiveau)
        for element in rEqu:
            tmp=[];
            tmp.append("<b>"+element[0]+"</b>")
            tmp.append('description')
            tmp.append(element[1][1])
            tmp.append(element[1][0])
            marker.append(tmp)
            tmp2 = element[0]
            rData.append(tmp2)

    if rVille!="" and rActivite=="":
        rAct = bd.ville_act(rVille,rNiveau)
        for ele in rAct:
            for element in ele:
                tmp=[];
                tmp.append("<b>"+element[0]+"</b>")
                tmp.append('description')
                tmp.append(element[1][1])
                tmp.append(element[1][0])
                marker.append(tmp)
                tmp2 = element[0]
                rData.append(tmp2)

    if rVille=="" and rActivite!="":
        rVille = bd.act_ville(rActivite, rNiveau)
        for element in rVille:
            tmp=[];
            tmp.append("<b>"+element[0]+"</b>")
            tmp.append('description')
            tmp.append(element[1][0])
            tmp.append(element[1][1])
            marker.append(tmp)
            tmp2 = element[0]
            rData.append(tmp2)

    if rVille=="" and rActivite=="":
        e="Veuillez renseigner au moins un champs de recherche"

    return template('index.tpl', erreur=e, data=rData, villes=ville, activites=act, niveau=niv, markers=marker)



run(host='localhost', port=8000)

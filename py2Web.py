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
    tmp1=0
    tmp2=0
    position = tmp1, tmp2
    tmp=[]
    tmp.append("titre")
    tmp.append("description")
    tmp.append(47.237225)
    tmp.append(-1.510021)
    return template('index.tpl', data=None, erreur=None, villes=ville, activites=act, niveau=niv, markers=tmp)

@route('/', method='POST')
def index():
    tmp1=0
    tmp2=0
    position = tmp1, tmp2
    bd = SGBD()
    ville = bd.villes()
    niv = bd.niveau()
    act = bd.activites()
    rVille = request.forms.get('ville')
    rActivite = request.forms.get('activite')
    rNiveau = request.forms.get('niveau')

    if rVille!="" and rActivite!="":
        marker = []
        rData = []
        rEqu = bd.equipements_villes(rVille, rActivite, rNiveau)
        for element in rEqu:
            tmp=[];
            tmp.append(element[0])
            tmp.append('description')
            tmp.append(element[1][1])
            tmp.append(element[1][0])
            marker.append(tmp)
            tmp2 = element[0]
            rData.append(tmp2)
        return template('index.tpl', data=rData, erreur=None, villes=ville, activites=act, niveau=niv, markers=marker)

    if rVille!="" and rActivite=="":
        marker = []
        rData = []
        rAct = bd.ville_act(rVille,rNiveau)
        for ele in rAct:
            for element in ele:
                tmp=[];
                tmp.append(element[0])
                tmp.append('description')
                tmp.append(element[1][1])
                tmp.append(element[1][0])
                marker.append(tmp)
                tmp2 = element[0]
                rData.append(tmp2)
        return template('index.tpl', data=rData, erreur=None, villes=ville, activites=act, niveau=niv, markers=marker)

    if rVille=="" and rActivite!="":
        marker = []
        rData = []
        rVille = bd.act_ville(rActivite, rNiveau)
        #boucle for décomposition position
        for element in rVille:
            tmp=[];
            tmp.append(element[0])
            tmp.append('description')
            tmp.append(element[1][0])
            tmp.append(element[1][1])
            marker.append(tmp)
            tmp2 = element[0]
            rData.append(tmp2)
        return template('index.tpl', data=rData, erreur=None, villes=ville, activites=act, niveau=niv, markers=marker)

    if rVille=="" and rActivite=="":
        e="Veuillez renseigner au moins un champs de recherche"
        return template('index.tpl', erreur=e, data=None, villes=ville, activites=act, niveau=niv, markers=position)

    return template('index.tpl')



run(host='localhost', port=8000)

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
    return template('index.tpl', data=None, erreur=None, villes=ville, activites=act, niveau=niv, latitude=0, longitude=0)

@route('/', method='POST')
def index():
    bd = SGBD()
    ville = bd.villes()
    niv = bd.niveau()
    act = bd.activites()
    rVille = request.forms.get('ville')
    rActivite = request.forms.get('activite')
    rNiveau = request.forms.get('niveau')

    if rVille!="" and rActivite!="":
        ville="boujour"

    if rVille!="" and rActivite=="":
        ville="cc"

    if rVille=="" and rActivite!="":
        ville="salut"

    if rVille=="" and rActivite=="":
        e="Veuillez renseigner au moins un champs de recherche"
        return template('index.tpl', erreur=e, data=None, villes=ville, activites=act, niveau=niv, latitude=0, longitude=0)

    return template('index.tpl')



run(host='localhost', port=8000)

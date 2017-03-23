#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file
from sgbd import SGBD

@route('/file/<filename>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/')
def index():
    bd = SGBD()
    ville = bd.villes()
    act = bd.activites()
    return template('index.tpl', data=None, villes=ville, activites=act,latitude=0, longitude=0)

@route('/', method='POST')
def index():
    bd = SGBD()
    ville = bd.villes()
    recherche = request.forms.get('ville')
    name = request.forms.get('activite')
    list = bd.ville_act(recherche)
    lat = bd.LatitudeGPS(recherche)
    long = bd.LongitudeGPS(recherche)
    act = bd.activites()
    return template('index.tpl', data=list, villes=ville, activites=act, latitude=lat, longitude=long)



run(host='localhost', port=8000)

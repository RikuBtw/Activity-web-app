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
    return template('index.tpl', data=None, villes=ville, latitude=0, longitude=0)

@route('/', method='POST')
def index():
    bd = SGBD()
    ville = bd.villes()
    recherche = request.forms.get('recherche')
    name = request.forms.get('search')
    if recherche=="Ville" :
        list = bd.ville_act(name)
        lat = bd.LatitudeGPS(name)
        long = bd.LongitudeGPS(name)
    elif recherche == "Sport" :
        list = bd.act_ville(name)
        lat = 0
        long = 0
    return template('index.tpl', data=list, villes=ville, latitude=lat, longitude=long)





run(host='localhost', port=8000)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file
from sgbd import SGBD

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/')
def index():
    bd = SGBD()
    ville = bd.villes()
    return template('index.tpl', data=None, villeList=ville)

@route('/', method='POST')
def index():
    bd = SGBD()
    name = request.forms.get('search')
    list = bd.ville_act(name)
    ville = bd.villes()
    if list != None:
         return template('index.tpl', data=list, villeList=ville)
run(host='localhost', port=8000)

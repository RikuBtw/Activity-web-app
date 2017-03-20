#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, request, static_file
from sgbd import SGBD

@route('/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')

@route('/')
def index():
    return template('index.tpl')

@route('/', method='POST')
def index():
    bd = SGBD()
    name = request.forms.get('search')
    list = bd.ville_act(name)
    if list != None:
        return template('index.tpl', package=list)
    else:
        list = bd.act_ville(name)
        if list != None:
            return template('index.tpl', package=list)
        else:
            list = bd.niveau(name)
            if list != None:
                return template('index.tpl', package=list)
            else:
                return template('index.tpl', package='Pas de résultat')

run(host='localhost', port=8000)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g
from modele import*
from views import *

# konfiguracja aplikacji
app.config.update(dict(
SECRET_KEY='vehainvbnabna',
))

@app.before_request
def before_request():
    g.db = baza
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response
    
@app.route("/klasa")
def klasa():
    return render_template('klasa.html')

if __name__ == '__main__':
    app.run(debug=True)

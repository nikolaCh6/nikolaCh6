#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template, request
from flask import redirect, url_for, flash
from modele import*

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ('index.html')

@app.route("/lista")
def lista():
    pytania = Pytanie.select()
    return render_template('lista.html', query = pytania)

@app.route("/quiz", methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        print(request.form)
        wynik = 0
        for pid, oid in request.form.items():
            odp = Odpowiedz().get(Odpowiedz.id == int(oid)).odpok
            if odp:
                wynik += 1
        print("Poprawne: ", wynik)
        flash('Poprawne odpowiedzi: {}'.format(wynik), 'info')
        return redirect(url_for('index'))
        
    pytania = Pytanie.select().join(Odpowiedz).distinct().order_by(Pytanie.id)
    return render_template('quiz.html', query = pytania)

if __name__ == '__main__':
    app.run(debug=True)

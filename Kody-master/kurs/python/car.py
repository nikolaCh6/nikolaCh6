#!/usr/bin/env python
# -*- coding: utf-8 -*-

# napisz definicje obiektu samochod z nastepujacymi atrybutami
# marka, np. "Ford"
# model, np. "Mondeo"
# rok produkcji np. "2000"
# nadwozie, np. "sedan"
# metody obiektu:
# wiek() - zweaca wiek auta w latach
from datetime import date

class Auto():
        
    def __init__(self, marka, model, rok, nadwozie):
        self.marka = marka
        self.model = model
        self.rok = rok
        self.nadwozie = nadwozie
        self.wiek(rok)
        
    def wiek(self, rok):
        dzis = date.today().year
        self.wiek = dzis - self.rok
    
        return self.wiek
       
        
ford = Auto('Ford', 'Mondeo', 2000, 'sedan')
print(ford.__dict__)

exit()

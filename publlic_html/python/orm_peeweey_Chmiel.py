#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from peewee import *

baza_plik = 'test.db'
baza = SqliteDatabase(baza_plik) #instalacja bazy

#### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza

class Klasa(BazaModel):
    
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)
        
class Uczen(BazaModel):
    
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')

class Wynik(BazaModel):
    
    egzhum = FloatField(default=0)
    egzmat = FloatField(default=0)
    egzjez = FloatField(default=0)
    uczen = ForeignKeyField(Uczen, related_name='wyniki')

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    
    kl2a = Klasa (nazwa="2A" , roknaboru=2010, rokmatury=2013)
    ll2a.save()
    
    u1 = Uczen(imie="Jarosław" , nazwisko=" Mały" , plec=False , klasa=kl2)
    u1.save()
    
# dodaj klase 1A, 2009, 2012
# dodaj ucznia do klasy 1A: Anna Gacek 
# dodaj ucznia do kilasy 1A: Roman Polek     

    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

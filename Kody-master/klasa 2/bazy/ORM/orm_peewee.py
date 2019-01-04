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
    
    kl2a = Klasa(nazwa="2A", roknaboru=2017, rokmatury=2020)
    kl2a.save()
    
    kl1a = Klasa(nazwa="1A", roknaboru=2019, rokmatury=2022)
    kl1a.save()
    
    u1 = Uczen(imie="Jarosław", nazwisko="Kaczyński", plec=False, klasa=kl2a)
    u1.save()
    
    u2 = Uczen(imie="Krystyna", nazwisko="Pawłowicz", plec=True, klasa = kl1a)
    u2.save()
    
    u3 = Uczen(imie="Antoni", nazwisko="Macierewicz", plec=False, klasa = kl1a)
    u3.save()
    
    
    uczniowie = Uczen.select()
    for uczen in uczniowie:
        print(uczen.id, uczen.nazwisko, uczen.klasa.nazwa)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

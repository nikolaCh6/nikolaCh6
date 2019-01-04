#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from modele import *
from baza import dane_z_pliku

def dodaj_dane(dane):
    
    for model, plik in dane.items():
        pole = [pole for pole in model._meta.fields]
        pole.pop(0)  # usunięcie klucza głównego 
        
        wpisy = dane_z_pliku(plik + '.csv')
        model.insert_many(wpisy, fields=pole).execute()

def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Uczen, Klasa, Przedmiot, Ocena])
    
    dane = {
        Klasa: 'klasy',
        Uczen: 'uczniowie',
        Przedmiot: 'przedmioty',
        Ocena: 'oceny',
    }
    
    dodaj_dane(dane)
    
    baza.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szkola.py


import sqlite3
import csv


def dane_z_pliku(nazwa_pliku):
    dane = []  # pusta lista na dane
    with open(nazwa_pliku, 'r', newline='', encoding='utf-8') as plik:
        tresc = csv.reader(plik, delimiter='\t')
        for rekord in tresc:
            rekord = [x.strip() for x in rekord]  # oczyszczamy dane
            dane.append(rekord)  # dodawanie rekordów do listy
    return dane

def main(args):
    con = sqlite3.connect('szkola.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('szkola.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    uczniowie = dane_z_pliku('szkoła_z6pr052010_uczniowie.txt')
    uczniowie.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO uczniowie VALUES(?, ?, ?, ?, ?, ?)', uczniowie)
    
    oceny = dane_z_pliku('szkoła_z6pr052010_oceny.txt')
    oceny.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO oceny VALUES(?, ?, ?, ?)', oceny)
    
    przedmioty = dane_z_pliku('szkoła_z6pr052010_przedmioty.txt')
    przedmioty.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO przedmioty VALUES(?, ?, ?, ?)', przedmioty)

   
    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


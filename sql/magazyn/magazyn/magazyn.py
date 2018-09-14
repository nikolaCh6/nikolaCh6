#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def kwerenda_1(cur):
    cur.execute("""
        SELECT * FROM fakeapps
    """)

    """
    SELECT name, downloads FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps);
    SELECT name, downloads FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps) ORDER BY downloads DESC LIMIT 5;
    SELECT COUNT(name) FROM fakeapps WHERE downloads > (SELECT AVG(downloads) FROM fakeapps);
    SELECT category, SUM(downloads) AS suma_pobran FROM fakeapps GROUP BY category ORDER BY suma_pobran DESC;


    """
    wyniki = cur.fetchall()  # pobranie wszystkich rekordów na raz
    for row in wyniki:  # odczytywanie kolejnych rekordów
        print(tuple(row))  # drukowanie pól


def main(args):
    con = sqlite3.connect('fakeapps.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('fakeapps.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    dane = dane_z_pliku('fake_apps.txt')
    dane.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO fakeapps VALUES(?, ?, ?, ?, ?)', dane)

    # przykład zapytania (kwerendy)
    kwerenda_1(cur)

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

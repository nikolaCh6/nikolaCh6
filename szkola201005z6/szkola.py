#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szkola.py
#  
#  Copyright 2018  <>

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



    wyniki = cur.fetchall()  # pobranie wszystkich rekordów
    for row in wyniki:  # odczytywanie rekordów
        print(tuple(row))  # drukowanie pól


def main(args):
    con = sqlite3.connect('szkola.db')  # połączenie z bazą
    cur = con.cursor()  # utworzenie kursora

    # utworzenie tabeli w bazie
    with open('szkola.sql', 'r') as plik:
        cur.executescript(plik.read())

    # dodawanie danych do bazy
    tbOceny= dane_z_pliku('dane_.txt')
    print(dane)
    tbOceny.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO dane_customer VALUES(?, ?, ?, ?)', dane)

# dodawanie danych do bazy
    tbPrzedmioty = dane_z_pliku('dane_orders.txt')
    print(dane)
    tbPrzedmioty.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO dane_orders VALUES(?, ?, ?, ?)', tbPrzedfmioty)
    
# dodawanie danych do bazy
    tbUczniowie = dane_z_pliku('dane_subscriptions.txt')
    print(dane)
    tbUczniowie.pop(0)  # usuń pierwszy rekord z listy
    cur.executemany('INSERT INTO dane_subscriptions VALUES(?, ?, ?, ?)', tbUczniowie)

    #kwerenda_1(cur)

    con.commit()  # zatwierdzenie zmian w bazie
    con.close()  # zamknięcie połączenia z bazą
    return 0



def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

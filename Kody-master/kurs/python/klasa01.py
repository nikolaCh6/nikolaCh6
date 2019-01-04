#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Osoba():
    """
    Prosta klasa opisująca osobę
    """
    def __init__(self, imie, nazwisko, hp):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ustawPlec(imie)
        self.hp = hp
        
    def ustawPlec(self, imie):
        if imie [-1] == "a":
            self.plec = "k"
            self.atak = 2
            self.blok = 4
        else:
            self.plec = "m"
            self.atak = 5
            self.blok = 3
    
    def atakuj(self, osoba):
        osoba.blokuj(self.atak)
        
    def blokuj(self, atak):
        self.hp = (atak - self.blok)
        if self.hp < 1:
            print("I'm dead")
        else:
            print("JUPIKAJEJ MADAFUCKER")
    
jakub = Osoba('Jakub', 'Gwizd', 10)
print(jakub.nazwisko, jakub.plec, jakub.hp)
karolina = Osoba('Karolina', 'Świst', 10)
print(karolina.nazwisko, karolina.plec, karolina.hp)

print("Combat")
jakub.atakuj(karolina)
karolina.atakuj(jakub)
print(jakub.hp, karolina.hp)

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
        if imie[-1] == "a":
            self.__plec = "k"
            self.__atak = 2
            self.__blok = 4
        else:
            self.__plec = "m"
            self.__atak = 5
            self.__blok = 3
            
    def atakuj(self, osoba):
        #osoba.hp -= self.atak
        osoba.blokuj(self.__atak)
        
    def blokuj(self, atak):
        self.hp -= (atak - self.__blok)
        if self.hp < 1:
            print("I'm dead :)")
        else:
            print("i'm still alive!")
        
jakub = Osoba('Jakub', 'Gwizd', 10)
karolina = Osoba('Karolina', 'Świst', 10)
jakub.wzrost = 180
print(jakub.__dict__)

exit()

print(jakub.nazwisko, jakub.plec, jakub.hp)
karolina = Osoba('Karolina', 'Świst', 10)
print(karolina.nazwisko, karolina.plec, karolina.hp)

print("Combat")
jakub.atakuj(karolina)
karolina.atakuj(jakub)
print(jakub.hp, karolina.hp)

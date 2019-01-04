#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maks. losowaną liczbę: "))
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))

    # losowanie liczb

    liczby = []  # lista wylosowanych liczb
    i = 0
    #  for i in range(ileliczb):
    while i < ileliczb:
        liczba = random.randint(1, maksliczba)  # losowanie liczby <1;10>
        if liczby.count(liczba) == 0:  # sprawdzenie czy wartość jest w liście
            liczby.append(liczba)
            i += 1  # powiększ i o 1
    print(liczby)

    typy = set()  # deklaracja pustego zbioru na typy użytkownika
    i = 0
    while i < ileliczb:
        typ = input("Podaj Liczbe {}".format(i + 1))
    # Lista pozwala przechowawywać powtarzające wartości, a zbiór nieeeeeeee
        if typ not in typy:
            typy.add(typ)
            i += 1
        print(typy)

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma_cyfr.py
#  Dane wejsciowe: liczba "l2" co najmniej dwucyfrowa podawana przez uzytkownika
#  Dane Wyjściowe: suma cyfr liczby"l2" wydrukowana w terminalu
#
def sumuj_cyfry(l2):
    suma = 0
    while l2 > 0:
        suma += l2 % 10
        l2 = int(l2 / 10)
    print(suma)
    return suma

def main(args):
    
    l2 = int(input("Podaj liczbe wiekszą od 9: "))
    while l2 < 10:
        l2 = int(input("Podaj liczbę wiekszą od 9: "))

    assert(sumuj_cyfry(111) == 3)
    assert(sumuj_cyfry(9876) == 30)
    assert(sumuj_cyfry(734) == 14)
    assert(sumuj_cyfry(190) == 10)
    
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py

def silnia_it(n):
    # 0! = 1
    # n! = 1 * 2 * ... * n
    wynik = 1
    for i in range(1, n + 1):
        print(wynik)
        wynik = wynik * i
    return wynik
    
def main(args):
    # zmienne lokalne
    n = int(input("Podaj liczbę: "))
    print("{}! = {}". format(n, silnia_it(n)))
   
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

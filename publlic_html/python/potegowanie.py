#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potegowanie.py

def potega_it(a, n):
    # a^n = a1 * a2 * ... * an
    # a^1 = a
    iloczyn = 1
    for i in range(n):
        iloczyn = iloczyn * a
    return iloczyn

def main(args):
    # zmienne lokalne
    a = int(input("Podaj podstawe potegi: "))
    n = int(input("Podaj wykladnik potegi: "))
    print("{} do potęgi {} wynosi {} ". format(a, n, potega_it(a, n)), end='')
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

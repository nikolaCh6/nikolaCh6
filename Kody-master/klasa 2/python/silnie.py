#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnie.py

def f(x):
    
    wynik = 1
    
    for y in range(1, x + 1):
        wynik = wynik * y
    return wynik

def main(args):
    
    x = int(input("Podaj liczbe: "))
        
    print("{}! = {} ". format(x, f(x)), end='')
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

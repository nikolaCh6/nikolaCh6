#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia.py

a, b = 5, 10
print(a + b)
# zmienna (variable) globalna,
# zasięg (global) globalny,
# przestrzeń nazw (namespace) moduł

def sumuj1(): # nowa przestrzeń nazw, przestrzeń funkcji
    
    print(a + b)

def main(args):
    
    global a, b
    a, b = 2, 3 # zmienne lokalne, zasięg lokalny, przestrzeń funkcji
    print(a + b)
    sumuj1() #wywołanie funkcji
    
    return 0
    
def odejmij(x, y):
    
    print(x - y)
    x, y = 5, 4
    
def odejmij2(lista):
    
    lista.append(lista[0] - lista[1])
    
def main2(args):
    
    # ~a, b = 2, 3
    # ~print(a - b)
    # ~odejmij(a, b)
    # ~print(a - b)
    l = [3, 4]
    odejmij2(l)
    print(l)
    
    return 0

if __name__ == '__main__':
    # skrypt został uruchomiony, a nie zaimportowany
    import sys
    sys.exit(main2(sys.argv))

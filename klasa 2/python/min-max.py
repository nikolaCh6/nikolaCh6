#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  min-max.py

import random

# ~ def minmax1():
    # ~ a = int(input('Podaj Liczbę: '))
    # ~ min1 = a
    # ~ max1 = a
    
    # ~ while True:
        # ~ a = int(input('Podaj Liczbę: '))
        # ~ if a < 1:
            # ~ break
        # ~ if a < min1:
            # ~ min1 = a
        # ~ if a > max1:
            # ~ max1 = a
    # ~ return min1, max1

def minmax2(lista):
    """Funkjca zwraca element minimalny i maksymalny z podanej listy"""
    min2 = max2 = lista[0]
    
    for x in lista:
        if x < min2:
            min2 = x
        if x > max2:
            max2 = x
    
    return min2, max2

def main(args):
    
    # ~ min, max = minmax()
    # ~ print("Najmniejsza liczba: ",min)
    # ~ print("Największa liczba: ",max)
    
    lista =[]
    for i in range(100):
        lista.append(random.randint(1, 1000))
    print(lista)
    min2, max2 = minmax2(lista)
    print("Najmniejsza liczba: ",min2)
    print("Największa liczba: ",max2)
    
     
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

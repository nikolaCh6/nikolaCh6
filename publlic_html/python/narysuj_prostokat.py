#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  narysuj_prostokat.py
#  
#  Copyright 2018  <>
#Dane wejściowe: boki a i b prostokąta
#Dane wyjściowe: prostokąt narysowany w terminalu gwiazdkami o 
#                rozmiarach podanych przez użutkownika
#EXTRA: znak, którym rysowany jest prostokąt pobierz od uzytkownika 
#Prostokąt o wymiarach 17 na 9
#

def main(args):
     
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b : "))
    znak = input("Podaj znak którym chcesz rysować: ")
    
    i = 0
    j = 0
    
    for i in range(a):
        if i == 0 or i == a - 1:
            print(znak*a)
            continue
        for j in range(b):
            if j > 0 and j < b - 1:
                print("", end = '')
            else:
                print(znak, end='')
        print()
        
    
    return 0 

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

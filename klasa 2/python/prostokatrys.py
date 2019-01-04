#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rysunek.py
#  
# DANE WEJSCIOWE: boki a i b
# DANE WYJSCIOWE: rysunek prostokata rysowany gwiazdkami o wymiarach jakie podal uzytkownik

def main(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    znak = input("Podaj znak: ")
 
    for i in range(a):
        if i == 0 or i == a - 1:
            print(znak*b)
            continue
        for j in range (b):
            if j > 0 and j < b - 1:
                print(" ", end=' ')
            else:
                print(znak, end=' ')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

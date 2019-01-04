#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkat.py
import math
        
def prostokatny(a, b, c):
    
    trojkat = False
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        trojkat = True
    if trojkat:
        print('Trójkąt będzie prostokątny :D')
    else:
        print('Trójkąt nie będzie prostokątny :/')
    
def pole(a, b, c):
        l = (a + b + c)/2
        p = math.sqrt(l * (l - a) * (l - b) * (l - c))
        print('Pole wynosi: {:.4f}'.format(p))
        
def trojkat(a, b, c):
    
    trojkat = False
    if a + b > c and a + c > b and b + c > a:
        trojkat = True
        
    if trojkat:
        print('Gratuluję, zbudujesz trójkąt :)')
        prostokatny(a, b, c)
        pole(a, b, c)
    else:
        print('Idioto, spróbuj ponownie :P')
        
def main(args):
    a, b, c = eval(input("Podaj dane oddzielone przecinkami: "))
    print('Podano boki: {}, {}, {}'.format(a, b, c))
    trojkat(a, b, c)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

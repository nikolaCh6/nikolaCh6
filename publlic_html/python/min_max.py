#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  min_max.py


def min1():
    a = int(input('Podaj liczbę:'))
    min = a
    max = a
    
    while True:
        a = int(input('Podaj liczbę:'))
        if a < 1:
            break
        if a < min:
            min = a
        if a > max:
            max = a
            
    return min, max
    
def minmax2(lista):
    """Funkcja zwraca element minimalny i maksymalny z podanej listy"""
    
    liczba =
    min = 1
    max = 0
    
    for liczba in lista:
        if 
    
    pass 
    
    return min, max
    

def main(args):
    # min, max = minmax1()
    # print ("Najmniejsza liczba:",min())
    # print ("Największa liczba:",max())
    
    lista = []
    for i in range(100):
        lista.append(random.randint(1, 100))
    print()lista    
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

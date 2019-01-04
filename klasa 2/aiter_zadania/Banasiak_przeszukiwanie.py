#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def wpisz(szuk):
    for i in range(50):
        szuk.append(random.randint(0, 50))
    print(szuk)
    
def main(args):
    i = 0
    szuk = []
    wpisz(szuk)
    i = int(input("Podaj liczbę: "))
    
    for a in range (len(szuk)):
        if szuk.count(i) == 0 or i > 51:
            print("Element nieznaleziony")
            i += 1
            return
        else:
            print("Element znaleziony")
            return
            
    return 0
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

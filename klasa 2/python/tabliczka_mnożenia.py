#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tabliczka_mnożenia.py


def tabliczka(a, b):
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            print("{:>5} ".format(i * j), end='')
        print()
        
def main(args):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: ")) 
    tabliczka(a,b)   
    return 0
    
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

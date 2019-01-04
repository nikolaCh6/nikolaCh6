#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cpp2.py
#

def main(args):
    
    a = int(input("podaj liczbe a: "))
    b = int(input("podaj liczbe b: "))
    
    
    while a >= b:
        b = int(input("Pierwsza liczba musi mniejsza od drugiej: "))
    
    for c in range(a, b+1):
        print (c, " ", end='')
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

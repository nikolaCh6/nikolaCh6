#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  choinka.py

def main(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    znak = input("Podaj znak: ")
 
    for i in range(a):
        for j in range (b):
            if j > i and j < b:
                print(" ", end='')
            else:
                print(znak, end='')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

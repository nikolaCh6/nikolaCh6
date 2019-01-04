#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  porstokat.py
#  

  
def pole(a, b):
    return a * b
    
def obwod(a, b):
    return (2 * a) + (2 * b)

def main(args):
    
    a = int(input("Podaj długość boku a: "))
    print(a)
    
    b = int(input("Podaj długość boku b: "))
    print(b)
    
    print("Pole = ", pole(a, b))
    print("Obwód = ", obwod(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

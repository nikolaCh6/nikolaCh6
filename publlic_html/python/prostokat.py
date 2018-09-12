#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat.py
#  
#  Copyright 2018  <>

def obwod(a, b):
    return a + b + a + b
    
    
def pole(a, b):
    return a * b
    
    

def main(args):
    a = int(input("Podaj pierwszy bok: "))
    print(a)
    b = int(input("Podaj drugi bok: "))
    print(b)
    
    print("Obwód: ", obwod(a, b))
    print("Pole: ", pole(a, b))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))



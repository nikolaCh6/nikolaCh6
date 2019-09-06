#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  warunek.py
#  


def max(a, b, c):
    
    maks = a
    
    if b > maks:
        maks = b
        
    if c > maks:
        maks = c
    
    return  maks 
    
def main(args):
    
    a = int(input("Podaj pierwszą liczbę: " ))
    b = int(input("Podaj drugą liczbę: " ))
    c = int(input("Podaj trzecią liczbę: " ))
    maks = najwieksza(a, b, c)
    
    print("Najwiekszą liczbą jest ", maks)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

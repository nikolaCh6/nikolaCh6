#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie-wyjscie.py
# duck typing
# zasieg zmiennych: zasieg lokalny (ograniczony np. funkcją)

def suma(a, b):
    return a + b
    
def roznica(a, b):
    return a - b
    
def iloczyn(a, b):
    return a * b
    
def iloraz(a, b):
    return a / b
    
    

def main(args):
    a = int(input("Podaj pierwsza liczbe: "))
    print(a)
    
    b = int(input("Podaj druga liczbe: "))
    print(b)
    
    print("Suma: ", suma(a, b))
    print("Różnica: ", roznica(a, b))
    print("Iloczyn: ", iloczyn(a, b))
    print("Iloraz: ", iloraz(a, b))
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

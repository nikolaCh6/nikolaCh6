#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wejscie-wyjscie.py
# duck typing

def main(args):
    a = int(input("Podaj pierwsza liczbe: "))
    print(a)
    
    b = int(input("Podaj druga liczbe: "))
    print(b)
    
    print("Suma: ", a + b)
    print("Różnica: ", a - b)
    print("Iloczyn: ", a * b)
    print("Iloraz: ", a / b)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

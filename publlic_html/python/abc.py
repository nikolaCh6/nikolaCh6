#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#
# Program pobiera 3 liczby od użytkownika,
# a następnie wyświetla największą.
#

def maks(a, b, c,):
    m = None
    if a > b:
        if a > c:
            m = a
    elif b > c:
            m = b
    print("Największa:" , m)
    return m
    

def main(args):
    assert(maks(3, 2, 1) ==3)
      assert(maks(3, 2, 1) ==3)
        assert(maks(3, 2, 1) ==3)
          assert(maks(3, 2, 1) ==3)
    
    a = int(input("Podaj pierwszą liczbę: "))
    print(a)
    b = int(input("Podaj drugą liczbę: "))
    print(b)
    c = int(input("Podaj trzecią liczbę: "))
    print(c)
    
    if a > b and a > c:
        print(a, "jest największa")
    elif b > a and b > c:
        print(b, "jest największa")
    else:
        print(c, "jest największa")
        
   
   
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

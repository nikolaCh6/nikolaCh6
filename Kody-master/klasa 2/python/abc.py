#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#  

    
def maks2(a, b, c):
    """
    Funkcja wyszukuje i zwraca najwieksza z trzech podanych liczb
    """
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    
    return m
    
def main(args):
    
    assert(maks2(3, 2, 1) == 3)
    assert(maks2(2, 3, 1) == 3)
    assert(maks2(1, 3, 2) == 3)
    assert(maks2(1, 2, 3) == 3)
    assert(maks2(1, 1, 3) == 3)
    assert(maks2(3, 3, 1) == 3)
    assert(maks2(3, 1, 1) == 3)
    assert(maks2(3, 2, 3) == 3)
    assert(maks2(3, 3, 3) == 3)
    
    return 0
    
    #a = int(input("Podaj liczbe a: "))
    #print(a)
    
    #b = int(input("Podaj liczbe b: "))
    #print(b)
    
    #c = int(input("Podaj liczbe c: "))
    #print(c)
    
    #if a > b and a > c:
    #    print(a, "jest najwieksza")
    #elif a < b and b > c:
    #    print(b, "jest najwieksza")
    #elif a < c and b < c:
    #    print(c, "jest najwieksza")
    #elif a == b == c:
    #       print(a, "jest najwieksza")
    #else:
    #    if a == b and a < c:
    #       print(c, "jest najwieksze")
    #    if c == b and c < a:
    #       print(a, "jest najwieksze")
    #    if a == c and a < b:
    #       print(b, "jest najwieksze")
    #    if a == b and a > c:
    #       print(a, "jest najwieksze")
    #    if c == b and c > a:
    #       print(c, "jest najwieksze")
    #    if a == c and a > b:
    #       print(a, "jest najwieksze")
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def wersja_1(n, silnia, i):
    while i <= n:
        silnia *= i
        i += 1
    print(silnia)
        
def main(args):
    n = int(input("Wprowadz n: "))
    silnia = 1
    i = 1
    wersja_1(n, silnia, i)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

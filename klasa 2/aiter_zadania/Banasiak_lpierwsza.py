#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pierwsze(n, i):
    
    if i * i <= n:
        if (n % i) != 0:
            i += 1
            pierwsze(n, i)
        else:
            print("{} to liczba złożona".format(n))
    else:
        print("{} to liczba pierwsza".format(n))
    
def main(args):
    n = int(input("Podaj liczbę całkowitą: "))
    i = 2
    pierwsze(n, i)
     
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

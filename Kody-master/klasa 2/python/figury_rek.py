#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

def rysuj(bok, kat, przyrost, warunek):
    
    turtle.forward(bok)
    turtle.right(kat)
    if kat <= warunek:
        rysuj(bok, kat, przyrost, warunek-przyrost)

def main(args):
    
    bok = int(input("Podaj bok: "))
    kat = int(input("Podaj kat: "))
    przyrost = 30
    warunek = 180
    
    turtle.setup(1000.800)
    turtle.color('black', 'red')
    turtle.begin_fill()
    turtle.speed(5)
    
    rysuj(bok, kat, przyrost, warunek)
    
    turtle.end_fill()
    turtle.done()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_rek.py

import turtle

def rysuj(bok, kat, przyrost, warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if kat <= warunek:
        bok += 10
        rysuj(bok, kat, przyrost, warunek)
    
    
def main(args):
    turtle.setup(800, 600)
    turtle.color('black', 'green')
    turtle.begin_fill()
    turtle.speed(10)
    
    rysuj(bok=10, kat=91, przyrost=30, warunek=180)
    
    turtle.end_fill()
    turtle.done()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

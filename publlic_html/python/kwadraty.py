#!/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

def rysujKwadrat(zolw, bok, ile):
    
    # ~ for i in range(4):
    zolw.forward(bok)
    zolw.right(90)
    if ile > 0:
        rysujKwadrat(zolw, bok, ile-1)
    
def rysujKwadrat2(zolw, bok):
    for i in range(4):
        zolw.forward(bok)
        zolw.left(90)
    
    if bok >= 10:
        rysujKwadrat2(zolw, bok-10)
        
def rysuj(zolw, bok, kat, warunek):
    zolw.forward(bok)
    zolw.right(kat)
    if kat < warunek:
        rysuj(zolw, bok, kat, warunek)
        
def main(args):
    bok = int(input("Podaj bok: "))
    kat = int(input("Podaj kat: "))
    # ~ bok = 100
    ile = 4
    warunek = 180
    turtle.title("Kwadraty")
    turtle.setup(1000,800)
    
    zolw = turtle.Turtle()
    zolw.color('black', 'red')
    zolw.pensize(2)
    zolw.speed(0)
    
    # ~ rysujKwadrat(zolw, bok, ile)
    zolw.begin_fill()
    # ~ rysujKwadrat2(zolw, bok)
    rysuj(zolw, bok, kat, warunek)
    zolw.end_fill()
        
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

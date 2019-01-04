#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parzyste.py
#  


def main(args):
    start = int(input("Podaj pierwszą liczbę:"))
    stop = int(input("Podaj drugą liczbę:"))
    
    if start > stop:
        print("Źle gałganie")
        exit(0)
    
    for liczba in range(start, stop + 1):
        #if liczba % 2 == 0:
        if not liczba % 2:
            print(liczba)
        
            
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

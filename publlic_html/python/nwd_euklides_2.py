#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nwd_euklides_2.py  
# 
 
def nwd_klasyczny(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def main(args):
    a = int(input("Liczba 1:"))
    b = int(input("Liczba 2:"))
    print(nwd_klasyczny(4,190))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

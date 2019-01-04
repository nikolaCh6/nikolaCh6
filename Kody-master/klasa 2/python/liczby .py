#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczby.py

def liczby2():
    
    """
    Drukuje wszystkie liczby 2-cyfrowe o niepowtarzających się
    cyfrach i ich ilość
    """
    ile=0
    
    for i in range(1, 10):
        for j in range(0, 10):
            if i != j:
                print("{}{} ".format(i, j), end='')
            ile += 1
    return ile
       
def liczby3():
    
    """
    Drukuje wszystkie liczby 3-cyfrowe o niepowtarzających się
    cyfrach i ich ilość
    """
    
    ile=0
    
    for i in range(1, 10):
        for j in range(0, 10):
            for k in range(0, 10):
                if i != j and i != k and j != k:
                    print("{}{}{} ".format(i, j, k), end='')
                ile += 1
    return ile
        
def main(args):
    return 0
    
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

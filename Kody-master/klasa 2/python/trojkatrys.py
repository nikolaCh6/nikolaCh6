#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  trojkatrys.py

def trojkat(a, c):
    for i in range (a):
        print(" "*(a - i), c * (i*2-1))
    
    return 0


def main(args):
    trojkat(10, "$")
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

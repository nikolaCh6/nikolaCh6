#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cpp3.py
#

def main(args):
	
	a = int(input("Podaj liczbe a: "))
	b = 0
	
	for a in range(a+1):
		b = a*a
		print(b)

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

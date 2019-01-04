#!/usr/bin/env python
# -*- coding: utf-8 -*-

def kolejne_1(n, i):
     for i in range(1, n, 2):
         print(i)

def kolejne_2(n, i):
    while i < n:
        print(i)
        i += 2
# algorytm częściowo poprawny
# algorytm skończony
# algorytm o złożoności liniowej O(n)

def main(args):
    n = int(input("Wprowadz n: "))
    i = 1
    print("Wersja 1: ")
    kolejne_1(n, i)
    print("Wersja 2: ")
    kolejne_2(n, i)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

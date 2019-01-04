#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)
    # komentarz
    for i in range(3):
        odp = input("Podaj liczbę od 1 do 10: ")
        print(" Podałeś liczbę:", odp)

         if liczba == int(odp):
             print("Zgadłeś!")
             break #stop pentla
         else:
            print("Jeszcze raz!!!")

    return 0


if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

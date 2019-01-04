#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stos_obj import Stos

def czy_poprawne(onp):
    for z in onp:
        if z.isalpha():
            return False
    return True

def main(args):
    stos = Stos()
    onp = input("Podaj wyrażenie ONP, oddzielając operandy i operatory spacjami:\n")
    if not czy_poprawne(onp):
        print("Błąd wyrazenia!")
        return 0
        
    onp = onp.split(" ")
    
    for el in onp:
       if el.isdigit():
           stos.push(el)
       else:
           a = stos.pop()
           b = stos.pop()
           stos.push(eval(str(b) + el + str(a)))

    print("Wynik: ", stos.pop())
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py

def bmi(a, b):
    
    bmi = a / ((b/100)**2)
    
    if bmi < 18.5:
        print('Twoje BMI wynosi: {:.2f}'.format(bmi), 'Masz niedowagę')
    elif bmi < 25:
        print('Twoje BMI wynosi: {:.2f}'.format(bmi), 'Norma')
    elif bmi < 30:
        print('Twoje BMI wynosi: {:.2f}'.format(bmi), 'Nadwaga')
    else:
        print('Twoje BMI wynosi: {:.2f}'.format(bmi), 'Otyłość')
        
    
def main(args):
    a = int(input("Podaj wagę w kilogramach: "))
    b = int(input("Podaj wzrost w centmetrach: "))
    bmi(a, b)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

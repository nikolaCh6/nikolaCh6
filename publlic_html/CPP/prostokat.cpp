/*
 * prostokat.cpp
 * 
 * Copyright 2018  <>
 */
 


#include <iostream>

using namespace std;

int obwod(int a, int b)
{
   return 2*a + 2*b;
}

int pole(int a, int b)
{
   return a * b;
}
    
int main(int argc, char **argv)
{
      int a, b;  // deklaracja zmiennych
    a = b = 0; //inicjalizacja zmiennych
    
    cout << "Podaj pierwszy bok: ";
    cin >> a;
    
    cout << "Podaj drugi bok: ";
    cin >> b;
    
    cout << a << " " << b;
    
    cout << endl << " Obwód: " << obwod(a, b) << endl;
    cout << endl << " Pole: " << pole(a, b) << endl;
	
	return 0;
}


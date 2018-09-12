/*
 * szkielet.cpp
 */


#include <iostream>

using namespace std;

int suma(int a, int b)
{
   return a + b;
}

int roznica(int a, int b)
{
   return a - b;
}

int iloczyn(int a, int b)
{
   return a * b;
}

int iloraz(int a, int b)
{
   return a / b;
}

int main(int argc, char **argv)
{

    int a, b;  // deklaracja zmiennych
    a = b = 0; //inicjalizacja zmiennych
    
    cout << "Podaj liczbę: ";
    cin >> a;
    
    cout << "Podaj drugą liczbę: ";
    cin >> b;
    
    cout << a << " " << b;
    
    cout << endl << " Suma: " << suma(a, b) << endl;
    cout << endl << " Róznica: " << roznica(a, b) << endl;
    cout << endl << " Iloczyn: " << iloczyn(a, b) << endl;
    cout << endl << " Iloraz: " << iloraz(a, b) << endl;
    
    
    //DRY-don't repeat yourself
    
	return 0;
}



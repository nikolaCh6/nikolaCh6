/*
 * szkielet.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{

    int a, b;  // deklaracja zmiennych
    a = b = 0; //inicjalizacja zmiennych
    
    cout << "Podaj liczbę: ";
    cin >> a;
    
    cout << "Podaj drugą liczbę: ";
    cin >> b;
    
    cout << a << " " << b;
    
    cout << endl << " Suma " << a + b << endl;
    cout << endl << " Róznica " << a - b << endl;
    cout << endl << " Iloczyn " << a * b << endl;
    
    
    //DRY-don't repeat yourself
    
	return 0;
}


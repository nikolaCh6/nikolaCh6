#include <iostream>

using namespace std;

int suma(int a, int b){
    return a + b;
    }

int roznica(int a, int b){
    return a - b;
    }

int iloraz(int a, int b){
    return a / b;
    }

int iloczyn(int a, int b){
    return a * b;
    }



int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "Podaj pierwsza liczbe: ";
    cin >> a;
    cout << a;
      
    cout << endl << "Podaj druga liczbe: ";
    cin >> b;
    cout << b;
    
    cout << endl << "Suma: " << suma(a, b);
    cout << endl << "Różnica: " << roznica(a, b);
    cout << endl << "Iloraz: " << iloraz(a, b);
    cout << endl << "Iloczyn: " << iloczyn(a, b);
    
	return 0;
}

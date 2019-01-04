/*
 * potega.cpp
 */

#include <iostream>
using namespace std;

// x^0 = 1 dla x <> 0
// x^n = x(n-1)*x dla n = N+

float potega_re(float x, int n)
{
    if (n == 0) return 1;
    return potega_re(x, n-1) * x;
}

int main(int argc, char **argv)
{
	float podstawa;
    int wykladnik;
    cout << "Podstawa: ";
    cin >> podstawa;
    
    cout << "Wykładnik: ";
    cin >> wykladnik;
    
    cout << "Wynik: " << potega_re(podstawa, wykladnik);
    
    
    
	return 0;
}


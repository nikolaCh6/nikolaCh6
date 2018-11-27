/*
 * potenga.cpp
 * 
 */


#include <iostream>
using namespace std;

//x0 = 1 dla x <> 0
// xn = x(n-1)*x dla n = N+
float potenga_re(float x, int n)
{
   if (n == 0) return 1;
   return potenga_re(x, n-1) * x
}

int main(int argc, char **argv)
{
	float podstawa;
    int wykładnik;
    cout << "Podstawa: "; cin >> podstawa;
    cout << "Wykładnik: "; cin >> wykladnik;
    cout << "Wynik: " << potenga_re(podstawa, wykladnik);
	return 0;
}


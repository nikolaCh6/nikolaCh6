/*
 * fibonacci.cpp
 */


#include <iostream>
using namespace std;

float fibonacci_re(int n)
{   
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci_re(n-1) + fibonacci_re(n-2);
}

int fibonacci_it(int n)
{   
    int a = 0; // n-2
    int b = 1; // n-1
    if (n < 1) return a;
    else if (n < 2) return b;
    int wynik = 0;
    for (int i = 2; i <= n; i++)
    {
        wynik = a + b;
        a = b;
        b = wynik;
    }
    return wynik;
}

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj numer wyrazu ciągu: ";
    cin >> n;
    cout << "Ciąg Fibonacci'ego ITERACYJNIE " << n << " :" << fibonacci_it(n) << endl;
    cout << "Ciąg Fibonacci'ego REKURENCYJNIE " << n << " :" << fibonacci_re(n) << endl;
    
	return 0;
}


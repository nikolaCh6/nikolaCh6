/*
 * fibonacci.cpp
 * 
 */


#include <iostream>
using namespace std;

// f(n) = 1 dla n {0, 1}
// f(n) = f(n-1) + f(n-2) dla n > 1

int fibonacci_re(int n) // wersja rekurencyjna
{
   
    if (n == 0) return 0;
    if (n == 1 || n == 2) return 1;
    return fibonacci_re(n-1) + fibonacci_re(n-2);
}


int fibonacci_it(int n)
{
    int a = 0; // wyraz n-2
    int b = 1; // wyraz n-1
    if (n < 1) return a;
    else if ( n < 2) return b;
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
    cout << "Ciąg Fibonacciego do wyrazu: " << n << ": " << endl;
    cout << fibonacci_it(n);
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ":" << endl;
    // cout << fibonacci_it(n);
	return 0;
}


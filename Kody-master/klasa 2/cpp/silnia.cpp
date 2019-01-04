/*
 * silnia.cpp
 */


#include <iostream>
using namespace std;

float silnia_it(int n)
{
    int silnia = 1;
    int i;
    for (i = 1; i <= n; i++)
    {
        silnia = silnia * i;
    }
        return silnia;
}

float silnia_re(int n)
{
    if (n == 0) return 1;
    return silnia_re(n-1) * n;
}

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj liczbę: ";
    cin >> n;
    
    cout << "Wynik: " << silnia_re(n) << endl;
    cout << "Wynik: " << silnia_it(n) << endl;
    
    
    
	return 0;
}

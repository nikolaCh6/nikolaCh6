/*
 * horner.cpp
 * 
 * w(x) = 2x^3 + 3x^2 + 5x + 4 => 6 mnożeń + 3 dodawania
 * w(x) = x (x (2x + 3) + 5) + 4 => 3 mnożenia + 3 dodawania
 * 
 */


#include <iostream>
using namespace std;

void drukujw(int st, float tbwsp[])
{
    int i = 0;
    for (i = 0; i < st; i++)
    {
        cout << tbwsp[i] << "x^" << st - i << " + " ;
    }
    cout << tbwsp[i];
}

float horner_re(int st, float tbwsp[], float x)
{
    if (st == 0) return tbwsp[0];
    return x*horner_re(st-1, tbwsp, x) + tbwsp[st];
}

float horner_it(int st, float tbwsp[], float x)
{
    int i = 0;
    float wynik = tbwsp[i];
    for (i = 1; i <= st; i++)
    {
        wynik = wynik * x + tbwsp[i];
    }
    
    return wynik;
}


int main(int argc, char **argv)
{
    float x = 0;
    int stopien = 0;
    cout << "Podaj stopień wielomianu: ";
    cin >> stopien;
    float *tbwsp;  // wskaźnik ~ adres komórki w pamięci
    tbwsp = new float [stopien+1];
    for (int i = 0; i <= stopien; i++)
    {
        cout << "Podaj współczynnik przy potędze " << stopien-i << " : ";
        cin >> tbwsp[i];
    }
    
    cout << "Podaj argument: ";
    cin >> x;
    
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    cout << "\nDla x = " << x << " wynosi: " << horner_it(stopien, tbwsp, x);
    cout << "\nRekurencyjne x = " << x << " wynosi: " << horner_re(stopien, tbwsp, x);
    
	return 0;
}


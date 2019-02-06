/*
 * dec2bin_2.cpp
 * 
 */


#include <iostream>
using namespace std;

int dec2any(int liczba, int podstawa, int tab[])
{
    int i=0;
    do {
        tab[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++;
    } while (liczba != 0);
    return i-1;
}

void bin2dec(int tab[])
{
    ;
}

int main(int argc, char **argv)
{
	int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawe systemu docelowego: ";
    cin >> liczba >> podstawa;
    int i = dec2any(liczba, podstawa, tab);
    cout << "Wynik: ";
    while (i > -1) {
        cout << tab[i];
        i--;
        } 
	return 0;
}


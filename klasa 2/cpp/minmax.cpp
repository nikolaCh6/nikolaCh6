/*
 * minmax.cpp
 */


#include <iostream>
#include <cstdlib>

using namespace std;

void wypelnij(int tab[], int rozmiar)
{
    cout << "Podaj " << rozmiar << " liczb: " <<endl;
    for(int i = 0; i < rozmiar; i++)
    {
        cin >> tab[i];
    }
}

void los(int tab[], int rozmiar)
{
    srand(time(NULL)); //inicjacja generatoraliczb pseudolosowych
    for(int i = 0; i < rozmiar; i++)
    {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar)
{
    for(int i = 0; i < rozmiar; i++)
    {
        cout << tab[i] << ' ';
    }
}

int min(int tab[], int rozmiar)
{
    int min = tab[0]; //inicjacja pierwszego elementu tablicy
    for(int i = 1; i < rozmiar; i++)
    {
            if(tab[i] < min)
                min = tab[i];
    }
    return min;
}

int max(int tab[], int rozmiar)
{
    int max = tab[0]; //inicjacja pierwszego elementu tablicy
    for(int i = 1; i < rozmiar; i++)
    {
            if(tab[i] > max)
                max = tab[i];
    }
    return max;
}

int main(int argc, char **argv)
{
	int rozmiar = 100;
    int tablica[rozmiar];  // statyczna deklaracja tablicy
    los(tablica, rozmiar);
    drukuj(tablica, rozmiar);
    cout << endl << "Najmniejsza liczba: " << min(tablica,rozmiar);
    cout << endl << "Największa liczba: " << max(tablica, rozmiar);
    
	return 0;
}


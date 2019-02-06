/*
 * wyszukaj.cpp
 * 
 */


#include <iostream>
using namespace std;

void los(int tab[], int rozmiar)
{
    srand(time(NULL));  // inicjacja generatoraliczb pseudolosowych
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
void sort_insert(int tab[], int n)
{
    cout << "\nSortowanie przez wstawianie" << endl;
    int i, j, tmp;
    for(i = 1; i < n; i++)  // pętla wybiera elementy zaczynając od drugiego
    {
        tmp = tab[i];
        j = i - 1;
        while(j >= 0 && tab[j] >tmp)
        {
            tab[j+1] = tab[j];
            j--;
        }
        tab[j+1] = tmp;
    }
}
int szukaj_bin_it(int tab[], int n, int szuk)
{
    int p, k, s;
    p = 0; k = n - 1;
    
    while (p <= k)
    {
        s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        else if (szuk < tab[s]) k = s - 1;
        else p = s + 1;
    }
    return -1;
    
}

int szukaj_bin_rek(int tab[], int szuk, int p, int k)
{
    if (p <= k) 
    { 
        int s = (p + k) / 2;
        if (tab[s] == szuk) return s;
        if (szuk < tab[s]) 
            return szukaj_bin_rek(tab, szuk, p, s-1);
        else 
            return szukaj_bin_rek(tab, szuk, s + 1, k);
    }
    return -1;
    
}

int main(int argc, char **argv)
{
    int n = 20;
    int tab[n];
    
    los(tab,n);
    drukuj(tab, n);
    
    int szuk = 0;
    
    cout << "\nPodaj liczbę: ";
    cin >> szuk;
    sort_insert(tab, n);
    drukuj (tab, n);
    
    //int indeks = szukaj_bin_it(tab, n, szuk);
    int indeks = szukaj_bin_rek(tab, szuk, 0, n-1);
    
    if (indeks >= 0)
        cout << "\nZnaleziona! " << indeks << endl;
    else
        cout << "\nNie znaleziona! " << indeks << endl;

}


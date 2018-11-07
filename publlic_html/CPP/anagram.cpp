/*
 * anagram.cpp
 */

#include <iostream>

using namespace std;

int zlicz(char tab[])
{
    int i = 0;
    while(tab[i] != '\0') i++;
    return i;
}

void wyswietl(char tab[], int roz)
{
    for(int i = 0; i < roz; i++)
    {
        cout << tab[i];
    }
}

void anagram(char tab[], int roz)
{
        for(int i = roz - 1; i >= 0; i--)
        {
            cout << tab[i];
        }  
}

int main(int argc, char **argv)
{
	const int rozmiar = 50;  // deklaracja stałej
    char tekst[rozmiar];  // deklaracja tablicy znakowej
    cout << "Wprowadz tekst: ";
    cin.getline(tekst, rozmiar);
    wyswietl(tekst, zlicz(tekst));
    cout << endl;
    anagram(tekst, cin.gcount());
    cout << endl;
    return 0;
}

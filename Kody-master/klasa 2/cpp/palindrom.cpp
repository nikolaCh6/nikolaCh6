/*
 * palindrom.cpp
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(char tab[], int roz)
{
    bool czyPal = true;
    for(int i = 0; i < roz / 2; i++)
    {
        if (tab[i] == tab[roz - 1 - i]);
        else
        {
            czyPal = false;
            break;
        }
    }
    return czyPal;
}

int main(int argc, char **argv)
{
	const int rozmiar = 20;
    char tekst[rozmiar];
    cout << "Wprowadz tekst: ";
    cin.getline(tekst, rozmiar);
    if (palindrom(tekst, strlen(tekst)))
    {
        cout << "Podałeś poprawny tekst";
    }
    else
    {
        cout << "Podałeś niepoprawny tekst";
    }
    
	return 0;
}


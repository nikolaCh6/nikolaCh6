/*
 * szyfr_cezara.cpp
 */


#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

#define MAKS 100

void deszyfruj(char tb[], int k)
{
    ;
}

void szyfruj(char tb[], int k)
{
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    
    while(tb[i] != '\0')
    {
        kod = (int)tb[i];
        if (tb[i] == '') 
        {
           ; 
        }
    else if(kod < 91)
    {
        kod += klucz;
        if (czy_przekroczono_zakres 90)
        ;
        }
        else // mała litera 
        {
            kod += klucz;
            if (czy_przekroczono_zakres 122)
            ;
        }
    {
        cout << (char)kod;
        tb[i] = char(kod); // zapisz zaszyfrowany znak
        i++;
    }
}


int main(int argc, char **argv)
{
    char tekst[MAKS];
	int klucz = 0;

    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);

    cout << "Podaj klucz: " << endl;
    cin >> klucz;

    szyfruj(tekst, klucz);
	return 0;
}


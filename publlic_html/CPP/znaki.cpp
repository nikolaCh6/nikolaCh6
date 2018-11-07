/*
 * znaki.cpp
 */


#include <iostream>

using namespace std;

void licz_znaki(char tab[])
{
    int i = 0;
    int biale, inter, licz;
    biale = inter = licz = 0;
    while (tab[i] != '\0')
    {
        //~ if (tab[i] == ' ' || tab[i] == '\t')
            //~ biale++;
        //~ else
            //~ cout << tab[i] << ' ';
        switch (tab[i])
        {
            case ' ':
                biale++;
                // inne;
            break;
            case '\t':
                biale++;
                // inne;
            break;
            case ',':
                inter++;
                // inne;
            break;
            case '.':
                inter++;
                // inne;
            break;
            default:
                licz++;
                // inne;
            break;
        }
        i++;  // zwiększanie indeksu
    }
    cout << "\nZnaków białych: " << biale << endl;
    cout << "\nZnaków interpunkcyjnych: " << inter << endl;
    cout << "\nReszta: " << licz << endl;
}

void ascii(char tab[])
{
    int i = 0;
    while (tab[i] != '\0')
    {
        cout << (int)tab[i] << ' ';
        i++;
    }
}

// A-Z ascii 65-90
// a-z ascii 97-122
void zamiana(char tab[])
{   
    int x = 0;
    int i = 0;
    while (tab[i] != '\0')
    {   
        x = (int)tab[i];
        if ( 65 <= x && x <= 90 )
        {
            x = x + 32;
            cout << (char)x;      
        }
        i++;
    }
}

int main(int argc, char **argv)
{   
    const int rozmiar = 30;  // deklaracja stałej
    char znaki[rozmiar];  // deklaracja tablicy znakowej
    cout << "Jak się nazywasz: ";
    cin.getline(znaki, rozmiar);
	cout << "WITAJ" << znaki << endl;
    //~ licz_znaki(znaki);
    ascii(znaki);
    zamiana(znaki);
    
    
	return 0;
}
 

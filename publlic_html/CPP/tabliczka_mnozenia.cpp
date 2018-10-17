/*
 * bez nazwy.cpp
 */

#include <iostream>
#include <iomanip>

using namespace std;

void tabliczka(int a, int b) 
{
    for (int i = 1; i <= a; i++ ) 
    {
        for (int j = 1; j <= a; j++ )
        {
            cout << setw(4) << i * j;
        }
    }
}


int main(int argc, char **argv)
{
	int a, b; // deklaracja
    a = b = 0; // inicjacja
    cout << "Podaj zakres 1:";
    cin >> a;
    cout << "Podaj zakres 2:";
    cin >> b;
    tabliczka(a, b);
	return 0;
}


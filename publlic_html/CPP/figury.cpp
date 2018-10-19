/*
 * figury.cpp
 * 
 */
 
#include <iostream>

using namespace std;

void prostokat(int x, int y, char z) 
{
    for (int i = 0; i < x; i++ ) {
        for (int j = 0; j < y; j++ )
        
            if (j == 0 || j == y-1 || i == 0 || i == x-1)
                cout << z;
            else
                cout << " ";
        cout << endl;
        }
    
}


int main(int argc, char **argv)
{
	int a, b; // deklaracja
    a = b = 0; // inicjacja
    cout << "Podaj boki prostokąta:";
    cin >> a >> b;
    char znak;
    cout << "Podaj znak:";
    cin >> znak;
    prostokat (a, b, znak);
	return 0;
}


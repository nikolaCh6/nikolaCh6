/*
 * dec2bin.cpp
 */


#include <iostream>
using namespace std;

int dec2bin(int l)
{
    int lbin = 0;
    int i = 1;
    
    while (l > 0)
    {
        lbin += (l%2)*i;
        l = l/2;
        i *= 10;
    }
    return lbin;    
}

int main(int argc, char **argv)
{
    int l = 0;
	cout << "Podaj dowolną liczbę dziesiętną: ";
    cin >> l;
    
    cout << "Liczba binarna: " << dec2bin(l) << endl;
	return 0;
}


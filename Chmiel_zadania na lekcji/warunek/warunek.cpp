/*
 * warunek.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int a, b, c;
    a = b = c = 0;
    
    cout << "Podaj pierwszą liczbę "; 
    cin >> a;
    cout << "Podaj drugą liczbę "; 
    cin >> b;
    cout << "Podaj trzecią liczbę ";
    cin >> c;
    
    if (a>b and a>c) cout << "Największa jest" << a << endl;
    if (b>a and b>c) cout << "Największa jest" << b << endl;
    else cout << "Największa jest" << c << endl; 
        
    return 0;
}


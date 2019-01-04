#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "Podaj pierwsza liczbe: ";
    cin >> a;
    cout << a;
      
    cout << endl << "Podaj druga liczbe: ";
    cin >> b;
    cout << b;
    
    cout << endl << "Suma: " << a + b << endl;
    cout << endl << "Różnica: " << a - b << endl;
    cout << endl << "Iloraz: " << a / b << endl;
    cout << endl << "Iloczyn: " << a * b << endl;
    
	return 0;
}

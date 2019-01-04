/*
 * lpierwsza.cpp
 * 
 */


#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj n: ";
    cin >> n;
    for (int i = 2; i * i <= n; i++)
{
        if ( n % i == 0)
{            
            cout << "Złożona";
            return;
            }
        }
        if ( n % i == 0)
	return 0;
}



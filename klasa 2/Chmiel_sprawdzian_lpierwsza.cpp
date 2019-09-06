/*
 * Chmiel_lpierwsza.cpp
 */

#include <iostream>
#include <cstdlib>

using namespace std;


bool pierwsza(int n)
{
    if(n<2)
            return false;
    for(int i=2; i*i<=n; i++)
            if(n%i==0)
                return false;
    return true;
}

int main(int argc, char **argv)
{
    int n;
    
    cout << "Prosze o podanie liczby: ";
    cin >> n;
    
    if(pierwsza(n))
    
        cout << "Liczba " << n << " Jest liczbą pierwszą " << endl;
    else
        cout << "Liczba " << n << " Nie jest liczbą pierwszą " << endl;
     
    return 0;
}

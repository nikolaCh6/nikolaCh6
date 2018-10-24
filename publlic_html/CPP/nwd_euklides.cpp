#include <iostream>
using namespace std;
 
int nwd_klasyczny(int a, int b)
{   
    int licznik = 0;
    while (a != b)
    {   
        if (a > b)
            a = a - b;
        else
            b = b - a;
        licznik++;
    }
    cout << "Powtórzeń klasyczny: " << licznik << endl;
    return a;
}

int nwd_optymalny(int a, int b)
{   
    int licznik = 0;
    while (a > 0)
    {
            a = a % b;
            b = b - a;
            licznik++;
    }
    cout << "Powtórzeń optymalny: " << licznik << endl;
    return b;
}

int main()
{
    int a,b;
        cout << "Podaj a: ";
        cin >> a;
        cout << "Podaj b: ";
        cin >> b;
        cout << nwd_optymalny(a, b) << endl;
        cout << nwd_klasyczny(a, b);
   
    return 0;
}




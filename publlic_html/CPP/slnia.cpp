/*
 * potenga.cpp
 * 
 */


#include <iostream>
using namespace std;

// n! = 1 dla n = 0
// n! = 1 * ... * n
// 4! = 3! * 4
//3! = 2! * 3
// n! = (n-1)! * n 

int silnia_re(int n)
{
  if (n == 0) return 1;
   return silnia_re(n-1) * n;
}

int main(int argc, char **argv)
{
    int n;
    cout << "Podaj liczbę: "; cin >> n;
    cout << "Wynik: " << silnia_re(n);
	return 0;
}


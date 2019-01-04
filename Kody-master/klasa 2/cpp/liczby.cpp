/*
 * liczby.cpp
 */


#include <iostream>
#include <iomanip>

using namespace std;

int liczby2()
{
   int ile = 0;
   
   for (int i = 1; i < 10; i++)
    {
        for(int j = 0; j < 10; j++)
        {
            if (i != j)
            {
            cout << i << j << " ";
            ile++;
            }
        }
        cout << endl;
    }
    return ile;
}

int liczby3()
{
   int ile = 0;
   
   for (int i = 1; i < 10; i++)
    {
        for(int j = 0; j < 10; j++)
        {
            for (int k = 0; k < 10; k++)
            {
                if (i != j && i != k && j != k)
                {
                    cout << i << j << k << " ";
                    ile++;
                }
            }
        }
        cout << endl;
    }
    return ile;
}

int main(int argc, char **argv)
{
    cout << "\n\nLiczb 2-cyfrowych: " << liczby2() << endl;
    cout << "\n\nLiczb 3-cyfrowych: " << liczby3() << endl;
    
	return 0;
}

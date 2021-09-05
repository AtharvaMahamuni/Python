#include <iostream>
using namespace std;

int main()
{

    int p;
    cin >> p;

    if (p >= 200 && p <= 100)
    {
        cout << "INVALID INPUT";
    }

    int n = 0;
    if (p % 4 == 0)
    {
        for (int i = 0; i < 4; i++)
        {
            cout << p / 4 << endl;
        }
    }
    else
    {
        while (p % 4 == 0)
        {
            n++;
            p--;
        }
        for (int i = 0; i < 3; i++)
        {
            cout << p / 4 << endl;
        }
        cout << p / 4 + n << endl;
    }

    return 0;
}
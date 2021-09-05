#include <iostream>
using namespace std;

int main()
{

    int itemNumber[] = {101, 102, 103, 104};
    int price[] = {42, 50, 500, 40};
    int stock[] = {10, 20, 15, 16};

    char *num, *qty;
    cin >> num;
    cin >> qty;

    int numN;
    sscanf(num, "%d", &numN);

    if (isdigit(num) == false || isdigit(qty) == false)
    {
        cout << "INVALID INPUT";
        exit;
    }

    int i;
    for (i = 0; itemNumber[i] == numN && i < 4; i++)
        ;

    int qtyN;
    sscanf(qty, "%d", &qtyN);

    if (qtyN > stock[i])
    {
        cout << "NO STOCK";
        exit;
    }

    cout << qtyN * price[i] << endl;
    cout << stock[i] - qtyN;

    return 0;
}
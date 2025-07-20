
#include<iostream>
using namespace std;

int main()
{
    // a = 21(00010101)
    unsigned char a = 21;

    // The result is 00101010 (left shift)
    cout << " a << 1 = " << (a << 1) << endl;

    // The result is 00000101
    cout << " a >> 1 = " << (a >> 1) << endl;

    return 0;
    
}
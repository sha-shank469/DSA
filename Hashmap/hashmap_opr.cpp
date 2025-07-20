#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    unordered_map <int,int> ump = {
        {1,1}, 
        {2,1}, 
        {4,2}
    };

    for (auto i: ump)
    {
        cout << " First " <<i.first<< " Second " << i.second <<endl;
    }

    


    return 0;
}
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool areDisjoint(vector<int> &a, vector<int> &b){

    unordered_map<int, int> st;

    for(int ele: a)
    {
        st[ele]++;
    }
    for (int i : b)
    {
        if(st.find(i) != st.end())
        {
            return false;
        }
    }

    return true;
}

int main()
{
    vector<int> a = {12, 34, 11, 9, 3};
    vector<int> b = {7, 2, 1, 5};

    bool output = areDisjoint(a,b);
    cout << output << endl;

    return 0;
}
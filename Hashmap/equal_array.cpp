#include<iostream>
#include<bits/stdc++.h>

using namespace std;

bool checkequal(vector <int> &a, vector <int> &b){

    int n = a.size(); 
    int m = b.size();

    unordered_map<int,int> ump;

    if (n != m){
        return false;
    }

    for(auto i : a)
    {
        ump[a[i]]++;
    }

    for (int i=0;i<n;i++)
    {
        if (ump.find(b[i]) == ump.end())
        {
            return false;
        }
        if (ump[b[i]] == 0)
        {
            return false;
        }
        ump[b[i]] --;
    }   

    return true;

}

int main()
{

    vector<int> a = {3, 5, 2, 5, 2};
    vector<int> b = {2, 3, 5, 5, 2};

    bool output = checkequal(a,b);

    cout << output << endl;


    return 0;

}
#include<iostream>
#include<bits/stdc++.h>

using namespace std;


bool isSubset(vector<int>&a, vector<int>&b){

    unordered_map<int,int> hash;

    for(int num: a)
    {
        hash[num]++;
    }

    for (int num: b)
    {
        if (hash[num] > 0)
        {
            hash[num] --; 
        }
        else{
            return false;
        }
    }
    return true;
}   


int main()
{
    vector <int> a = {11, 1, 13, 21, 3, 7};
    vector <int> b = {11, 3, 7, 1 };

    bool output = isSubset(a,b);
    cout << output << endl;
    return 0;

}
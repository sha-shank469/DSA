#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int findDuplicate(vector<int> &arr, int n){
    
    vector <int> hashtable (n, -1);

    for (int i: arr)
    {
        if (hashtable[i] != -1){

            // duplicate found
            return i;
        }
        
        else{
            hashtable[i] = i;
        }
    }
    return -1;
}



int main()
{
    vector<int> v;
    int n;
    cin >> n;

    for(int i=0; i<n; i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }

    int output = findDuplicate(v,n);

    cout << "output: " << output << endl;

    return 0;
}
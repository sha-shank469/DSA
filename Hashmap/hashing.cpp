
#include<iostream>
#include<bits/stdc++.h>
using namespace std;


int main()
{
    int n;
    cin >> n;

    int arr[n];
    for (int i=0;i<n;i++)
    {
        cin >> arr[i];

    }
    
    map<int, int> mpp;
    for (int i=0; i<n; i++)
    {
        mpp[arr[i]]++; /*map stores all the value in sorted order*/
    }


    // iterating the map
    for (auto it: mpp)
    {
        cout << it.first << "->" << it.second << endl;
    }


    int q;
    cin >> q;
    while(q--)
    {
        int number;
        cin >> number;
        //fetch
        cout << mpp[number] << endl;
    }

    return 0;
}


// int main() 
// {   
//     int n;
//     cin >> n;

//     int arr[n];
//     for (int i=0; i<n; i++)
//     {
//         cin >> arr[i];
//     }
    
//     // precompute
//     int hash[1000000] = {0};
//     for(int i = 0; i < n; i++)
//     {
//         hash[arr[i]] += 1;

//         // here hash array is ready
//     }

//     int q;
//     cin >> q;
//     while(q--){
//         int number;
//         cin >> number;

//         cout << hash[number] << endl;
//         // fetch
//     }

//     return 0;
// }
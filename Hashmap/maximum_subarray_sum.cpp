#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n];

    for(int i=0;i<n;i++)
    {
        cin >> arr[i];
    }
    
    int res = arr[0];
    // cout << res << endl;
    for (int i=0;i<n;i++)
    {
        int curr_sum = 0;

        for (int j=i; j<n; j++)
        {
            curr_sum += arr[j];
            res = max(res,curr_sum);
        }
        
    }
    cout << res << endl;
    return res;
}
#include<bits/stdc++.h>
#include<iostream>

using namespace std;


int firstMissing(int arr[], int n)
{
    int hasharr[n+2] = {0};

    for(int i=0; i<n; i++)
    {
        if (arr[i] > 0 && arr[i] <= n)
        {
            hasharr[arr[i]] = 1;
        } 
    }

    for (int i=1; i<=n; i++)
    {
        if(hasharr[i] == 0)
        {
            return i;
        }
    }

    return n+1;
}


int main()
{

    int n;
    cin >> n;
    int arr[n];

    for (int i=0;i<n;i++){
        cin >> arr[i];
    }

    int output = firstMissing(arr, n);
    cout << output << endl;
    
    return 0;
}
#include<iostream>
#include<bits/stdc++.h>
using namespace std;


int findAllSubarraysWithGivenSum(vector < int > & arr, int k) {
    // Write Your Code Here
    int count = 0;
    int n = arr.size();

    for (int i = 0; i < n; i++)
    {
        int curr_sum = 0;

        for (int j=i; j<n; j++)
        {
            curr_sum += arr[j];
            if (curr_sum == k)
            {
                count ++;
            }
        }
    }
    return count;
}

int main()
{

    vector<int> v;
    int n;
    cin >> n;

    int k;
    cin >> k;

    for (int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        v.push_back(x);

    }
    int output = findAllSubarraysWithGivenSum(v,k);
    return 0;
}

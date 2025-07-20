#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int getLongestSubarray(vector<int>& nums, int k){

    unordered_map<int, int> ump;
    int sum = 0;
    int res = 0;

    for (int i=0; i<nums.size(); ++i)
    {
        sum += nums[i];
        if (sum == k)
            res = res + 1;
        if (ump.count(sum-k))
            res = max(res, i-ump[sum-k]);
        if (!ump.count(sum))
            ump[sum] = i;
    }

    return res;

}

int main()
{
    vector <int> v;
    int n;
    cin >> n;

    int k;
    cin >> k;

    for(int i=0; i<n; i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }
    
    int output = getLongestSubarray(v,k);
    cout << output << endl;


    return 0;
}




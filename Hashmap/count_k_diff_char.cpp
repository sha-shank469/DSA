#include<iostream>
using namespace std;
#include<bits/stdc++.h>


int countSubStrings(string str, int k) 
{
    int n = str.length();
    int ans = 0;

    for (int i=0;i<n;i++)
    {
        vector <bool> map(26,0);
        int distinct_cnt = 0;
        for(int j=i;j<n;j++){
            if (map[str[j]-'a'] == false){
                map[str[j]-'a'] == true;
                distinct_cnt++;
            }
            if(distinct_cnt == k) ans ++;
        }
    }
    return ans;
}

int main()
{
    string s = "abcad";
    int k = 2;
    cout << countSubStrings(s,k) << endl;
    return 0;
}
#include<iostream>
#include<bits/stdc++.h>

using namespace std;

void reverseArray(vector<int> &arr , int n) {
    
    int start = 0;
    int end = arr.size() - 1;

    while(start < end){
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start ++;
        end --;

    }
    
    // cout << "Array after reversing from position " << m + 1 << ":\n";
    for (int num : arr) {
        cout << num << " ";
    }
    cout << endl;

}

int main()
{
    int n;
    cin >> n;

    // int M;
    // // cout << "Position to reverse from" << endl;
    // cin >> M;

    vector<int>v;
    
    for (int i=0;i<n;i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }

    reverseArray(v,n);
    return 0;
}
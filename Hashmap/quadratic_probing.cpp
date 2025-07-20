
#include<iostream>
#include <bits/stdc++.h> 
using namespace std;

vector<int> quadraticProbing(vector<int> &keys, int n)
{
   vector <int> hashtable(n, -1);

   for (int key: keys)
   {
        int hashindex = key % n;
        if (hashtable[hashindex] == -1)
        {
            hashtable[hashindex] = key;
        }
        else{
            // Collision: Apply Quadratic Probing
            bool placed = false;
            for(int i = 1; i < n; i++)
            {
                int newIndex = (hashindex + i*i) % n;
                if (hashtable[newIndex] == -1)
                {
                    hashtable[newIndex] = key;
                    placed = true;
                    break;
                }
            }

        }
   }
   return hashtable;

}

int main()
{   
    vector<int> v;
    int n;
    cin >> n;

    for(int i=0; i<n ;i++)
    {
        int x;
        cin >> x;
        v.push_back(x);
    }

    vector<int> output = quadraticProbing(v,n);

    for (int val: output)
    {
        cout << val << endl;
    }
    cout << endl;

    return 0;
}
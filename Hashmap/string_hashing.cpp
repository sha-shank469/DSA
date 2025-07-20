
#include<iostream>
#include<string>
using namespace std;

int main()
{
    string s;
    cin >> s;
    
    // int hash[26] = {0};
    int hash[256] = {0};

    for (int i=0; i < s.size(); i++){
        // hash[s[i]-'a'] ++;
        hash[s[i]] ++;

    }

    int q;
    cin >> q;
    while(q--)
    {
        char c;
        cin >> c;
        // cout << hash[c-'a'] << endl;
        cout << hash[c] << endl;

    }

    return 0;
}


// my solution
// int main()
// {

//     int hash[26] = {0};

//     string s = "shashank";

//     for(int i = 0; i < s.length(); i++)
//     {
//         int number = s[i] - 'a';
//         hash[s[i] - 'a'] += 1;
//     }

//     for(int i = 0; i < 26; i++)
//     {
//         if(hash[i] > 0)
//         {
//             char ch = i + 'a';
//             cout << ch << " count: " << hash[i] << endl;
//         }
//     }


//     return 0;
// }
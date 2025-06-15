#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for(int i = 0; i < n; ++i)
        cin >> arr[i];

    map<int, int> freq;
    multiset<pair<int, int>> s; // (frequency, -value)

    for(int i = 0; i < k; ++i) {
        int val = arr[i];
        if(freq[val] == 0) {
            freq[val] = 1;
            s.insert({1, -val});
        } else {
            s.erase(s.find({freq[val], -val}));
            freq[val]++;
            s.insert({freq[val], -val});
        }
    }

    cout << -s.rbegin()->second << " ";

    for(int i = k; i < n; ++i) {
        int in = arr[i];
        int out = arr[i - k];

        // Add new element
        if(freq[in] == 0) {
            freq[in] = 1;
            s.insert({1, -in});
        } else {
            s.erase(s.find({freq[in], -in}));
            freq[in]++;
            s.insert({freq[in], -in});
        }

        // Remove outgoing element
        s.erase(s.find({freq[out], -out}));
        freq[out]--;
        if(freq[out] > 0)
            s.insert({freq[out], -out});

        cout << -s.rbegin()->second << " ";
    }

    return 0;
}

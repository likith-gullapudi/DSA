#include <iostream>
#include <vector>
#include <set>
#include <map>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i)
        cin >> arr[i];

    set<int> s;
    map<int, int> freq;

    // Pre-fill set with all possible values (Mex candidates)
    for (int i = 0; i <= n + 10; ++i)
        s.insert(i);

    // Initial window
    for (int i = 0; i < k; ++i) {
        if (freq[arr[i]] == 0) {
            s.erase(arr[i]);
        }
        freq[arr[i]]++;
    }

    cout << *s.begin() << " ";

    for (int i = k; i < n; ++i) {
        int in = arr[i];
        int out = arr[i - k];

        // Add new element
        if (freq[in] == 0)
            s.erase(in);
        freq[in]++;

        // Remove old element
        freq[out]--;
        if (freq[out] == 0)
            s.insert(out);

        cout << *s.begin() << " ";
    }

    return 0;
}

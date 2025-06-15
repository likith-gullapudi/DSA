#include <bits/stdc++.h>
using namespace std;

#define FAST_IO ios_base::sync_with_stdio(false); cin.tie(0);

int main() {
    FAST_IO;

    int n;
    cin >> n;

    vector<vector<int>> arr(n, vector<int>(3));
    multiset<int> end;

    // Read input and store intervals
    for (int i = 0; i < n; ++i) {
        cin >> arr[i][0] >> arr[i][1];
        arr[i][2] = i;  // Store the original index
        end.insert(arr[i][1]);
    }

    // Sort the intervals based on start time
    sort(arr.begin(), arr.end());

    vector<vector<int>> ans(2, vector<int>(n, 0));
    multiset<int> new_end;

    // Process intervals
    for (int i = 0; i < n; ++i) {
        int st = arr[i][0], en = arr[i][1], index = arr[i][2];

        // Remove the current end point
        end.erase(end.find(en));

        // Find the largest end that is <= current start
        auto it = end.lower_bound(en);
        if (it != end.begin()) {
            --it;
            ans[0][index] = 1;
        }

        // Find the smallest end that is >= current start
        it = new_end.lower_bound(en);
        if (it != new_end.end()) {
            ans[1][index] = 1;
        }

        // Add the current end to the new_end set
        new_end.insert(en);
    }

    // Print the result
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << ans[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}

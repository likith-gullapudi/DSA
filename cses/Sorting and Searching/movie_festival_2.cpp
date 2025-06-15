#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> movies(n);
    for (int i = 0; i < n; ++i) {
        cin >> movies[i].first >> movies[i].second;
    }

    // Sort by movie end times
    sort(movies.begin(), movies.end(),
        [](const pair<int, int> &a, const pair<int, int> &b) {
            return a.second < b.second;
        });

    multiset<int> watchers;
    for (int i = 0; i < k; ++i) watchers.insert(0); // All watchers free at time 0

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int start = movies[i].first;
        int end = movies[i].second;

        auto it = watchers.upper_bound(start);
        if (it == watchers.begin()) continue; // No watcher free before movie starts
        --it; // Get the latest watcher who is free before or at `start`
        watchers.erase(it); // Remove old end time
        watchers.insert(end); // Add new end time
        ++ans;
    }

    cout << ans << endl;
    return 0;
}

#include <iostream>
#include <set>
#include <vector>

using namespace std;

class Map {
    multiset<int> ms;

public:
    pair<int, int> insert(int val) {
        int lesser = distance(ms.begin(), ms.lower_bound(val));
        int greater = distance(ms.upper_bound(val), ms.end());
        ms.insert(val);
        return {lesser, greater};
    }

    pair<int, int> remove(int val) {
        auto it = ms.find(val);
        if (it == ms.end()) return {-1, -1};
        int lesser = distance(ms.begin(), ms.lower_bound(val));
        int greater = distance(ms.upper_bound(val), ms.end());
        ms.erase(it);  // Only removes one occurrence
        return {lesser, greater};
    }
};

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int &x : arr) cin >> x;

    Map obj;
    int count = 0;

    for (int i = 0; i < k; ++i) {
        count += obj.insert(arr[i]).second;
    }
    cout << count << " ";

    for (int i = k; i < n; ++i) {
        count -= obj.remove(arr[i - k]).first;
        count += obj.insert(arr[i]).second;
        cout << count << " ";
    }

    return 0;
}

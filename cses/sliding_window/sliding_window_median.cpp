#include <iostream>
#include <vector>
#include <set>
using namespace std;

class SlidingMedian {
    multiset<int> low, high;

    void balance() {

        while (low.size() > high.size() + 1) {
            auto it = prev(low.end());
            high.insert(*it);
            low.erase(it);
        }
        while (high.size() > low.size()) {
            low.insert(*high.begin());
            high.erase(high.begin());
        }
    }

public:
    void insert(int val) {
        if (!low.empty() && val <= *prev(low.end()))
            low.insert(val);
        else
            high.insert(val);
        balance();
    }

    void remove(int val) {
        if (!low.empty() && val <= *prev(low.end())) {
            auto it = low.find(val);
            if (it != low.end()) low.erase(it);
        } else {
            auto it = high.find(val);
            if (it != high.end()) high.erase(it);
        }
        balance();
    }

    int median() {
        return *prev(low.end());
    }
};

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int &x : arr) cin >> x;

    SlidingMedian sm;
    for (int i = 0; i < k; ++i)
        sm.insert(arr[i]);

    cout << sm.median() << " ";

    for (int i = k; i < n; ++i) {
        sm.remove(arr[i - k]);
        sm.insert(arr[i]);
        cout << sm.median() << " ";
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

class Map {
    multiset<int> low, high;
    long long sum_low = 0, sum_high = 0;

    void balance() {
        while (high.size() > low.size()) {
            int val = *high.begin();
            high.erase(high.begin());
            sum_high -= val;
            low.insert(val);
            sum_low += val;
        }
        while (low.size() > high.size() + 1) {
            auto it = prev(low.end());
            int val = *it;
            low.erase(it);
            sum_low -= val;
            high.insert(val);
            sum_high += val;
        }
    }

public:
    void insert(int val) {
        if (!low.empty() && val > *prev(low.end())) {
            high.insert(val);
            sum_high += val;
        } else {
            low.insert(val);
            sum_low += val;
        }
        balance();
    }

    void remove(int val) {
        if (!low.empty() && val <= *prev(low.end())) {
            auto it = low.find(val);
            if (it != low.end()) {
                low.erase(it);
                sum_low -= val;
            }
        } else {
            auto it = high.find(val);
            if (it != high.end()) {
                high.erase(it);
                sum_high -= val;
            }
        }
        balance();
    }

    int median() {
        balance();
        return *prev(low.end());
    }

    long long cost() {
        int med = median();
        return 1LL * med * (int)low.size() - sum_low + sum_high - 1LL * med * (int)high.size();
    }
};

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) cin >> arr[i];

    Map obj;
    for (int i = 0; i < k; ++i) obj.insert(arr[i]);
    cout << obj.cost() << " ";

    for (int i = k; i < n; ++i) {
        obj.remove(arr[i - k]);
        obj.insert(arr[i]);
        cout << obj.cost() << " ";
    }
    cout << endl;
    return 0;
}

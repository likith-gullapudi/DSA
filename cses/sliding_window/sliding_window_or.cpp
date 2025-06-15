#include <iostream>
#include <vector>
#include <deque>
using namespace std;

// Extract bit vector from number x efficiently
vector<int> get_bits(long long x) {
    vector<int> bits(32, 0);
    int j = 0;
    while (x > 0) {
        if (x & 1)
            bits[j] = 1;
        x >>= 1;
        ++j;
    }
    return bits;
}

int main() {
    long long n, k;
    cin >> n >> k;

    long long x, a, b, c;
    cin >> x >> a >> b >> c;

    vector<int> count(32, 0);     // Count of bits set in current window
    deque<vector<int>> window;    // Store bit pattern of last k elements
    long long ans = 0, xor_sum = 0;

    // Process first k elements
    for (long long i = 0; i < k; ++i) {
        vector<int> bits = get_bits(x);
        for (int j = 0; j < 32; ++j) {
            if (bits[j]) count[j]++;
        }
        window.push_back(bits);
        x = (a * x + b) % c;
    }

    // Compute initial answer
    for (int j = 0; j < 32; ++j) {
        if (count[j] > 0)
            ans |= (1LL << j);
    }
    xor_sum = ans;

    // Slide the window from k to n-1
    for (long long i = k; i < n; ++i) {
        // Remove oldest bits
        const vector<int>& old_bits = window.front();
        for (int j = 0; j < 32; ++j) {
            if (old_bits[j]) count[j]--;
        }
        window.pop_front();

        // Add new bits
        vector<int> new_bits = get_bits(x);
        for (int j = 0; j < 32; ++j) {
            if (new_bits[j]) count[j]++;
        }
        window.push_back(new_bits);

        // Compute new ans
        ans = 0;
        for (int j = 0; j < 32; ++j) {
            if (count[j] > 0)
                ans |= (1LL << j);
        }

        xor_sum ^= ans;

        // Update x for next iteration
        x = (a * x + b) % c;
    }

    cout << xor_sum << endl;
    return 0;
}

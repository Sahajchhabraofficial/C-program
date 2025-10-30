//wap to make pascal's triangle.
#include<iostream>
using namespace std;
int main()
{
    int n;
    const int MAX_ROWS = 32;
    const unsigned long long MAXV = ~0ULL;

    for (int i = 0; i < MAX_ROWS; ++i) {
        for (int s = 0; s < MAX_ROWS - i - 1; ++s) cout << "  ";
        unsigned long long val = 1;
        bool overflow = false;
        for (int j = 0; j <= i; ++j) {
            cout << val << " ";
            if (j < i) {
                __int128 next = (__int128)val * (i - j) / (j + 1);
                if (next > MAXV) { overflow = true; break; }
                val = (unsigned long long)next;
            }
        }
        cout << endl;
        if (overflow) break;
    }

    return 0;
}
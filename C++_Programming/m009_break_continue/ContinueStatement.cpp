//
// Created by Kelvin HT on 2/12/22.
//

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Input n: "; cin >> n;

    for (int i = 0; i < n; ++i) {
        if ((i + 1) % 2 == 0) {
            continue;
        }
        cout << (i + 1) << " ";
    }
    cout << endl;

    return 0;
}

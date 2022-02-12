//
// Created by Kelvin HT on 2/12/22.
//

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Input n: "; cin >> n;

    int i = 0;
    do {
        cout << (i + 1) << " ";
        i++;
    } while (i < n);

    cout << endl;

    return 0;
}

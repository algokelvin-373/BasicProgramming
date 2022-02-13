//
// Created by Kelvin HT on 2/12/22.
//

#include <iostream>
using namespace std;

int main() {
    int dtNumber;

    cout << "Input number: ";
    cin >> dtNumber;

    if (dtNumber < 0) {
        cout << "Your number is negative" << endl;
    } else {
        cout << "Your number is positive" << endl;
    }

    return 0;
}

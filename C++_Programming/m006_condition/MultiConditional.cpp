//
// Created by Kelvin HT on 2/12/22.
//

#include <iostream>
using namespace std;

int main() {
    int dtNumber;

    cout << "Input number: ";
    cin >> dtNumber;

    if (dtNumber % 2 == 0) {
        cout << "Your number can be divided by 2" << endl;
    } else if (dtNumber % 3 == 0) {
        cout << "Your number can be divided by 3" << endl;
    } else {
        cout << "Your number can't be divided by 2 or 3" << endl;
    }

    return 0;
}

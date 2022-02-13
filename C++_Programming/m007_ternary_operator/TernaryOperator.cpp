//
// Created by Kelvin HT on 2/12/22.
//

#include <iostream>
using namespace std;

int main() {
    int dtNumber;

    cout << "Input number: ";
    cin >> dtNumber;

    string result = (dtNumber < 0) ? "Negative" : "Positive";
    cout << dtNumber << " is " << result << endl;

    return 0;
}

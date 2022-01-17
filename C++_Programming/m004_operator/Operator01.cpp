//
// Created by AlgoKelvin on 1/16/22.
//

#include <iostream>
using namespace std;

int main() {
    // Arithmetic Operator
    int x = 10, y = 4;

    int addition = x + y;
    int subtraction = x - y;
    int multiplication = x * y;
    int division = x / y;
    int modulus = x % y;

    cout << x << " + " << y << " = " << addition << endl;
    cout << x << " - " << y << " = " << subtraction << endl;
    cout << x << " * " << y << " = " << multiplication << endl;
    cout << x << " / " << y << " = " << division << endl;
    cout << x << " % " << y << " = " << modulus << endl;

    return 0;
}

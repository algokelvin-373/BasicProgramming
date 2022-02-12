//
// Created by AlgoKelvin on 1/16/22.
//

#include <iostream>
using namespace std;

int main() {
    // Assignment Operator
    int x = 1;
    cout << "The 'x' is " << x << endl;

    x += 5; // Same to -> x = x + 5
    cout << "The 'x' now is " << x << endl;

    x *= 3; // Same to -> x = x * 3
    cout << "The 'x' now is " << x << endl;

    x -= 5; // Same to -> x = x - 5
    cout << "The 'x' now is " << x << endl;

    x /= 2; // same to -> x = x / 2
    cout << "The 'x' now is " << x << endl;

    return 0;
}

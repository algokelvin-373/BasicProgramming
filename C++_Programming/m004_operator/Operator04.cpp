//
// Created by AlgoKelvin on 1/16/22.
//

#include <iostream>
using namespace std;

int main() {
    // Comparison Operator
    int x = 1, y = 5, z = 1;
    int a = 5, b = -5, c = 10;

    // The value: 0 is false, 1 is true
    cout << "x == y -> " << (x == y) << endl;
    cout << "x == z -> " << (x == z) << endl;
    cout << "x != y -> " << (x != y) << endl;
    cout << "x != z -> " << (x != z) << endl;
    cout << "x < y -> " << (x < y) << endl;
    cout << "x < b -> " << (x < b) << endl;
    cout << "y > z -> " << (y > z) << endl;
    cout << "y > c -> " << (y > c) << endl;
    cout << "x <= y -> " << (x <= y) << endl;
    cout << "x <= z -> " << (x <= z) << endl;
    cout << "y >= z -> " << (y >= z) << endl;
    cout << "y >= a -> " << (y >= a) << endl;

    return 0;
}

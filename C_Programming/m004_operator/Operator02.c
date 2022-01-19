//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {

    // Operator Increment (++) And Decrement (--)
    int a = 10, b = 4;
    printf("Before : a = %d >-< b = %d \n", a, b);
    printf("After  : a = %d >-< b = %d \n", a--, b++);

    printf("Before : a = %d >-< b = %d \n", a, b);
    printf("After  : a = %d >-< b = %d \n", --a, ++b);

    return 0;
}

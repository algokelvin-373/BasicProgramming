//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {

    int number;
    printf("Input Your Number : ");
    scanf("%d", &number);

    // Single Conditional ( If )
    if (number % 2 == 0) {
        printf("%d is even number \n", number);
    }
    printf("The program is done");

    return 0;
}

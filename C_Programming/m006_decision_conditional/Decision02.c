//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {

    int number;
    printf("Input Your Number : ");
    scanf("%d", &number);

    // Double Conditional ( If - Else )
    if (number % 2 == 0) {
        printf("%d is even number \n", number);
    } else {
        printf("%d is odd number \n", number);
    }

    return 0;
}

//
// Created by Kelvin HT on 1/20/22.
//

#include <stdio.h>

int main() {
    int number;
    printf("Input Your Number : ");
    scanf("%d", &number);

    if (number % 2 == 0) {
        printf("%d can be divided by 2 \n", number);
        if (number > 0) {
            printf("%d is positive \n", number);
        } else {
            printf("%d is negative \n", number);
        }
    } else if (number % 3 == 0) {
        printf("%d can be divided by 3 \n", number);
        if (number % 6 == 0) {
            printf("%d can be divided by 6 \n", number);
        } else {
            printf("%d can't be divided by 6 \n", number);
        }
    } else {
        printf("%d can't be divided by 2 or 3 \n", number);
    }

    return 0;
}

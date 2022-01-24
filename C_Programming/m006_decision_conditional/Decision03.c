//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {

    int number;
    printf("Input Your Number : ");
    scanf("%d", &number);

    // Multi Conditional ( If - Else If _ Else )
    if (number % 2 == 0) {
        printf("%d can be divided by 2 \n", number);
    } else if (number % 3 == 0) {
        printf("%d can be divided by 3 \n", number);
    } else {
        printf("%d can't be divided by 2 or 3 \n", number);
    }

    return 0;
}

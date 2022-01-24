//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {

    int number;
    printf("Input Your Number : ");
    scanf("%d", &number);

    switch (number) {
        case 1:
            printf("You Input Number 1");
            break;
        case 2:
            printf("You Input Number 2");
            break;
        default:
            printf("You Input Another number");
    }

}

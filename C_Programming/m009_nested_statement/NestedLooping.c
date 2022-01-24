//
// Created by Kelvin HT on 1/20/22.
//

#include <stdio.h>

int main() {
    // Create Triangle

    int n;
    printf("Input n : ");
    scanf("%d", &n);

    // Nested Looping
    for (int x = 0; x < n; x++) {
        for (int y = 0; y <= x; y++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}

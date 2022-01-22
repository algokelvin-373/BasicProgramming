//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {
    // Arithmetic: 1, 2, 3, 4, 5, ...
    int n;
    printf("Input n : ");
    scanf("%d", &n);

    // Looping 'while'
    int x = 0;
    while (x < n) {
        printf("%d ", (x + 1));
        x++;
    }
    printf("\n");
}

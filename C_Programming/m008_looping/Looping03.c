//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {
    // Arithmetic: 1, 2, 3, 4, 5, ...
    int n;
    printf("Input n : ");
    scanf("%d", &n);

    // Looping 'do-while'
    int x = 0;
    do {
        printf("%d ", (x + 1));
        x++;
    } while (x < n);
    printf("\n");
}

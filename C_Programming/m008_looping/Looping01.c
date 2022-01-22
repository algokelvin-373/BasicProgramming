//
// Created by Kelvin HT on 1/19/22.
//

#include <stdio.h>

int main() {

    // Arithmetic: 1, 2, 3, 4, 5, ...
    int n;
    printf("Input n : ");
    scanf("%d", &n);

    // Looping 'for'
    for (int x = 0; x < n; x++) {
        printf("%d ", (x + 1));
    }
    printf("\n");

}

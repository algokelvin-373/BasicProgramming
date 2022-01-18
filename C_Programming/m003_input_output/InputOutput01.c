//
// Created by Kelvin HT on 1/18/22.
//

#include <stdio.h>

int main() {

    // Input Number - Must be using '&'
    int number;
    printf("Input Your Number : ");
    scanf("%d", &number);

    // Input String - Using 'char' with capacity
    char text[50];
    printf("Input Your Text   : ");
    scanf("%s", text);

    printf("Number : %d \n", number);
    printf("Text   : %s \n", text);

    return 0;
}


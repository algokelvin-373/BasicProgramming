package com.codingday;

import java.util.Scanner;

public class CodingJavaDay19 {
    public static void main(String[] args) {
        // Rectangle Style
        Scanner input = new Scanner(System.in);
        System.out.print("Input n: ");
        int n = input.nextInt();

        for (int x = 1; x <= n; x++) {
            for (int y = 1; y <= n; y++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}

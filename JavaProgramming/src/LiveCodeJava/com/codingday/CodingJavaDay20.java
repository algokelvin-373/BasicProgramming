package com.codingday;

import java.util.Scanner;

public class CodingJavaDay20 {
    public static void main(String[] args) {
        // Triangle Style
        Scanner input = new Scanner(System.in);
        System.out.print("Input n: ");
        int n = input.nextInt();

        for (int x = 1; x <= n; x++) {
            for (int y = 1; y <= n-x; y++) {
                System.out.print(" ");
            }
            for (int z = 1; z < 2*x; z++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}

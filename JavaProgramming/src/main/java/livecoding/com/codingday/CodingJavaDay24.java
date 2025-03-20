package com.codingday;

import java.util.Scanner;

public class CodingJavaDay24 {
    public static void main(String[] args) {
        // Triangle Style 2
        Scanner input = new Scanner(System.in);
        System.out.print("Input n: ");
        int n = input.nextInt();

        for (int x = 1; x <= n; x++) {
            for (int y = 1; y <= n-x; y++) {
                System.out.print(" ");
            }
            for (int z = 1; z < 2*x; z++) {
                if (x == n)
                    System.out.print("*");
                else {
                    if (z == 1 || z == 2*x - 1)
                        System.out.print("*");
                    else
                        System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}

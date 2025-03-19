package com.codingday;

import java.util.Scanner;

public class CodingJavaDay23 {
    public static void main(String[] args) {
        // Rectangle Style 2
        Scanner input = new Scanner(System.in);
        System.out.print("Input n: ");
        int n = input.nextInt();

        for (int x = 1; x <= n; x++) {
            for (int y = 1; y <= n; y++) {
                if (x == 1 || x == n)
                    System.out.print("*");
                else {
                    if (y == 1 || y == n)
                        System.out.print("*");
                    else
                        System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}

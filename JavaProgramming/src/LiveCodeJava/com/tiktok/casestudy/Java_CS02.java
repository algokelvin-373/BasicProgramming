package com.tiktok.casestudy;

import java.util.Scanner;

public class Java_CS02 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input n: ");
        int n = input.nextInt();

        for (int x = 1; x <= n; x++) {
            for (int y = n - x; y >= 1; y--) {
                System.out.print(" ");
            }
            for (int z = 1; z <= 2*x - 1; z++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int x = 1; x < n; x++) {
            for (int y = 1; y <= x; y++) {
                System.out.print(" ");
            }
            for (int z = 1; z <= 2*(n-x) - 1; z++) {
                System.out.print("*");
            }
            System.out.println();
        }

    }
}

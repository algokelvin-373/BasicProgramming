package com.tiktok.casestudy;

import java.util.Scanner;

public class Java_CS003 {
    public static void main(String[] args) {
        // Diamond Style 2
        Scanner input = new Scanner(System.in);
        System.out.print("Input n: ");
        int n = input.nextInt();

        for (int x = 1; x <= n; x++) {
            for (int y = x; y <= n; y++) {
                System.out.print(" ");
            }
            for (int z = 1; z <= 2*x - 1; z++) {
                if (z == 2*x - 1)
                    System.out.print("*");
                else if (z == 1)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }

        for (int x = n-2; x >= 0; x--) {
            for (int y = 1; y <= n-x; y++) {
                System.out.print(" ");
            }
            for (int z = 2*x + 1; z >= 1; z--) {
                if (z == 2*x + 1)
                    System.out.print("*");
                else if (z == 1)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }

    }
}

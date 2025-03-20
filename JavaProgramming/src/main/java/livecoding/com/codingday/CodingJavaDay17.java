package com.codingday;

import java.util.Scanner;

public class CodingJavaDay17 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input a: ");
        int a = input.nextInt();
        System.out.print("Input b: ");
        int b = input.nextInt();
        System.out.print("Input n: ");
        int n = input.nextInt();

        int index = 0;
        do {
            System.out.print(a+" ");
            a += b;
        } while (++index != n);

    }
}

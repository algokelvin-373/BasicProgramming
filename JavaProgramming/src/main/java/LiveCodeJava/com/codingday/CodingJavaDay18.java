package com.codingday;

import java.util.Scanner;

public class CodingJavaDay18 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input a: ");
        int a = input.nextInt();
        System.out.print("Input r: ");
        int r = input.nextInt();
        System.out.print("Input n: ");
        int n = input.nextInt();

        int index = 1;
        do {
            System.out.print(a+" ");
            a *= r;
        } while (index++ != n);

    }
}

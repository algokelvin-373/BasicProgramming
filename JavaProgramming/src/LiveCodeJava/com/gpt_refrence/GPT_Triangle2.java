package com.gpt_refrence;

import java.util.Scanner;

public class GPT_Triangle2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan tinggi segitiga: ");
        int tinggi = input.nextInt();

        for (int i = 1; i <= tinggi; i++) {
            for (int j = tinggi; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k <= i * 2 - 1; k++) {
                if (i == tinggi || k == 1 || k == i * 2 - 1) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}

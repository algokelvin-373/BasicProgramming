package com.gpt_refrence;

import java.util.Scanner;

public class GPT_Diamond {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan tinggi diamond: ");
        int tinggi = input.nextInt();

        // Bagian atas diamond
        for (int i = 1; i <= tinggi; i++) {
            for (int j = tinggi; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k <= i * 2 - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // Bagian bawah diamond
        for (int i = tinggi - 1; i >= 1; i--) {
            for (int j = tinggi; j > i; j--) {
                System.out.print(" ");
            }
            for (int k = 1; k <= i * 2 - 1; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

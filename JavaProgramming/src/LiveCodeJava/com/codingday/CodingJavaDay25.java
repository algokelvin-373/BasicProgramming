package com.codingday;

import java.util.Scanner;

public class CodingJavaDay25 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Matrix 1
        int[][] matrix01 = new int[2][2];
        System.out.println("Input Matrix 1: ");
        for (int i = 0; i < matrix01.length; i++) {
            for (int j = 0; j < matrix01[i].length; j++) {
                matrix01[i][j] = input.nextInt();
            }
        }

        // Matrix 2
        int[][] matrix02 = new int[2][2];
        System.out.println("Input Matrix 2: ");
        for (int i = 0; i < matrix02.length; i++) {
            for (int j = 0; j < matrix02[i].length; j++) {
                matrix02[i][j] = input.nextInt();
            }
        }

        // Additional
        int[][] result = new int[2][2];
        for (int i = 0; i < matrix02.length; i++) {
            for (int j = 0; j < matrix02[i].length; j++) {
                result[i][j] = matrix01[i][j] + matrix02[i][j];
            }
        }

        // Result
        System.out.println("Result Additional Matrix");
        for (int i = 0; i < matrix02.length; i++) {
            for (int j = 0; j < matrix02[i].length; j++) {
                System.out.print(result[i][j]+" ");
            }
            System.out.println();
        }

    }
}

package com.codingday;

import java.util.Random;
import java.util.Scanner;

public class CodingJavaDay21 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input size: ");
        int size = input.nextInt();

        int[] data = new int[size];

        Random random = new Random();
        for (int index = 0; index < data.length; index++) {
            data[index] = random.nextInt(1000);
        }
        for (int index = 0; index < data.length; index++) {
            System.out.print(data[index]+" ");
        }
        System.out.println();

    }
}

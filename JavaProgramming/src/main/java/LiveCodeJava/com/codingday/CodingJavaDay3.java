package com.codingday;

import java.util.Scanner;

public class CodingJavaDay3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Input Word: ");
        String word = input.nextLine();

        System.out.println("Input Number: ");
        int number = input.nextInt();

        System.out.println("Input Decimal: ");
        double decimal = input.nextDouble();

        System.out.println("Word: "+ word);
        System.out.println("Number: "+ number);
        System.out.println("Decimal: "+ decimal);

    }
}

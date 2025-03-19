package com.codingday;

import java.util.Scanner;

public class CodingJavaDay10 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input Number: ");
        int number = input.nextInt();

        if (number % 2 == 0)
            System.out.println(number+" is Even Number");
        else
            System.out.println(number+" is Odd Number");

    }
}

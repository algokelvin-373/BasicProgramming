package com.codingday;

import java.util.Scanner;

public class CodingJavaDay9 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input Number: ");
        int number = input.nextInt();

        if (number % 10 == 0)
            System.out.println(number+" is can be divided by 10");
        System.out.println("Done");

    }
}

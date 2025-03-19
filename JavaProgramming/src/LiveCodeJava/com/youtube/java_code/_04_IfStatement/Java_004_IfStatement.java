package com.youtube.java_code._04_IfStatement;

import java.util.Scanner;

public class Java_004_IfStatement {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input number: ");
        int number = input.nextInt();

        // If Conditional - Check can divide by 10
        if (number % 10 == 0) {
            System.out.println(number+" is divide by 10");
        }
        System.out.println("You input number "+ number);

    }
}

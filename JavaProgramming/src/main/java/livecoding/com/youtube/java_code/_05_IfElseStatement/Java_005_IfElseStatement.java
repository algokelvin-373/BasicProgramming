package com.youtube.java_code._05_IfElseStatement;

import java.util.Scanner;

public class Java_005_IfElseStatement {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input number: ");
        int number = input.nextInt();

        // If Else Conditional - Even or Odd Number
        if (number % 2 == 0) {
            System.out.println(number+ " is even number");
        } else { // this code will run if conditional 'IF' is not match
            System.out.println(number+ " is odd number");
        }

    }
}

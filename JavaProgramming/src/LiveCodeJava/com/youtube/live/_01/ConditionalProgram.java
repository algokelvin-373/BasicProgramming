package com.youtube.live._01;

import java.util.Scanner;

public class ConditionalProgram {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        System.out.print("Input Number: ");
        int number = input.nextInt();

        // If Statement
        if (number % 5 == 0) {
            System.out.println(number+" can be divided by 5");
        }

        // If Else Statement
        if (number % 2 == 0) {
            System.out.println(number+" is even");
        } else {
            System.out.println(number+" is odd");
        }
    }
}

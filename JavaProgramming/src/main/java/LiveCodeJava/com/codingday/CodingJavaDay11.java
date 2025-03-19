package com.codingday;

import java.util.Scanner;

public class CodingJavaDay11 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input Number 1: ");
        int number1 = input.nextInt();
        System.out.print("Input Number 2: ");
        int number2 = input.nextInt();

        System.out.println("(1). Addition (2). Subtraction");
        System.out.print("Choose: ");
        int choose = input.nextInt();

        if (choose == 1) {
            System.out.println(number1+" + "+number2+" = "+ (number1 + number2));
        } else if (choose == 2) {
            System.out.println(number1+" - "+number2+" = "+ (number1 - number2));
        } else {
            System.out.println("No available");
        }

    }
}

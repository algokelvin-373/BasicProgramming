package com.linkedin._04;

import java.util.Scanner;

public class ArmstrongNumber {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input Number: ");
        int number = input.nextInt();

        System.out.println("Is "+ number +" the Armstrong Number?");
        System.out.println(isArmstrongNumber(number));
    }
    private static boolean isArmstrongNumber(int number) {
        String data = String.valueOf(number);
        char[] digits = data.toCharArray();
        int size = data.length();

        int total = 0;
        for (int i = 0; i < size; i++) {
            total += Math.pow(digits[i] - '0', size);
        }
        return total == number;
    }
}

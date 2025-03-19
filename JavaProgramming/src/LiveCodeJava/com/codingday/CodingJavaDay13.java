package com.codingday;

import java.util.Scanner;

public class CodingJavaDay13 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("Menu:");
        System.out.println("(1). Fried Rice + Lemon Tea + Fish Role");
        System.out.println("(2). Chicken Steak + Chips + Avocado Coffee");
        System.out.println("(3). Fish Steak + Chips + Tea");
        System.out.print("Choose: ");
        int choose = input.nextInt();

        switch (choose) {
            case 1 -> {
                System.out.println("Fried Rice + Lemon Tea + Fish Role");
                System.out.println("Enjoy this meal");
            }
            case 2 -> {
                System.out.println("Chicken Steak + Chips + Avocado Coffee");
                System.out.println("Enjoy this meal");
            }
            case 3 -> {
                System.out.println("Fish Steak + Chips + Tea");
                System.out.println("Enjoy this meal");
            }
            default -> System.out.println("No Available");
        }

    }
}

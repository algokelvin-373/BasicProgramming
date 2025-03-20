package com.youtube.live._01;

import java.util.Scanner;

public class InputOutputPrograms {
    public static void main(String[] args) {
        // Use Scanner - input data
        Scanner input = new Scanner(System.in);

        // Input Number
        System.out.print("Input number: ");
        int number = input.nextInt(); // type integer

        // Input Name
        System.out.print("Input name: ");
        String name = input.next(); // type String

        // Output
        System.out.println(number);
        System.out.println(name);

    }
}

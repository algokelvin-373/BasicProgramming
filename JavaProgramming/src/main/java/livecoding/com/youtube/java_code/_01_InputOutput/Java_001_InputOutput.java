package com.youtube.java_code._01_InputOutput;

import java.util.Scanner;

public class Java_001_InputOutput {
    public static void main(String[] args) {
        // Using Scanner to Create Input Data Program
        Scanner input = new Scanner(System.in);

        // Input Data Number
        System.out.print("Input Your Number: ");
        int number = input.nextInt(); // Type data 'Integer'

        // Input Data String
        System.out.print("Input Your Name: ");
        String name = input.next(); // Type data 'String'

        // Output Data
        System.out.println("Number: "+ number); // Call variable 'number'
        System.out.println("Name: "+ name); // Call variable 'name'

    }
}

package material.m01;

import java.util.Scanner;

public class InputOutput {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in); // Input

        System.out.print("Input your name: ");
        String name = input.nextLine(); // Input Process
        System.out.println("Your name: "+ name); // Output
    }
}

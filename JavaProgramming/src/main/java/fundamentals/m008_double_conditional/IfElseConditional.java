package fundamentals.m008_double_conditional;

import java.util.Scanner;

public class IfElseConditional {
    public static void main(String[] args) {
        // Input from Keyboard using Scanner
        Scanner input = new Scanner(System.in);

        System.out.print("Input number: ");
        int number = input.nextInt();

        // Double Conditional ( If-Else )
        if (number % 2 == 0) {
            System.out.println(number + " is even");
        } else {
            System.out.println(number + " is odd");
        }
    }
}

package m011_ternary_operator;

import java.util.Scanner;

public class TernaryOperator {
    public static void main(String[] args) {
        // Input from Keyboard using Scanner
        Scanner input = new Scanner(System.in);

        System.out.print("Input number: ");
        int number = input.nextInt();

        // Ternary Operator
        String msg = (number % 2 == 0) ? "even" : "odd";
        System.out.println(number + " is " + msg);
    }
}

package m003_conditional;

import java.util.Scanner;

public class SingleConditional {
    public static void main(String[] args) {
        // Input from Keyboard using Scanner
        Scanner input = new Scanner(System.in);

        System.out.print("Input number: ");
        int number = input.nextInt();

        // Single Conditional ( If )
        if (number % 2 == 0) {
            System.out.println(number + " is even");
        }
        System.out.println("Done");
    }
}

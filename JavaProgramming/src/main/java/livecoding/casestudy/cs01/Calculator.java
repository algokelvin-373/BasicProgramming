package casestudy.cs01;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        // initialize Scanner
        Scanner input = new Scanner(System.in);

        // fundamentals.others.Looping
        for (;;) {
            // Menu
            System.out.println("Choose:");
            System.out.println("1. (+) Plus");
            System.out.println("2. (-) Minus");
            System.out.println("3. (*) Times");
            System.out.println("4. (/) Divided by");
            System.out.println("5. Exit");
            System.out.print("Input your choose: ");
            int choose = input.nextInt(); // Input

            if (choose == 5)
                break;

            // Input a and b
            System.out.println("Input a and b");
            int a = input.nextInt();
            int b = input.nextInt();

            // Conditional
            int result;
            if (choose == 1) {
                result = a + b;
                System.out.println(a +" + "+ b +" = "+ result);
            } else if (choose == 2) {
                result = a - b;
                System.out.println(a +" - "+ b +" = "+ result);
            } else if (choose == 3) {
                result = a * b;
                System.out.println(a +" * "+ b +" = "+ result);
            } else if (choose == 4) {
                result = a / b;
                System.out.println(a +" / "+ b +" = "+ result);
            }
        }

        System.out.println("END PROGRAM");

    }
}

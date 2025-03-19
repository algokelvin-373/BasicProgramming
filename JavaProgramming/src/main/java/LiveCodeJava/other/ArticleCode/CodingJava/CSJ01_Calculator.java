import java.util.Scanner;

public class CSJ01_Calculator {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        MenuCalculator();
        int a = input.nextInt();
        InputNumber(a, input);
    }

    private static void MenuCalculator() {
        System.out.println("Menu Calculator");
        System.out.println("1. Operator (+)");
        System.out.println("2. Operator (-)");
        System.out.println("3. Operator (*)");
        System.out.println("4. Operator (/)");
        System.out.println("5. Operator (%)");
        System.out.print("Pilih: ");
    }

    private static void InputNumber(int a, Scanner input) {
        System.out.print("Input number 1: ");
        int x = input.nextInt();
        System.out.print("Input number 2: ");
        int y = input.nextInt();

        if (a == 1) {
            plus(x, y);
        } else if (a == 2) {
            minus(x, y);
        } else if (a == 3) {
            times(x, y);
        } else if (a == 4) {
            divided(x, y);
        } else if (a == 5) {
            modulo(x, y);
        } else {
            System.out.println("Operator is not available");
        }
    }

    private static void plus(int x, int y) {
        System.out.println(x + " + " + y + " = " + (x+y));
    }

    private static void minus(int x, int y) {
        System.out.println(x + " - " + y + " = " + (x-y));
    }

    private static void times(int x, int y) {
        System.out.println(x + " * " + y + " = " + (x*y));
    }

    private static void divided(int x, int y) {
        System.out.println(x + " / " + y + " = " + (x/y));
    }

    private static void modulo(int x, int y) {
        System.out.println(x + " % " + y + " = " + (x%y));
    }

}

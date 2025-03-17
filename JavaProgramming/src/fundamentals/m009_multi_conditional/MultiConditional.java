import java.util.Scanner;

public class MultiConditional {
    public static void main(String[] args) {
        // Input from Keyboard using Scanner
        Scanner input = new Scanner(System.in);

        System.out.print("Input number: ");
        int number = input.nextInt();

        // Multi Conditional ( If - Else if - Else )
        if (number % 2 == 0) {
            System.out.println(number + " is divided by 2");
        } else if (number % 3 == 0) {
            System.out.println(number + " is divided by 3");
        } else {
            System.out.println(number + " isn't divided by 2 and 3");
        }
    }
}

package m010_switch_operator;

import java.util.Scanner;

public class SwitchOperator {
    public static void main(String[] args) {
        System.out.println("Card 1 || Card 2 || Card 3");

        //Input keyboard to choose card
        Scanner input = new Scanner(System.in);
        System.out.print("Choose card: ");
        int choose = input.nextInt();

        // Switch Operator
        switch (choose) {
            case 1: System.out.println("You Get IDR 5.000");
                break;
            case 2: System.out.println("You Get IDR 50.000");
                break;
            case 3: System.out.println("You Get IDR 500.000");
                break;
            default: System.out.println("Wrong to choose Card");
                break;
        }
    }
}

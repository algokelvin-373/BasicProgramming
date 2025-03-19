package material.m03;

import java.util.Scanner;

public class NilaiKuliah {
    public static void main(String[] args) {
        /*
        A -> 90 <= value <= 100
        B -> 80 <= value < 90
        C -> 70 <= value < 80
        D -> 60 <= value < 70
        E -> < 60
         */

        Scanner input = new Scanner(System.in);
        System.out.println("Input Value: ");
        int number = input.nextInt();

        // Conditional
        if (number >= 90 && number <= 100) { // To get score A
            System.out.println("Your score is A");
        } else if (number >= 80 && number < 90) { // To get score B
            System.out.println("Your score is B");
        } else if (number >= 70 && number < 80) { // To get score C
            System.out.println("Your score is C");
        } else if (number >= 60 && number < 70) { // To get score D
            System.out.println("Your score is D");
        } else { // To get score E
            System.out.println("Your score is E");
        }

    }
}

package material.m01;

import java.util.Scanner;

public class Decision {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input your score math: ");
        int score = input.nextInt();

        // Conditional
        if (score >= 90 && score <= 100) { // 90 <= x <= 100
            System.out.println("Congratulations, you get achievement");
        } else {
            System.out.println("Sorry, you're not lucky today");
        }
    }
}

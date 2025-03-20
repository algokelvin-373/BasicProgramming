package fundamentals.m008_double_conditional;

import java.util.Scanner;

public class ScoreMath {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Input Your score Math: ");
        int score = scanner.nextInt();

        // Decision Program
        if (score >= 90) {
            System.out.println("Selamat, anda dapat sepeda");
        } else {
            System.out.println("Anda belum beruntung");
        }


    }
}

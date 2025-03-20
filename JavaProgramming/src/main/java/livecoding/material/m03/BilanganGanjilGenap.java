package material.m03;

import java.util.Scanner;

public class BilanganGanjilGenap {
    public static void main(String[] args) {
        // Genap = habis dibagi 2
        // 2, 4, 6, 8 ==> mod 2 = 0 (genap)
        // 1, 3, 5, 7 ==> mod 2 = 1 (ganjil)

        Scanner input = new Scanner(System.in);
        System.out.println("Input Number: ");
        int number = input.nextInt();

        // Conditional
        if (number % 2 == 0) {
            System.out.println(number+" is genap");
        } else {
            System.out.println(number+" is ganjil");
        }

    }
}

package material.m01;

import java.util.Scanner;

public class Repeat {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Input n: ");
        int n = input.nextInt();

        // fundamentals.others.Looping - Repeat [ x++ => x = x + 1 ]
        for (int x = 1; x <= n; x++) {
            System.out.print(x +" ");
        }
        System.out.println();
    }
}

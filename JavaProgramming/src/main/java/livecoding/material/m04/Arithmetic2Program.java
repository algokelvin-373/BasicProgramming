package material.m04;

import java.util.Scanner;

public class Arithmetic2Program {
    public static void main(String[] args) {
        // 3, 7, 11, 15, 19  --> a = 3, n = 5, b = 4
        // 1, 3, 5, 7, 9 --> a = 1, n = 5, b = 2
        // fundamentals.others.Arithmetic: a + b(n - 1)

        Scanner input = new Scanner(System.in);
        System.out.print("Input data n: ");
        int n = input.nextInt();
        System.out.print("Input data a: ");
        int a = input.nextInt();
        System.out.print("Input data b: ");
        int b = input.nextInt();

        for (int index = a; index <= a + b*(n-1); index += b) {
            System.out.print(index+" ");
        }

        // fundamentals.others.Looping
        int num = 3;
        for (int index = 1; index <= 5; index++) {
            System.out.print(num+" ");
            num = num + 4;
        }

    }
}

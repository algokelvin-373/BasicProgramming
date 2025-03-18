package com.youtube.live._01;

public class ArrayProgram {
    public static void main(String[] args) {
        // Define
        int[] number1 = {1, 2, 3, 4, 5};
        for (int num1: number1) {
            System.out.print(num1+" ");
        }

        System.out.println();

        // Define 2
        int[] number2 = new int[5];
        for (int i = 0; i < number2.length; i++) {
            number2[i] = i + 1;
        }
        for (int num2: number2) {
            System.out.print(num2+" ");
        }

    }
}

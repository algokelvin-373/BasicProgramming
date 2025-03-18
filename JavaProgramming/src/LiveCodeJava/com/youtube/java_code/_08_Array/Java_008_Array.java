package com.youtube.java_code._08_Array;

public class Java_008_Array {
    public static void main(String[] args) {
        // Define array with size 5
        int[] number = new int[5];

        // Add value using lopping 'for'
        System.out.println("Process Add Value");
        for (int i = 0; i < number.length; i++) {
            number[i] = (i + 1);
        }

        // Show array - Just set variable 'number'
        System.out.println("Show Array");
        for (int j : number) {
            System.out.print(j + " ");
        }
        System.out.println();

        // Set Array (replace value)
        System.out.println("Set Value Array");
        number[0] = 100; // using index
        number[2] = 200;

        for (int k: number) {
            System.out.print(k + " ");
        }

    }
}

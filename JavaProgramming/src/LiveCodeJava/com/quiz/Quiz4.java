package com.quiz;

public class Quiz4 {
    public static void main(String[] args) {
        // Quiz Java Learning 04 - Array Data Part 1
        int[] data = new int[5];
        int a = 10;
        for (int x = 0; x < data.length; x++) {
            data[x] = a + x;
        }
        for (int y: data) {
            System.out.print(y+" ");
        }
    }
}

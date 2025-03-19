package com.quiz;

public class Quiz5 {
    public static void main(String[] args) {
        // Quiz Java Learning 05 - Array Data Part 2
        int[] data = new int[5];
        int a = 2, b = 3;
        int max = a + (data.length - 1)*b;
        int x = 0; // answer
        for (int result = a; result <= max;) {
            data[x++] = result;
            result += b; // answer
        }
        for (int y: data) {
            System.out.print(y+" ");
        }
    }
}

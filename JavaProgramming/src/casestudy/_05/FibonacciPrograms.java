package com.linkedin._05;

public class FibonacciPrograms {
    public static void main(String[] args) {
        int[] fib10 = fibonacci(10);
        int[] fib20 = fibonacci(20);

        System.out.println("\n Fibonacci (n = 10)");
        for (int i : fib10) {
            System.out.print(i + " ");
        }
        System.out.println("\n Fibonacci (n = 20)");
        for (int j : fib20) {
            System.out.print(j + " ");
        }

    }
    private static int[] fibonacci(int n) {
        int[] fibArray = new int[n];
        for (int i = 0; i < fibArray.length; i++) {
            if (i == 0) {
                fibArray[i] = 0;
            } else if (i == 1){
                fibArray[i] = 1;
            } else {
                fibArray[i] += fibArray[i-1] + fibArray[i-2];
            }
        }
        return fibArray;
    }
}

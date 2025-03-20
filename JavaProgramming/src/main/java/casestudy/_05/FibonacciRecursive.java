package com.linkedin._05;

public class FibonacciRecursive {
    public static void main(String[] args) {
        int result1 = fibonacci(100);
        System.out.println(result1);
    }
    private static int fibonacci(int n) {
        if (n <= 1) return n;
        else return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

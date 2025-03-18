package com.linkedin._06;

public class FactorialProgram {
    public static void main(String[] args) {
        System.out.println("---12---");
        factorial(17);
        System.out.println();
        System.out.println("---100---");
        factorial(100);
        System.out.println();
    }
    private static void factorial(int number) {
        int data = number;
        for (int i = 1; i <= data; i++) {
            int mod = number % i;
            int result = number / i;
            if (mod == 0) {
                if ((i == data) && (i != result)) {
                    continue;
                } else {
                    data = result;
                    System.out.println(i +" "+ result);
                }
            }
        }
    }
}

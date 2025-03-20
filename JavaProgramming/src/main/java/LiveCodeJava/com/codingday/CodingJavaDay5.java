package com.codingday;

public class CodingJavaDay5 {
    public static void main(String[] args) {
        // Case 1: Algebra
        int a = 10, b = 5, c = 2, d = 3;

        int result1 = a + b * c - d;
        int result2 = (a + b) * (c - d);
        int result3 = (a + c + d) / b;
        int result4 = (a + b) * d / c;
        int result5 = (b * c) / a * d;

        System.out.println("Result1: "+result1);
        System.out.println("Result2: "+result2);
        System.out.println("Result3: "+result3);
        System.out.println("Result4: "+result4);
        System.out.println("Result5: "+result5);

    }
}

package com.quiz;

public class Quiz8 {
    public static void main(String[] args) {
        // Quiz Java Learning 08 - Methods 1
        add(2, 3);
        add(2.1, 2.2);
    }
    public static void add(int a, int b) {
        System.out.println(a + b);
    }
    public static void add(double a, double b) {

    }

    /*
    int resultA = add(3, 7);
    double resultB = add(2.3, 3.2);

    public static int add(int a, int b) { return a + b; }
    public static double add(double a, double b) { return a + b; }

    Create method 'add' with 2 parameter type data integer, then set 'a + b' [false]
    Create method 'add' with 2 parameter type data integer, then return data from the result 'a + b' [true]
    Create method 'add' with 2 parameter type data double, then set 'a + b' [false]
    Create method 'add' with 2 parameter type data double, then return data from the result 'a + b' type integer [false]
    Create method 'add' with 2 parameter type data double, then return data from the result 'a + b' type double [true]
     */

}

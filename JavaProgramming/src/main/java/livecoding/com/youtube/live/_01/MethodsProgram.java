package com.youtube.live._01;

public class MethodsProgram {
    public static void main(String[] args) {
        getMessage();
        setNumber(100);

        String str = getMessage2();
        System.out.println(str);
    }

    // fundamentals.others.Function without parameter and return data
    public static void getMessage() {
        System.out.println("Welcome");
    }
    // fundamentals.others.Function with parameter, without return data
    public static void setNumber(int number) {
        System.out.println(number);
    }
    // fundamentals.others.Function with return data, without parameter
    public static String getMessage2() {
        return "Welcome My Channel AlgoKelvin";
    }
}

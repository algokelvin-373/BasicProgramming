package com.youtube.java_code._10_Function;

public class Java_010_Function {
    public static void main(String[] args) {
        func01();
        func02("Function 2: With parameter, without return data");
        System.out.println(func03());
        System.out.println(func04("Function 4: With parameter & return data"));
    }

    // function without parameter dan return data
    private static void func01() {
        System.out.println("Function 1: without parameter & return data");
    }

    // function with parameter, however without return data
    private static void func02(String msg) {
        System.out.println(msg);
    }

    // function with return data, however without parameter
    private static String func03() {
        return "Function 3: With return data, without parameter";
    }

    // function with parameter & return data
    private static String func04(String msg) {
        return msg;
    }

}

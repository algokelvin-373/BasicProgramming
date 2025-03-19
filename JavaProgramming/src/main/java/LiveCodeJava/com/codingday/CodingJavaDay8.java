package com.codingday;

public class CodingJavaDay8 {
    public static void main(String[] args) {
        boolean a = true, b = false;

        System.out.println("Logical AND");
        System.out.println(a+" && "+ a +" = "+ (a && a));
        System.out.println(a+" && "+ b +" = "+ (a && b));
        System.out.println(b+" && "+ a +" = "+ (b && a));
        System.out.println(b+" && "+ b +" = "+ (b && b));

        System.out.println("Logical OR");
        System.out.println(a+" || "+ a +" = "+ (a || a));
        System.out.println(a+" || "+ b +" = "+ (a || b));
        System.out.println(b+" || "+ a +" = "+ (b || a));
        System.out.println(b+" || "+ b +" = "+ (b || b));

        System.out.println("Logical NOT");
        System.out.println("!"+a+" = "+ !a);
        System.out.println("!"+b+" = "+ !b);

    }
}

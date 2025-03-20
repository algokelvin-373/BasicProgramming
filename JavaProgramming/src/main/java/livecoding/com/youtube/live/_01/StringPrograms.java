package com.youtube.live._01;

public class StringPrograms {
    public static void main(String[] args) {
        String strNum = "12";
        String strWord = "Coding";

        String word = "I Love Coding Java";

        String str1 = word.toUpperCase(); // Make all Capital
        String str2 = word.substring(2, 6); // index 2 - 5
        String str3 = word.replace("Java", "Kotlin");

        System.out.println(str1);
        System.out.println(str2);
        System.out.println(str3);


    }
}

package com.quiz;

import java.util.ArrayList;
import java.util.List;

public class Quiz7 {
    public static void main(String[] args) {
        // Quiz Java Learning 07 - List

        List<String> list = new ArrayList<>();
        list.add("Java");
        list.add("Kotlin");
        list.add("Python");

        list.set(2, "Java");
        list.remove(0);

        for (String y: list) {
            System.out.print(y+" ");
        }

        // Set "Java" on index 2 and remove data on index 0 [True]
        // Remove data on index 2 [False]
        // Set "Java" on index 1 and remove data on index 2 [False]

    }
}

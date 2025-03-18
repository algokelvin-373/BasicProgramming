package com.youtube.java_code._09_ArrayList;

import java.util.ArrayList;

public class Java_009_ArrayList {
    public static void main(String[] args) {
        // Define Array List
        ArrayList<String> coding = new ArrayList<>();

        // Add data
        System.out.println("Add Data");
        coding.add("Java");
        coding.add("Kotlin");
        coding.add("Python");
        coding.add("Javascript");
        System.out.println();
        // Result: Java - Kotlin - Python - Javascript

        // Show data
        System.out.println("Show Data");
        for (String data: coding) {
            System.out.println(data);
        }
        System.out.println();

        // Set Data
        System.out.println("Set data index 1");
        coding.set(1, "Dart"); // Change 'Kotlin' to 'Dart'
        System.out.println();
        // Result: Java - Dart - Python - Javascript

        // Delete Data
        System.out.println("Remove data index 0");
        coding.remove(0); // Remove index 0 - 'Java'
        System.out.println();
        // Result: Dart - Python - Javascript

        // Show data
        System.out.println("Show Data");
        for (String data: coding) {
            System.out.println(data);
        }
        System.out.println();

    }
}

package com.linkedin._02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadFile {
    public static void main(String[] args) throws FileNotFoundException {
        File file = new File("src/li/_02/sample.txt");
        Scanner reader = new Scanner(file);
        while (reader.hasNextLine()) {
            System.out.println(reader.nextLine());
        }
    }
}

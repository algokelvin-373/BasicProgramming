package com.linkedin._03;

import java.io.FileWriter;
import java.io.IOException;

public class WriteFile {
    public static void main(String[] args) {
        try {
            FileWriter writeFile = new FileWriter("src/li/_03/writeFile.txt");
            writeFile.write("I create my file");
            writeFile.close();
            System.out.println("Successfully create and wrote to file");
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}

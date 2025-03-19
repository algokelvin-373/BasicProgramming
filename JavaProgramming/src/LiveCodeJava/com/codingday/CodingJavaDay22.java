package com.codingday;

public class CodingJavaDay22 {
    public static void main(String[] args) {
        String[][] array2D = {
                {"Java", "Kotlin", "C++"},
                {"HTML", "CSS", "Javascript"}
        };

        for (int x = 0; x < array2D.length; x++) {
            for (int y = 0; y < array2D[x].length; y++) {
                System.out.print(array2D[x][y]+" ");
            }
            System.out.println();
        }

    }
}

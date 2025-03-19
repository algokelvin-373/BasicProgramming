package com.quiz;

public class Quiz {

    public static void main(String[] args) {

        String data = "I love coding Java";
        System.out.println(countingWord(data));
    }

    private static int countingWord(String data) {
        int count = 1;
        for (char ch: data.toCharArray()) {
            if (ch == 32) {
                count++;
            }
        }
        return count;
    }

}

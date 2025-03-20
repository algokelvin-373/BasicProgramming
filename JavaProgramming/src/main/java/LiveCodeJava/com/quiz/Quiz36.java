package com.quiz;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class Quiz36 {
    public static void main(String[] args) {
        String format = "yyyy-MM-dd'T'HH:mm:ss'Z'";
        LocalDateTime localDateTime = LocalDateTime.now();
        DateTimeFormatter formatted = DateTimeFormatter.ofPattern(format);
        String date = formatted.format(localDateTime);
        System.out.println(date);
    }
}

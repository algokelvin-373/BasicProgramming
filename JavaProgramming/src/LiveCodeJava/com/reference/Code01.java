package com.reference;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Code01 {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        try {
            String str1 = br.readLine().toUpperCase();
            String str2 = br.readLine().toUpperCase();
            System.out.println(str1+" "+str2);
        } catch (IOException e) {
            System.out.println("Error !");
        }



    }
}

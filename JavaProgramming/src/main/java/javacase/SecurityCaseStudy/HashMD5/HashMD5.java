package javacase.SecurityCaseStudy.HashMD5;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class HashMD5 {
    public static void main(String[] args) {

        String hashtext = null;
        Scanner input = new Scanner(System.in);
        System.out.print("Input text: ");
        String data = input.nextLine();

        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] messageDigest = md.digest(data.getBytes());
            BigInteger no = new BigInteger(1, messageDigest);
            hashtext = no.toString(16);
            while (hashtext.length() < 32) {
                hashtext = "0" + hashtext;
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }

        System.out.println("MD5 : "+hashtext);
    }
}

package javacase.SecurityCaseStudy.HashMD5;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class TestHashMD5 {
    public static void main(String[] args) {

        String hashtext = null;
        String a = "D1234";
        String b = "01234567897968123456789FB05332AF";
        String c = "abcde12345";
        String data = a + b + c;
        System.out.println("Data: "+data);

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

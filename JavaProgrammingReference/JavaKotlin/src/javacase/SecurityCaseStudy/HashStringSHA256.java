package javacase.SecurityCaseStudy;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class HashStringSHA256 {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String str = "StackHowTo";

        MessageDigest msg = MessageDigest.getInstance("SHA-256");
        byte[] hash = msg.digest(str.getBytes(StandardCharsets.UTF_8));

        //Convert byte to hexadecimal
        StringBuilder s = new StringBuilder();
        for (byte b: hash) {
            s.append(Integer.toString((b & 0xff) + 0x100, 16).substring(1));
        }

        System.out.println(s.toString());
    }
}

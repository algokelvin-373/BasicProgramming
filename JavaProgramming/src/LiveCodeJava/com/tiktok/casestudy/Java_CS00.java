package com.tiktok.casestudy;

public class Java_CS00 {
    public static void main(String[] args) {
        String[] lines = {
                "000111111111000011111110000111000000000001110000111111100",
                "000000001111000011111110000001100000000011000000111111100",
                "000000001111000111000111000000110000000110000001110001110"
        };

        for (String s : lines) {
            for (int index = 0; index < s.length(); index++) {
                if (s.charAt(index) == '1')
                    System.out.print("#");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }

//        String line01 = "000111111111000011111110000111000000000001110000111111100";
//        String line02 = "000111111111000011111110000111000000000001110000111111100";
//        System.out.println("   #########    AAAAAAA    VVV           VVV    AAAAAAA  ");
//        System.out.println("        JJJJ    AAAAAAA      VV         VV      AAAAAAA  ");
//        System.out.println("        JJJJ   AAA   AAA      VV       VV      AAA   AAA ");
        System.out.println("        JJJJ   AAA   AAA       VV     VV       AAA   AAA ");
        System.out.println("J       JJJJ   AAAAAAAAA        VV   VV        AAAAAAAAA ");
        System.out.println("J       JJJJ   AAAAAAAAA         VV VV         AAAAAAAAA ");
        System.out.println("J       JJJJ   AAA   AAA          VVV          AAA   AAA ");
        System.out.println("JJ     JJJJ    AAA   AAA          VVV          AAA   AAA ");
        System.out.println(" JJJJJJJJJ     AAA   AAA           V           AAA   AAA ");
    }
}

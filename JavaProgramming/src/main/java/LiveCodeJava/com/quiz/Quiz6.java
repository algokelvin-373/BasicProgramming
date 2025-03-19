package com.quiz;

import java.util.ArrayList;
import java.util.List;

public class Quiz6 {
    public static void main(String[] args) {
        // Quiz Java Learning 06 - ArrayList

        ArrayList<Integer> arrNum = new ArrayList<>();
        int a = 3, r = 2, n = 5;
        for (int x = 1; x++ <= n;) { // answer
            arrNum.add(a);
            a *= r;
        }

        for (int y: arrNum) {
            System.out.print(y+" ");
        }

        // for (int x = 1; x <= n; x++) true
        // for (int x = 0; x <= n; x++) false
        // for (int x = 1; x++ <= n;) true

    }
}

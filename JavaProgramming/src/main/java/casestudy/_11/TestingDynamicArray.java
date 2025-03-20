package com.linkedin._11;

import java.util.Random;

public class TestingDynamicArray {
    public static void main(String[] args) {
        Random random = new Random();

        //DynamicArray array = new DynamicArray();

        // Testing runtime
        int n = 1000000;
        long start = System.currentTimeMillis();
        for (int i = 1; i <= n; i++) {
            //array.add(random.nextInt(10000000));
        }
        long finish = System.currentTimeMillis();
        System.out.println(n+ " data = "+ (finish - start) +" ms");

    }
}

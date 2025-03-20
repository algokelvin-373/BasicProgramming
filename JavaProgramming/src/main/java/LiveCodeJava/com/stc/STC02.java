package com.stc;

import java.util.Arrays;

public class STC02 {
    public static void main(String[] args) {
        int[] numbers = {5, 3, 2, 4, 1};

        // filter
        int[] filterNumber = Arrays.stream(numbers)
                .filter(n -> n % 2 == 0)
                .toArray();

        System.out.println(Arrays.toString(filterNumber));

        // map
        int[] mapNumber = Arrays.stream(numbers)
                .map(n -> n * 2)
                .toArray();

        System.out.println(Arrays.toString(mapNumber));

        // limit
        int[] limitNumber = Arrays.stream(numbers)
                .limit(3)
                .toArray();

        System.out.println(Arrays.toString(limitNumber));

        // sort
        int[] sortNumber = Arrays.stream(numbers)
                .sorted()
                .toArray();

        System.out.println(Arrays.toString(sortNumber));

    }
}

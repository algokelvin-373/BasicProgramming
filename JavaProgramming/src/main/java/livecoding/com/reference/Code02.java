package com.reference;

import java.util.List;

public class Code02 {
    public static void main(String[] args) {

    }
    public static int solution(List<Integer> a) {
        int result = 0;
        for (int index = 0; index < a.size();) {
            result += a.get(index++);
        }
        return result;
    }
}

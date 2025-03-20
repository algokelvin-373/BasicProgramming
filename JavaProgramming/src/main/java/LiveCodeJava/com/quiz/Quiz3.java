package com.quiz;

import java.util.HashMap;
import java.util.Map;

public class Quiz3 {
    public static void main(String[] args) {
        // Quiz Learning Java 03 - HashMap and Map
        Map<String, Object> map = new HashMap<>();
        map.put("a1", "Java");
        map.put("a2", 200);
        map.put("a3", true);
        map.replace("a2", 500);

        Object v1 = map.get("a1");
        Object v2 = map.get("a2");
        Object v3 = map.get("a3");
        System.out.println(v1+" "+v2+" "+v3);

    }
}

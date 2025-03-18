package fundamentals.m017_list;

import java.util.ArrayList;
import java.util.List;

public class ListAddData {
    public static void main(String[] args) {
        List<String> datas = new ArrayList<>();

        // Add datas
        datas.add("Java");
        datas.add("Kotlin");
        datas.add("Python");
        datas.add("Dart");
        datas.add("Swift");

        // Show List
        System.out.println("List Programming: ");
        for (String data : datas) {
            System.err.println(data);
        }
    }
}

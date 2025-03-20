package fundamentals.m016_array_list;

import java.util.ArrayList;

public class ArrayListGetData {
    public static void main(String[] args) {
        ArrayList<Integer> dtNumber = new ArrayList<>();
        // Add Data 1, 2, 3, 4, 5
        dtNumber.add(1);
        dtNumber.add(2);
        dtNumber.add(3);
        dtNumber.add(4);
        dtNumber.add(5);

        // Get Data for index
        System.out.println("ArrayList data number: ");
        System.out.print(dtNumber.get(0)+" ");
        System.out.print(dtNumber.get(1)+" ");
        System.out.print(dtNumber.get(2)+" ");
        System.out.print(dtNumber.get(3)+" ");
        System.out.print(dtNumber.get(4)+" ");
    }
}
